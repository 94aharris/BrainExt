# Pip Tips #

## Downloading Packages ##

* [Pip Download Docs](https://pip.pypa.io/en/stable/cli/pip_download/)
* *downloading packages and dependencies*
  * `pip download \<packageName\>`
* *downloading packages for specific platform*
  * **must use --only-binary:all: as well**
  * `pip download --platform manylinux1_x86_64 --only-binary=:all: --python 38 SomePackage`
* valid platforms
  * linux_x86_64
  * manylinux1_x86_64
  * win32
  * win_amd64
* specify python version
  * `--python-version 37`
* specify package version
  * `SomePackage==1.0`