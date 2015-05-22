# Run data preprocessing script
cd ../data
sh get_cifar_10_data.sh
cp cifar_10/cifar_10_train.hdf5 cifar_t1.hdf5
cd ../tutorial_1
