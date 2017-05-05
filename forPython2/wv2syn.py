# -*- coding: utf-8 -*-

from gensim.models import word2vec
from gensim import models
import logging
import io
import sys

def main():
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	model = models.Word2Vec.load('med250.model.bin')
        v1=model.wv[u'天空'] #has to input unicode u'xxx'
	#print(type(v1)) <type 'numpy.ndarray'>
        print(len(v1), v1[0:5], v1[-5:-1])
        print( u",".join(wv2syn(model.wv, u'天空', 5)) )
        x=wv2ant(model.wv, u'天空', 3, -0.2)
        print(x)

def wv2syn(wv, wd, topn, th=0.65):
   try:
       vs= wv.most_similar(positive=[wd],topn = topn) 
       return [t[0] for t in vs if t[1]>=th]
       return u",".join(x)
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
