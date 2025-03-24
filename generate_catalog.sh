#!/usr/bin/env bash

die() { echo "$0: die - $*" >&2; exit 1; }

cd $( dirname $0 )

cd content/fr/docs
    echo
    read -p "[$PWD]: About to generate docs"
    ./generate_catalog.sh $*
cd -

cd content/en/docs
    echo
    read -p "[$PWD]: About to generate docs"
    ./generate_catalog.sh $*
cd -

