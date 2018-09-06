#!/usr/bin/env bash
folder=$($@);
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
$DIR/exism.py $folder
echo $folder

if [[ -d $folder ]] ; then
    cd $folder
fi

# need to add an alias :
# alias exercism='. /path/to/exism.sh exercism'