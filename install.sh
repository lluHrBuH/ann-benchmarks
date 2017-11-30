apt-get update
apt-get install -y python-numpy python-scipy python-pip python-nose build-essential software-properties-common unzip

apt-get install -y libboost1.58-all-dev swig
apt-get autoremove -y


pip install setuptools wheel six pybind11
pip install scikit-learn pyyaml Cython

cd install
for fn in lib-*.sh
do
  sh $fn
done

#sh data-sift.sh

