from __future__ import absolute_import
import numpy
from n2 import HnswIndex
from ann_benchmarks.algorithms.base import BaseANN

class N2(BaseANN):
    def __init__(self, m):
        threads = 8
        self.name = 'N2(m={}, threads={})'.format(m,threads)
        self._m = m
        self._threads = threads
        self._index = None
        print("Init done")

    def fit(self, X):
        X = numpy.array(X)	
        X = X.astype(numpy.float32)
        self._index = HnswIndex(X.shape[1],"L2")
        print("Shape", X.shape[1])
        for el in X:
            self._index.add_data(el) 
        self._index.build(m=self._m, n_threads=self._threads)
        print("Fit done")

    def query(self, v, n):
        v = v.astype(numpy.float32)
        print(v)
        print(n)
        print("-----------------------------------")
        nns = self._index.search_by_vector(v,n)
        #print("[search_by_vector]: Nearest neighborhoods of vector {}: {}".format(v, nns))
        return nns
    def use_threads(self):
        return False
      
