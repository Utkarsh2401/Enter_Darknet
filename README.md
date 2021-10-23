# Enter_Darknet

* [Darknet](#Darknet)

* [Setting Up Darknet In Linux](#Setup_Darknet)

* [CNN.cfg](#CNN)

* [ResNet_34.cfg](#ResNet34)

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

<a name = "CNN">

## CNN.cfg

#### CNN Model

![CNN Model](/Assets/CNN_Model.png "CNN Model Image")

#### Training Graph

![CNN Model Training Graph](/Assets/CNN_TrainingGraph.png "CNN Training Graph")

</a>

<a name = "ResNet34">

## Resnet_34.cfg

#### ResNet_34 Model

![ResNet34 Model](/Assets/ResNet_34_Model.png "ResNet34 Model Image")

#### Training Graph

![ResNet34 Training Graph](/Assets/ResNet_34_TrainingGraph.png "ResNet34 Training Graph")
  
</a>
