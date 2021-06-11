# Transfer Stuff #

## Overview ##
How to move stuff from one place to another

## Hugging Face ##
git bash

    cd d:
    cd workspaces
    mkdir huggingface
    git clone https://huggingface.co/repo D:\\workspaces\\huggingface\\reponame --depth 1

**--depth 1 is to save bandwidth and copies default main / master. Use --branch \<name\> to otherwise specify**

Scan, zip, transfer


## R Packages ##

from R-Studio on an internet connected computer...

    >getPackages <- function(packs){
        packages <- unlist(
            tools::package_dependencies(packs, available.packages(),
                         which=c("Depends", "Imports"), recursive=TRUE)
         )
    packages <- union(packs, packages)
    packages
    }

    packages <- getPackages(c("packagename"))

    download.packages("packagename", destdir="C:\\users\\harrisal\\tidyverse_packages",type="win.binary")

    download.packages(packages, destdir="C:\\users\\harrisal\\tidyverse_packages", type="win.binary")

save all the packages, move them to isolated computer then run R-Studio 

    setwd("path/packages/") #set the working directory to the path of the packages
    pkgs <- list.files()
    
    install.packages(c(print(as.character(pkgs), collapse="\",\"")), repos = NULL, type = "win.binary")

if you cannot run as admin then run something like the following

    install.packages(c(print(as.character(pkgs), collapse="\",\"")), repos = NULL, type = "win.binary", lib=c:\\users\\harrisal\\mypackages)

then copy all folders in *mypackages* to the rstudio folder (e.g. \R\win-library\4.0)


## Spacy ##

* Use pip download

        pip download https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0-py3-none-any.whl

        pip download https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.0.0/en_core_web_md-3.0.0-py3-none-any.whl


        https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.0.0/en_core_web_lg-3.0.0-py3-none-any.whl

        https://github.com/explosion/spacy-models/releases/download/en_core_web_trf-3.0.0/en_core_web_trf-3.0.0-py3-none-any.whl