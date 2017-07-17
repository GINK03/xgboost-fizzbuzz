import os
import sys
import math
import random
import pickle
def makePureData():
  w = open('pureData.txt', 'w')
  ii = [i for i in range(99999)]
  random.shuffle(ii)
  for i in ii:
    if i%15 == 0:
      a = '%d FizzBuzz'%i
    elif i%3 == 0:
      a = '%d Fizz'%i
    elif i%5 == 0:
      a = '%d Buzz'%i
    else:
      a = '%d そのまま'%i
    w.write('%s\n'%a)

def mapToFeatsIndex():
  f = open('pureData.txt')

  feat_index = {}
  for line in f: 
    line = line.strip()
    feats, ans = line.split()
    for e, char in enumerate( reversed(feats) ):
      uniq = 'digit:%d, char:%s'%(e, char)
      if feat_index.get( uniq ) is None:
        feat_index[uniq] = len( feat_index )
  open('feat_index.pkl', 'wb').write( pickle.dumps( feat_index ) )

def makeSVMFormat():
  f = open('pureData.txt')

  feat_index = pickle.loads( open('feat_index.pkl', 'rb').read() )
  ans_index  = {'FizzBuzz':0, 'Fizz':1, 'Buzz':2, 'そのまま':3}  
  svm_train = open('svm.fmt.train', 'w')
  svm_test  = open('svm.fmt.test', 'w')
  for line in f: 
    line = line.strip()
    feats, ans = line.split()
    feats_buff = []
    for e, char in enumerate( reversed(feats) ):
      uniq = 'digit:%d, char:%s'%(e, char)
      feats_buff.append( feat_index[uniq] )
    txt = ' '.join( ['%d:1.0'%f for f in feats_buff] )
    ans = ans_index[ans]
    if random.random() < 0.8:
      svm_train.write( '{} {}\n'.format(ans, txt) )
    else:
      svm_test.write( '{} {}\n'.format(ans, txt) )

if __name__ == '__main__':
  if '--step1' in sys.argv:
    makePureData()

  if '--step2' in sys.argv:
    mapToFeatsIndex()

  if '--step3' in sys.argv:
    makeSVMFormat()
