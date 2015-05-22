sudo apt-get install python-protobuf
sudo apt-get install python-numpy
sudo apt-get install python-scipy
sudo apt-get install python-h5py 

sudo apt-get install python-qt4
sudo apt-get install pyqt4-dev-tools
sudo apt-get install libqt4-dev
sudo apt-get install python-h5py

if [ -n "$HTTP_PROXY" ]; then
echo Proxy is $HTTP_PROXY
sudo pip install --proxy $HTTP_PROXY pyqtgraph
sudo pip install --proxy $HTTP_PROXY qtutils 
else
echo No proxy
sudo pip install pyqtgraph
sudo pip install qtutils 
fi
