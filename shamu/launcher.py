#!/usr/bin/env python3

import argparse
from subprocess import Popen, PIPE, check_output, STDOUT
import sys
import os
from os.path import abspath, expanduser
import coloredlogs
import logging
import pwd

from shamu import __version__


class DockerLaunch(object):
    def __init__(self,**kwargs):
        # Set all of them as attributes
        for k,v in kwargs.items():
            setattr(self,k,v)

        if self.debug:
            level = logging.getLevelName("DEBUG")
        else:
            level = logging.getLevelName("INFO")

        # Add a custom format for logging
        fmt = "%(levelname)s: %(msg)s"

        self.log = logging.getLogger(__name__)

        # Always write to the screen
        coloredlogs.install(logger=self.log, level=level,
                                                 fmt=fmt)

        self.log.info("SHAMU V{}".format(__version__))
        self.log.info("Interpreting your docker command...")

        self.uid = pwd.getpwuid( os.getuid() ).pw_uid

        self.volumes = self.format_volumes()

    def format_volumes(self):
        """
        Volumes are passed in as a list of colon separate key value pairs
        this parses them and converts them into a the absolute paths required.
        """

        self.log.debug("Converting volume format to absolute paths")
        result = {}

        # Check the paths.
        for v in self.volumes:
            paths = v.split(":")

            # Unix paths
            if len(paths) == 2:
                path, mountable = paths[0:2]

            # Likely a windows sitch
            elif len(paths) == 3:
                drive, path, mountable = paths[0:3]
                path = drive + path

            else:
                raise ValueError("Unable to parse local paths without a single"
                                 " colon and no more than two colons in it."
                                 "\n Problem Raised by {}"
                                 "".format(v))
            path = abspath(expanduser(path))
            result[path] = mountable

        return result

    def run(self):
        """
        Forms the command and executes the command
        """
        volume_string = " ".join(["-v {}:{}".format(k, v) for k, v in self.volumes.items()])
        cmd = "docker run -it --rm --entrypoint {} --user {} {} {}".format(
                                                                    self.entrypoint,
                                                                    self.uid,
                                                                    volume_string,
                                                                    self.image)
        self.log.debug(cmd)
        os.system(cmd)

def main():
    """
    Provides a interface to launch dockers
    """
    p = argparse.ArgumentParser(description='Launches dockers!')

    p.add_argument(dest="docker_image",
                   help="Docker image to use")

    p.add_argument("-v", dest="volumes",
                    required=False,
                    nargs="+",
                    help="Paths to pass to map volumes just like docker but can"
                         " be relative or absolute, passing multiple is space"
                         " separated.")

    p.add_argument("-e","--entrypoint", dest="entrypoint",
                    default="/bin/bash",
                    help="Docker image to use")
    p.add_argument("-d","--debug", dest="debug",
                    action="store_true",
                    help="Output debug info")
    args = p.parse_args()


    shamu = DockerLaunch(image=args.docker_image, volumes=args.volumes,
                                                  entrypoint=args.entrypoint,
                                                  debug=args.debug)
    shamu.run()
