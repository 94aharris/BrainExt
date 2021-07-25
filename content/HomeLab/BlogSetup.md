# Blog Setup #

## Resources ##

- [Homebrew on Linux](https://docs.brew.sh/Homebrew-on-Linux)
- [Installing Hugo](https://gohugo.io/getting-started/quick-start/)
- [Hugo Quickstart](https://gohugo.io/getting-started/quick-start/)
  
## Blog Stack Overview ##

- Using Netlify
- Using Hugo
- Using Centos 8
  
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
cd themes
git clone https://github.com/matcornic/hugo-theme-learn.git
```



