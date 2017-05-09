# -*- coding: utf-8 -*-

from gensim.models import word2vec
from gensim import models
import logging
import io
import sys

import jieba.posseg as pseg
words = pseg.cut("我爱北京天安门")
for word, flag in words:
   print('%s %s' % (word, flag))

#exit()
def zhPar2Sents(fname):
  sents=[]
  with io.open(fname, 'r', encoding='utf8') as f:
     for line in f:
        sents.extend(line.split(u'。'))

  return sents
_wv=[]

def main():
      global _wv
      logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
      model = models.Word2Vec.load('vectors.bin')
      _wv=model.wv
      sents = zhPar2Sents('sample2.txt')
      sents=[s for s in sents if len(s.strip()) > 2 ]
      s0=sents[0]
      L=len(sents)
      print("number of effective sentences", L)
      #for s1, s2 in zip(sents[0:L-1], sents[1:L]) :
      #    print(sentSim(s1,s2)) 
      x=(0, 0.0)
      for i, s in  enumerate(sents[0:L]) :  
        print(s) 
        if i==0  : continue
        tmp=sentSim(s0,s)
        print("similarity:", tmp)
        if tmp > x[1] :
             x=(i,tmp)
      print(x)
      print(s0)
      print(sents[x[0]])

def sent2words(s):
   try:
       return pseg.cut(s) #[(wd,flag), ...]    
   except Exception as e:
       logging.info("sent2words exception %s", repr(e))
       return []

def wdlistSim(list1, list2):
   global _wv
   try:
     if len(list1) == 0 : return 0.0
     if len(list2) == 0 : return 0.0
     x=0.0
     for w1 in list1:
        for w2 in list2:
           tmp=_wv.similarity(w1,w2)
	   if tmp<0 : tmp=-tmp
           if tmp > x : 
              x=tmp
     return x    
   except KeyError as ke:
       return 0.0
   except Exception as e:
       logging.info(sys._getframe().f_code.co_name +" exception %s", repr(e))
       return 0.0


def sentSim(s1,s2, th=0.65):
   try:
      ns1=[wd   for wd, postag in sent2words(s1)    if postag=='ns' ]
      n1=[wd   for wd, postag in sent2words(s1)    if postag=='n' ]
      v1=[wd   for wd, postag in sent2words(s1)    if postag=='v' ]
      ns2=[wd   for wd, postag in sent2words(s2)    if postag=='ns' ]
      n2=[wd   for wd, postag in sent2words(s2)    if postag=='n' ]
      v2=[wd   for wd, postag in sent2words(s2)    if postag=='v' ]
      print(u",".join(n1))
      print(u",".join(n2))
#      print(u",".join(v1))
#      print(u",".join(v2))
#
      x=wdlistSim(ns1, ns2)
      x += wdlistSim(n1, n2)
      x += wdlistSim(v1, v2)

      return x/3
 
   except Exception as e:
      logging.info(sys._getframe().f_code.co_name +" exception %s", repr(e))
      return 0.0


if __name__ == "__main__":
   main()
