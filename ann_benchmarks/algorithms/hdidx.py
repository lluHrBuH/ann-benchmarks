from __future__ import absolute_import
import numpy
import hdidx
from ann_benchmarks.algorithms.base import BaseANN

class Hdidx(BaseANN):
    def __init__(self, nsubq):
        self.name = 'Hdidx(nsubq={})'.format(nsubq)
        self._nsubq = nsubq
        self._index = None
        print("Init done")

    def fit(self, X):
        X = numpy.array(X)	
        X = X.astype(numpy.float32)
        self._index = hdidx.indexer.IVFPQIndexer()
        self._index.build({'vals': X, 'nsubq': self._nsubq}) 
        self._index.add(X)
        print("Fit done")
    def query(self, v, n):
        v = v.astype(numpy.float32)
        print(v)
        print(n)
        print(self._index.search(v,n))
        print("-----------------------------------")
        print(self._index.search(v,n))

        return self._index.search(v,n)
    def use_threads(self):
        return False
      
