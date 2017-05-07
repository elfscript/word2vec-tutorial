#!/bin/bash
if [[ $# == "1" ]]; then
  wiki_bz2_fname=$1
  echo $wiki_bz2_fname
else
  echo "bat_wiki.sh wiki_bz2_fname"
  exit 
fi

python wiki_to_txt.py $wiki_bz2_fname
#opencc -i  wiki_texts.txt -o wiki_zh_tw.txt

python segment.py

python train.py



