# Installation

The instructions below assume that Caffe has already been installed. If not, please refer to installation instructions at [](http://val.serc.iisc.ernet.in/expresso/installation.html) 

If Caffe has been installed, add the following environmental variables to your .bashrc (or whatever shell you happen to be using)

`CAFFE_ROOT` : Location of Caffe''s root directory (E.g. `/home/username/caffe`)

`EXPRESSO_ROOT` : Full path location of Expresso''s root directory (E.g. `/home/username/Projects/expresso`)

`HTTP_PROXY` : If you need/use a HTTP proxy, enter the proxy string here (without quotes)

Type the following on the command line:
    source ~/.bashrc

To begin installation, type the following on command line:
    sh install.sh


To check if the installation is successful, first type the following on the command-line:
    echo $EXPRESSO_ROOT
    echo $CAFFE_ROOT

and verify that they are correct. Having done so, type
    sh run_expresso.sh

This should display Expresso''s main screen.

If you encounter problems during installation, in addition to the web, you can browse the [Expresso user forums] (https://groups.google.com/forum/#!forum/expresso-users) to post and obtain community assistance.
