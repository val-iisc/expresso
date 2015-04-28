CAFFE_ROOT=/home/babu/caffe
EXPRESSO_ROOT=/home/babu/expresso
HTTP_PROXY=http://proxy.serc.iisc.in:3128

sudo apt-get install python-qt4
sudo apt-get install pyqt4-dev-tools
sudo apt-get install libqt4-dev
sudo apt-get install python-h5py

if [[ -n "$HTTP_PROXY" ]]; then
echo Proxy is $HTTP_PROXY
sudo pip install --proxy $HTTP_PROXY pyqtgraph
sudo pip install --proxy $HTTP_PROXY qtutils 
else
sudo pip install pyqtgraph
sudo pip install qtutils 
fi

python install.py $CAFFE_ROOT $EXPRESSO_ROOT
