#!/bin/bash

SCRIPPATH="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $SCRIPPATH; zsh; source .ve/bin/activate;
