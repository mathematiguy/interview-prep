FROM nvidia/cuda:11.2.0-cudnn8-devel-ubuntu20.04

# Use New Zealand mirrors
RUN sed -i 's/archive/nz.archive/' /etc/apt/sources.list
RUN apt update

# Set timezone to Auckland
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y locales tzdata git
RUN locale-gen en_NZ.UTF-8
RUN dpkg-reconfigure locales
RUN echo "Pacific/Auckland" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
ENV LANG en_NZ.UTF-8
ENV LANGUAGE en_NZ:en

# Create user 'kaimahi' to create a home directory
RUN useradd kaimahi
RUN mkdir -p /home/kaimahi/
RUN chown -R kaimahi:kaimahi /home/kaimahi
ENV HOME /home/kaimahi

# Install apt packages
RUN apt update
RUN apt install -y awscli curl software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa

# Install python
ENV PYTHON_VERSION 3.9
RUN apt update
RUN apt install -y python${PYTHON_VERSION}-dev python${PYTHON_VERSION}-distutils
RUN rm /usr/bin/python3 && ln -s /usr/bin/python${PYTHON_VERSION} /usr/bin/python3
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python${PYTHON_VERSION}

# Install pip packages
RUN pip3 install --upgrade pip
COPY requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt

# Install jax
RUN pip3 install --upgrade "jax[cuda]" -f https://storage.googleapis.com/jax-releases/jax_releases.html
RUN pip3 install jax[cuda11_cudnn805] -f https://storage.googleapis.com/jax-releases/jax_releases.html
#RUN pip3 install jax[cuda11_cudnn82] -f https://storage.googleapis.com/jax-releases/jax_releases.html

# Download fasttext language detection model
RUN apt install wget
RUN wget https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz -P ${HOME}/.models

# Install nltk data
# Need this for the nltk.tokenizers package
ENV NLTK_DATA /nltk_data
RUN python3 -c "import nltk;nltk.download('punkt', download_dir='$NLTK_DATA')"
