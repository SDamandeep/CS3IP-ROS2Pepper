# Use the official ROS2 humble base image
FROM osrf/ros:humble-desktop-full

# Install Ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections


RUN apt-get update && apt-get install -y \
    software-properties-common \
    && apt-add-repository universe \
    && apt-get update \
    && apt-get install -y \
    ubuntu-desktop \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Update package lists
RUN apt-get update

# Install X11 apps
RUN apt-get install -y x11-apps

# Install Python development tools and libraries
RUN apt-get install -y \
    python3-pip \
    libssl-dev \
    libffi-dev \
    libbz2-dev \
    libclang-dev

# Install miscellaneous tools
RUN apt-get install -y \
    cmake \
    wget \
    git \
    nano \
    vim \
    tmux \
    net-tools

RUN pip install \ 
    zeroc-ice \
    ice \
    pygame \
    pillow


# Install ROS2 packages
RUN apt-get update && apt-get install -y \
    ros-humble-ros-base \
    python3-colcon-common-extensions

# Source ROS2 setup script
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

#COPY ICEP /

RUN apt update
RUN apt -y upgrade

RUN apt-get install -y curl python2.7-dev
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py && \
    python2.7 get-pip.py
RUN pip2.7 install zeroc-ice

RUN apt update


# Set the XDG_RUNTIME_DIR environment variable
ENV XDG_RUNTIME_DIR=/tmp/runtime-dir

# Create the directory and change its permissions
RUN mkdir $XDG_RUNTIME_DIR && \
    chmod 0700 $XDG_RUNTIME_DIR


# Clean up APT cache to reduce image size
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#Installing NAOqi drivers
RUN mkdir /naoqi
WORKDIR /naoqi
COPY naoqiSDK/naoqi-sdk-2.5.5.5-linux64.tar.gz /naoqi
COPY naoqiSDK/pynaoqi-python2.7-2.5.5.5-linux64.tar.gz /naoqi/
RUN tar xzf naoqi-sdk-2.5.5.5-linux64.tar.gz
RUN tar xzf pynaoqi-python2.7-2.5.5.5-linux64.tar.gz
ENV PYTHONPATH=${PYTHONPATH}:/naoqi/pynaoqi-python2.7-2.5.5.5-linux64/lib/python2.7/site-packages
#RUN echo 'export DYLD_LIBRARY_PATH=${DYLD_LIBRARY_PATH}:naoqi/pynaoqi-python2.7-2.5.5.5-linux64'

RUN apt update
RUN apt -y upgrade

# RUN apt-get install -y ros-kinetic-nao-robot

#Retun back to the home directory
WORKDIR /
#Create a ROS2 workspace and import the code
RUN mkdir -p /ros2pepper/src
WORKDIR /ros2pepper/
RUN rosdep install -i --from-path src --rosdistro humble -y
RUN colcon build
COPY /PepperCode /ros2pepper/src/
WORKDIR /src/codeBridge/ICE/

# Set up entry point
CMD ["bash"]

# Set the display environment variable
ENV DISPLAY=0
ENV QT_X11_NO_MITSHM=1


#############################  Build command  #############################
#sudo docker build -t pepperros2 --build-arg DISPLAY=$DISPLAY  .

#############################  Run command  #############################
#sudo docker run -v /path/to:/ros2pepper/src/ -it --rm --privileged --gpus all --name pepperros2 --network host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix pepperros2

#############################  Command to open a new terminal  #############################
#sudo docker exec -it --privileged pepperros2 /bin/bash

# xhost +local: sudo apt install python3-pip

############################# ROS2 Commands ###############################

# ros2 topic pub /move_topic std_msgs/String "data: '0.2,0.0,0.2'"

# ros2 topic pub /image_topic std_msgs/msg/String "data: 'image'"

# ros2 topic pub /rightarm_topic std_msgs/msg/String "data: '1.0,0.0,0.0,0.0'"

# ros2 topic pub /leftarm_topic std_msgs/msg/String "data: '1.0,0.0,0.0,0.0'"
