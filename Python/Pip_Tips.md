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

## Errors and Resolutions ##

* On pip install **"ERROR: Cannot uninstall 'PyYAML'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall"**
  * Resolution: `pip install --ignore-installed PyYAML` This will attempt to install the newer version of PyYAML on top of the existing installation without uninstalling the old version. Once that completes, then try installing the other package.