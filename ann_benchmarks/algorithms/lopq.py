from __future__ import absolute_import
import numpy
from lopq import LOPQModel, LOPQSearcher
from ann_benchmarks.algorithms.base import BaseANN

class LOPQ(BaseANN):
    def __init__(self, v):
        m = 4
        self.name = 'LOPQ(v={}, m={})'.format(v,m)
        self._m = m
        self._model = LOPQModel(V=v, M=m)
        self._searcher = None
        print("Init done")

    def fit(self, X):
        X = numpy.array(X)	
        X = X.astype(numpy.float32)
        self._model.fit(X)       
        self._searcher = LOPQSearcher(self._model)
        self._searcher.add_data(X)
        print("Fit done")

    def query(self, v, n):
        v = v.astype(numpy.float32)
        print(v)
        print(n)
        print("-----------------------------------")
        nns = searcher.search(x, quota=100)
        return nns
    def use_threads(self):
        return True
      
