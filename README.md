# Enter_Darknet

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

