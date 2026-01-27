#!/usr/bin/env bash

die() { echo "$0: die - $*" >&2; exit 1; }

cd $( dirname $0 )

die "Revert to manual creation of catalog markdown files"

~/scripts/TRAINING_catalog_xlsx.py


OLD_GDRIVE_METHOD() {
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
}

