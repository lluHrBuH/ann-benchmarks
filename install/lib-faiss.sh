#!/bin/sh
cd "$(dirname "$0")"
. ./_ins_utilities.sh

ins_deb_require libopenblas-dev &&
  ins_git_get https://github.com/facebookresearch/faiss.git &&
  cp example_makefiles/makefile.inc.Linux makefile.inc &&
  make -j4 py BLASLDFLAGS=/usr/lib/libopenblas.so.0&&
  cd gpu&&
  make -j4 -e BLASLDFLAGS=/usr/lib/libopenblas.so.0 CXXFLAGS+="-std=gnu++11 -msse -msse4.1 -fPIC"  CFLAGS+="-std=gnu++11 -msse -msse4.1 -fPIC"&&
  make -j4 py -e BLASLDFLAGS=/usr/lib/libopenblas.so.0 CXXFLAGS+="-std=gnu++11 -msse -msse4.1 -fPIC"  CFLAGS+="-std=gnu++11 -msse -msse4.1 -fPIC"


