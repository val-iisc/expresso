# Download Caffenet model from BVLC's website
if [ ! -f bvlc_reference_caffenet.caffemodel ]
then
	wget http://dl.caffe.berkeleyvision.org/bvlc_reference_caffenet.caffemodel
	wget http://dl.caffe.berkeleyvision.org/caffe_ilsvrc12.tar.gz
	tar -xf caffe_ilsvrc12.tar.gz && rm -f caffe_ilsvrc12.tar.gz
fi

# Converts binaryproto to npy format
python ../../tools/protoToNpy/prototonpy.py imagenet_mean.binaryproto imagenet_mean.npy
