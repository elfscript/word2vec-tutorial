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


def main():
      logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
      model = models.Word2Vec.load('vectors.bin')
      v1=model.wv[u'天空'] #has to input unicode u'xxx'
      #print(type(v1)) <type 'numpy.ndarray'>
      print(len(v1), v1[0:5], v1[-5:-1])
      print( u",".join(wv2syns(model.wv, u'天空', 5)) )
      i=0
      #xxx model.sort_vocab()
      vocab=model.wv.vocab
      destfname="wv2syns.txt"
      print("write synonyms to %s starting" %(destfname) )      
      x1k=[]
      with io.open(destfname, 'w', encoding='utf-8') as f:
        for wd in vocab:
	    #print(wd,vocab[wd].index , unicode(vocab[wd]))
           x = wd + ":" + u",".join(wv2syns(model.wv, wd, 5, 0.75))
           x1k.append(x)
	   if i%10000==0 :
             print(i, vocab[wd].index, vocab[wd].count)
             logging.info(x) 
             f.write(u'\n'.join(x1k))
             x1k=[]
           i +=1
             
               
      print("write synonyms to %s finished" %(destfname) )

#        x=wv2ant(model.wv, u'天空', 3, -0.2)
#        print(x)

def wv2syns(wv, wd, topn, th=0.65):
   try:
       # vs= wv.most_similar(positive=[wd],topn = topn) 
       tuples=wv.similar_by_word(wd, topn=topn)
       return [t[0] for t in tuples if t[1]>=th]
       #how to set threshold to filter out low-similarity words ?
       #say, to chosse only top 3 words haveing similarity > 0.9
 
   except Exception as e:
       #print("Unexpected error:", sys.exc_info()[0])
       logging.info("wv2syns exception %s", repr(e))
       return []

def wv2ant(wv, wd, topn, th=0.65):
   try:
       vs= wv.most_similar(negative=[wd],topn = topn)
       return [t for t in vs if t[1]>=th]

   except Exception as e:
       logging.info("wv2ant exception %s", repr(e))
       return []

if __name__ == "__main__":
   main()
