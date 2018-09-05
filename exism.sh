#!/usr/bin/env bash
folder=$($@);
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
$DIR/exism.py $folder
echo $folder;

function jump(){
    cd $folder;
};

jump

# need to add an alias :
# exercism='. /path/to/exism.sh exercism'