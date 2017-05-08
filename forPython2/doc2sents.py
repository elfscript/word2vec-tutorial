# -*- coding: utf-8 -*-
import gensim.models.word2vec as word2vec
sents=word2vec.LineSentence("sample1.txt")
for sent in sents: 
  print(len(sent), "=======================")
  print(u"---".join(sent))


import io
def zhPar2Sents(fname):
  sents=[]
  with io.open(fname, 'r', encoding='utf8') as f:
     for line in f:
        sents.extend(line.split(u'。'))
  
  return sents

sents=zhPar2Sents("sample1.txt")
for sent in sents:
  print("=======================")
  print(sent)

     
