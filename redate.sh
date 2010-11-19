#!/bin/bash

FILE=$1
BASE=`echo $FILE|cut -d'-' -f4`
DATE=`date +%Y-%m-%d`
mv $FILE _posts/$DATE-$BASE
