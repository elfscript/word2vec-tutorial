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
	model = models.Word2Vec.load('med250.model.bin')
        v1=model.wv[u'天空'] #has to input unicode u'xxx'
	#print(type(v1)) <type 'numpy.ndarray'>
        print(len(v1), v1[0:5], v1[-5:-1])
        print( u",".join(wv2syn(model.wv, u'天空', 5)) )
        i=0
        for wd in model.wv.vocab:
	    print(wd)
            i +=1
            if i >3 :
               break
             
               


        x=wv2ant(model.wv, u'天空', 3, -0.2)
        print(x)

def wv2syn(wv, wd, topn, th=0.65):
   try:
       # vs= wv.most_similar(positive=[wd],topn = topn) 
       vs=wv.similar_by_word(wd, topn=topn)
       return [t[0] for t in vs if t[1]>=th]
       #how to set threshold to filter out low-similarity words ?
       #say, to chosse only top 3 words haveing similarity > 0.9
 
   except Exception as e:
       #print("Unexpected error:", sys.exc_info()[0])
       logging.info("wv2syn exception %s", repr(e))
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
