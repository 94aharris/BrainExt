# Blog Setup #

https://anthonybrainext.netlify.app/

## Resources ##

- [Homebrew on Linux](https://docs.brew.sh/Homebrew-on-Linux)
- [Installing Hugo](https://gohugo.io/getting-started/quick-start/)
- [Hugo Quickstart](https://gohugo.io/getting-started/quick-start/)
- [GeekDoc Theme](https://themes.gohugo.io/themes/hugo-geekdoc/)
- [GeekDoc Getting Started](https://geekdocs.de/usage/getting-started/)
- [Hugo Static Files](https://gohugo.io/content-management/static-files/)
- [Netlifi Toml](https://docs.netlify.com/configure-builds/file-based-configuration/#sample-file)
- [Hosting Hugo on Netlifi](https://gohugo.io/hosting-and-deployment/hosting-on-netlify/)
  
  
## Blog Stack Overview ##

- Using Netlify
- Using Hugo
- Using Centos 8

Future state
blog.<siteurl>.com
brainext.<siteurl>.com
  
## Setting up Hugo ##

Install Homebrew to the computer

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Add brew command to path

```bash
test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile
echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
```

Install hugo

```bash
brew install hugo
```

Start with hugo

create a new directory, create the site, and add the learn theme

```bash
mkdir hugosite
cd hugosite
hugo new site quickstart
cd quickstart
```

Add the Geekdoc Theme (pre-built)

- Download the prebuilt

```bash
mkdir -p themes/hugo-geekdoc/
curl -L https://github.com/thegeeklab/hugo-geekdoc/releases/latest/download/hugo-geekdoc.tar.gz | tar -xz -C themes/hugo-geekdoc/ --strip-components=1
```

- Reference the Geekdoc Docs for config
  - Add the basic config to the hugo config.toml file
  - In each folder create an **_index.md** file to control collapse levels and title the folder
  - Add any images under /static folder in a new /static/images folder. All references become relative (e.g \!\[this image\]\(\\images\\image.png\))

See how it all looks with a hugo build

```bash
hugo server -D
```

Integrate with netlify 

Current Option - netlify Wired up to Git

- Wired up to the Brainext/netlifi branch
- In the project root add netlifi.toml
- Make sure to set **Hugo Version**
- If you receive an error like below you probably didn't set the version

```  
"Error: "/opt/build/repo/themes/hugo-geekdoc/layouts/partials/title.html:11:1": parse failed: template: partials/title.html:11: function "return" not defined"
```


```toml
[context.production.environment]
HUGO_VERSION = "0.86.0"
```

Backup Option - Easy manual build 

- Perform a hugo build `hugo -D`
  - make sure the config.toml reflects the correct website base url
- Upload the 'public' folder to netlify