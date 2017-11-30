FROM nvidia/cuda:8.0-devel-ubuntu16.04
LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

RUN echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list

ENV CUDNN_VERSION 7.0.4.31
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

RUN apt-get update && apt-get install -y --no-install-recommends \
            libcudnn7=$CUDNN_VERSION-1+cuda8.0 \
            libcudnn7-dev=$CUDNN_VERSION-1+cuda8.0 && \
    rm -rf /var/lib/apt/lists/*

RUN	apt-get update -y && apt-get install -y ruby git python-pip python-dev build-essential wget python-tk python-opencv
RUN pip install matplotlib Cython
ADD	. ann-benchmarks
WORKDIR	ann-benchmarks
RUN git config --global user.email "ann-benchmarks@ann-benchmarks.com"
RUN git config --global user.name "ANN Benchmarks"
RUN mkdir queries/
RUN	bash install.sh
RUN bash install/lib-flann.sh