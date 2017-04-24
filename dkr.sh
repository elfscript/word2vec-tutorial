#!/bin/bash
docker run -it --rm  --name my10k \
  -v $(pwd):/mnt/work  -w /mnt/work \
  -v $HOME/workspaces/spacy/data:/usr/local/lib/python2.7/dist-packages/spacy/data \
  -v $HOME/workspaces/wiki:/mnt/work/data/wiki \
  -p 8888:8888 \
  3hdeng/zake-word2vec:cpu \
  /bin/bash

# -p 7474:7474 \
	 
#    -v $gitRepo:/opt/$USER/repos \
#    -e "OPTION_NAME=OPTION_VALUE" \
#   -v /tmp/.X11-unix:/tmp/.X11-unix \
# /usr/local/lib/python2.7/dist-packages/spacy/data
