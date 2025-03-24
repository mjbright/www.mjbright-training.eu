#!/usr/bin/env bash

cd $( dirname $0 )

die() { echo "$0: die - $*" >&2; exit 1; }

[ ! -f Catalog.rtf ] && die "[$PWD] File missing - Catalog.rtf"
[ ! -f Catalog.pdf ] && die "[$PWD] File missing - Catalog.pdf"

set -x; rm -rf TR_*/; set +x

../../../scripts/rtf2md.py $*

