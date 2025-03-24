#!/usr/bin/env bash

cd $( dirname $0 )

die() { echo "$0: die - $*" >&2; exit 1; }

[ ! -f Catalog.fr.rtf ] && die "[$PWD] File missing - Catalog.fr.rtf"
[ ! -f Catalog.fr.pdf ] && die "[$PWD] File missing - Catalog.fr.pdf"

set -x; rm -rf TR_*/; set +x

../../../scripts/rtf2md.py $* Catalog.fr.rtf

