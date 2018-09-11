#!/usr/bin/env bash
folder=$($@)

echo "$folder"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
$DIR/exism.py $folder

if [[ -d $folder ]] ; then
    cd $folder
fi
