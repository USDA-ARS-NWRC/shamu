# SHAMU v0.1.0

shamu is a shortcut commandline tool to quickly open and enter a docker
interactively with mounted volumes. Specifically Shamu tackles that docker
volume mounts are required to be absolute and thats always driven me crazy.
So shamu wraps the docker run command and pipes in your images and mount
options. I do realize that docker-compose files can do this as well but I
often run around to different folders and jump into dockers to run some
commands and exit it. Shamu help do interactive dockers on the fly with
volume mounts.

## INSTALL

**Prequisites**:

- docker
- python3.5 +
- pip

Once docker, python, and pip are installed, install shamu using pip:

``` bash
$ pip install -u shamu
```

## Usage

``` bash
$  shamu < image name > -v ./:
```
*Working Example* with two volumes

``` bash
  $ shamu usdaarsnwrc/basin_setup:develop -v ./:/Data ~/Downloads:/Downloads
```
