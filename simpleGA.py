# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 20:42:41 2016

@author: R16
"""

import numpy as np

def initpop(type_,nPop,nGen,nInt=0):
  
  if type_ == 'binary':
    
    return np.random.randint(2,size=(nPop,nGen))
    
  elif type == 'real' :
    
    return np.random.rand(nPop,nGen)
    
  elif type == 'integer':
    
    return np.random.randint(nInt,size=(nPop,nGen))
    
def decode(c,type_,ub,lb,lim):
  x=0
  y=0
  
  if type_ == 'binary':
    
    x = lb+((ub-lb)/np.sum(np.exp2(np.arange(1,lim+1)/-1)))*np.sum(c[0:lim]*np.exp2(np.arange(1,lim+1)/-1))
    
    y = lb+((ub-lb)/np.sum(np.exp2(np.arange(1,lim+1)/-1)))*np.sum(c[lim:]*np.exp2(np.arange(1,lim+1)/-1))
    
  elif type_ == 'integer':
    
    x = lb+((ub-lb)/np.sum(9*np.power(np.arange(1,lim+1)/-1,10)))*np.sum(c[0:lim]*np.power(np.arange(1,lim+1)/-1,10))

    y = lb+((ub-lb)/np.sum(9*np.power(np.arange(1,lim+1)/-1,10)))*np.sum(c[lim:]*np.power(np.arange(1,lim+1)/-1,10))
  else :
    x = c[:lim]
    
    y= c[lim:]
  
  return x,y
    
    
def evalfitness(pop,type_):
  fx='x**2+y**2'
  fit=np.array([])
  x=0
  y=0
  if type_ == 'maximize' :
    for c in pop:
      x,y = decode(c,type_)
      fitc = eval(fx)
      fit = np.append(fit,fitc)
  else:
    for c in pop:
      x,y = decode(c,type_)
      fitc = 1/eval(fx)
      fit = np.append(fit,fitc)
      
    
    return fit

def mutation(pM,type_,chromosome,nInt=0):
  
  if type_ == 'binary':
   
   for gen in chromosome:
     if np.random.rand()<=pM:
       gen = 1 if gen == 0 else 0
       
  elif type_ == 'real':
    
    for gen in chromosome:
      if np.random.rand()<=pM:
        gen = gen+np.random.uniform(-1,1)
      
  elif type_ == 'integer':
    
    for gen in chromosome:
      if np.random.rand()<=pM:
        gen = np.random.randint(nInt)
      
def parentSel():
  
  #soon 
  
def runGA(nPop,nGen,type_):
  
  #soon

       