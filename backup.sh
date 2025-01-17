
cd $( dirname $0 )

BKP_DIR=~/var/website.$( date +%Y-%b-%d_%Hh%Mm )

rsync -av . $BKP_DIR
du -sh $BKP_DIR

