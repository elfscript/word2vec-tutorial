# -*- coding: utf-8 -*-

from gensim.models import word2vec
from gensim import models
import logging
import io
import sys

""" http://stackoverflow.com/questions/35596031/gensim-word2vec-find-number-of-words-in-vocabulary
The vocabulary is in the vocab field of the Word2Vec model's wv property, as a dictionary, with the keys being each token (word). So it's just the usual Python for getting a dictionary's length:

len(w2v_model.wv.vocab)
(In older gensim versions before 0.13, vocab appeared directly on the model. So you would use w2v_model.vocab instead of w2v_model.wv.vocab.)
"""
import jieba.posseg as pseg

def get_postag(sent):
    result = pseg.cut(sent)
    for word, flag in result:
        yield flag

def get_word_tag(wd):
   try:
       return pseg.dt.word_tag_tab.get(wd, 'x')
       # word, _, tag = line.split(" ")
   except Exception as e:
       logging.info(repr(e))
       return 'x'

	

def main():
      logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
      model = models.Word2Vec.load('vectors.bin')
      sent="今天台北的天空很藍"
      for wd, tag in pseg.cut(sent) :
        print(u",".join([wd, tag, get_word_tag(wd)]))

      #exit()
      i=0
      #xxx model.sort_vocab()
      vocab=model.wv.vocab
      destfname="mydict.txt"
      print("write to %s starting" %(destfname) )      
      x1k=[]
      with io.open(destfname, 'w', encoding='utf-8') as f:
        for wd in vocab:
	    #print(wd,vocab[wd].index , unicode(vocab[wd]))
           x = u" ".join([wd,  unicode(vocab[wd].count) , get_word_tag(wd)])
           x1k.append(x)
	   if i%10000==0 :
             print(i, vocab[wd].index, vocab[wd].count)
             logging.info(x) 
             f.write( u"\n".join(x1k))
             x1k=[]
           i +=1
             
               
      print("write to %s finished" %(destfname) )


if __name__ == "__main__":
   main()
