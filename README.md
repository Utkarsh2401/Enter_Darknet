# Enter_Darknet

* [Darknet](#darknet)

* [Setting Up Darknet In Linux](#Setup_Darknet)

* [Darknet Tutorial Using Google Colab](#Colab)

* [Object Detection](#ObjDetect)

* [Dataset For Image Classification](#dataset)

* [CNN](#CNN_Model)

* [ResNet_34](#ResNet34)

* [Training The Model](#Train)

* [Predicting](#Predict)

* [File Structure Of Darknet](#File)

<a name = "darknet">

## Darknet

[Darknet](https://pjreddie.com/darknet/) is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation. You can find the source on [GitHub](https://github.com/AlexeyAB/darknet).
  
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
  
Follow [this](https://github.com/AlexeyAB/darknet#how-to-compile-on-linux-using-make).

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

<a name = "ObjDetect">

## Object Detection

Using the darknet library we detect objects in images as well as videos. The [simple_darknet_code.py](https://github.com/Utkarsh2401/Enter_Darknet/blob/dev/simple_darknet_code.py) does exactly that for images.

|       Original Image        |          Object Detection          |
|-----------------------------|------------------------------------|                                                              
|![Dog](/Assets/dog.jpg "Dog")|![Dog](/Assets/dog_output.png "Dog")|
  
</a>  

<a name = "dataset">
  
## Dataset For Image Classification

#### CIFAR-10
The [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

The dataset is divided into five training batches and one test batch, each with 10000 images. The test batch contains exactly 1000 randomly-selected images from each class. The training batches contain the remaining images in random order, but some training batches may contain more images from one class than another. Between them, the training batches contain exactly 5000 images from each class.

We will be using this dataset to train and test our models.

##### Downloading the dataset:

The python, MATLAB, and binary version can be downloaded from this [link](https://www.cs.toronto.edu/~kriz/cifar.html).

But since we are training through darknet, we will use a mirror of the dataset as we want the pictures in image format.
Follow instructions at this [link](https://pjreddie.com/darknet/train-cifar/) to do so.

Also make the cifar.data file in the cfg folder of the cloned darknet repository from the above, but since we will be using our own config files, we don't need the cifra_small.cfg file from the above link.
  
</a>  

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

<a name = "Train">

## Training The Model

After making the cfg files, we are ready to train our models now using the CIFAR-10 dataset!

#### For training with the CNN Model

```
cd darknet
./darknet classifier train cfg/cifar.data cfg/CNN.cfg
```

#### For training with the ResNet Model

```
cd darknet
./darknet classifier train cfg/cifar.data cfg/ResNet_34.cfg
```
  
</a>

<a name = "Predict">

## Predicting

After training, we get a .weights file which stores the weights of the model.
Using this file we will now predict outputs.

#### To predict using the CNN Model

```
./darknet classifier predict cfg/cifar.data cfg/CNN.cfg backup/CNN_final.weights
```

#### To predict using the ResNet Model

```
./darknet classifier predict cfg/cifar.data cfg/ResNet_34.cfg backup/ResNet_34_final.weights
```

</a> 
 
<a name = "File"> 
 
## File Structure Of Darknet

```
Darknet
├── build_release
|    └── libdarknet.so
|    
├── cfg
|    └── cifar.data           - this is the file we created for training and predicting our models using CIFAR dataset.
|    └── CNN.cfg              - CNN model cfg file.
|    └── coco.data        
|    └── coco.names
|    └── ResNet_34.cfg        - ResNet34 model cfg file.
|    └── yolov4.cfg           - YOLO v4 cfg file.
|    
├── data
|    └── cifar                - after downloading cifar this folder is created.
|         └── test            - this folder contains images for testing our models.
|         └── train           - this folder contains images for training our models.
|         └── labels.txt      - this file contains the labels for image classification.
|         └── test.list       - this file contains paths to the images in the test folder.
|         └── train.list      - this file contains paths to the images in the train folder.
|        
├── darknet                   - darknet executable (made after doing make)
|
├── darknet.py                - python wrapper for darknet.
|
├── darknet_images.py         - python code for object detection in images.
|
├── darknet_video.py          - python code for object detection in videos.
|
├── Makefile                  - special file, containing shell commands. While in the directory containing this makefile, you will type make and the commands in the Makefile will be executed.
|
├── yolov4.weights            - downloaded wieghts for training with YOLOv4.
```
</a>
