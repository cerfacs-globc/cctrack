#!/bin/sh
#

LIST=$1

WGET="wget -nc"

#--output-document=

# Get all files and save with proper names
#
while read -r line; do
  name="$line"
  echo "$name"
  url=`echo $name | awk '{print $1}'`
  output=`echo $name | awk '{print $2}'`
  $WGET --output-document="$output" "$url"
done < "$LIST"
