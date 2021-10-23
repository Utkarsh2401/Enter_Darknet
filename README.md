# Enter_Darknet

* [Darknet](#Darknet)

* [Setting Up Darknet In Linux](#Setup_Darknet)

* [Darknet tutorial Using Google Colab](#Colab)

* [CNN](#CNN_Model)

* [ResNet_34](#ResNet34)

## Darknet

<a name = "Darknet">

Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation. You can find the source on [GitHub](https://github.com/AlexeyAB/darknet).
  
![Darknet Logo](/Assets/Darknet_Logo.png "Darknet Logo")
  
</a>

<a name = "Setup_Darknet">
  
## Setting up Darknet in Linux

#### Prerequisites: 
Install python3 (it's preinstalled on ubuntu).

Install pip.

Install cmake using: <code>sudo pip install cmake</code>

#### Commands:
```
git clone https://github.com/AlexeyAB/darknet
cd darknet
mkdir build_release
cd build_release
```
##### Now if you are doing it via GPU (CUDA):
<code>cmake ..</code>

##### If it's via CPU:

Install openCV first using:
```
sudo apt update
sudo apt install libopencv-dev python3-opencv
```

Then <code>cmake ..-DENABLE_CUDA=OFF</code> 

And the final command is <code>make -j4</code>

</a>

<a name = "Colab">
  
## Darknet Tutorial Using Google Colab (And it's 12 RAM GPU runtime)
  
Our Complete Tutorial for how we trained a 34-layer Resnet Model using Colab is here:
[How to train a Classifier on Cifar-10 using Darknet on Colab notebook using a Resnet model's config file](https://colab.research.google.com/drive/1wzoCVvgglMtFPiXt-oA6SfqOqk7MCpmq) 
Following the tutorial, setting up and installation of darknet to acquiring the dataset and writing your own [config file](add link if we explain about config files) to train and test a model can be done in 7 simple steps, and use almost no resources of your native machine!

</a>

## Dataset

#### CIFAR-10

<a name = "CNN_Model">

## CNN
 
#### CNN Model

![CNN Model](/Assets/CNN_Model.png "CNN Model Image")

#### Training Graph

![CNN Model Training Graph](/Assets/CNN_TrainingGraph.png "CNN Training Graph")

</a>

<a name = "ResNet34">

## Resnet_34

#### ResNet_34 Model

![ResNet34 Model](/Assets/ResNet_34_Model.png "ResNet34 Model Image")

#### Training Graph

![ResNet34 Training Graph](/Assets/ResNet_34_TrainingGraph.png "ResNet34 Training Graph")
  
</a>
