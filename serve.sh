
cd $( dirname $0 )
grep -ir draft content/ | grep -v contribution-guidelines.md | grep draft && {
    echo; echo "WARNING: some pages have draft setting"
    read
}


hugo serve
