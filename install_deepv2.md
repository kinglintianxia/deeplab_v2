# Install deeplab_v2 

#1 clone codes
* git clone https://github.com/xmojiao/deeplab_v2.git

#2 config
* see kinglintianxia/caffe_learning/Install_caffe.md
* tx2: 
1. Makefile.config
  > LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/`aarch64`-linux-gnu /usr/lib/`aarch64`-linux-gnu/hdf5/serial
2. Makefile
  > LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_serial_hl hdf5_serial `matio`	

#3 build error see
1. https://blog.csdn.net/tianrolin/article/details/71246472
2. https://blog.csdn.net/ruotianxia/article/details/78331964

# nyud dataset see
1. https://blog.csdn.net/xmo_jiao/article/details/78012504
