#!/bin/bash
docker run -it --rm  --name myword2vec \
  -v $(pwd):/mnt/work  -w /mnt/work \
  3hdeng/zake-word2vec:2.7 \
  /bin/bash



# -v $HOME/workspaces/spacy/data:/usr/local/lib/python2.7/dist-packages/spacy/data \
#  -v $HOME/workspaces/wiki:/mnt/work/data/wiki \
#  -p 8888:8888 \

