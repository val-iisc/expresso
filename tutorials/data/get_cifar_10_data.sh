
# Download CIFAR-10 data (python format) from CIFAR-10 website (http://www.cs.toronto.edu/~kriz/cifar.html)
if [ ! -f cifar-10-python.tar.gz ]
then
	wget http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
	# Unpack
	tar -xvzf cifar-10-python.tar.gz

	# Run python script to preprocess CIFAR-10 data
	python preprocess_cifar_10.py
fi
