FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

LABEL maintainer="Andres"
LABEL description="Video AI Framework"

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    git \
    wget \
    curl \
    unzip \
    ffmpeg \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip

#
# PyTorch CUDA 11.8
#
RUN pip install \
    torch \
    torchvision \
    torchaudio \
    --index-url https://download.pytorch.org/whl/cu118

#
# Librerías comunes
#
RUN pip install \
    numpy \
    opencv-python-headless \
    pillow \
    tqdm \
    einops \
    imageio \
    imageio-ffmpeg \
    scipy \
    basicsr \
    facexlib \
    gfpgan \
    realesrgan

RUN pip install aura-sr

WORKDIR /app

# COPY test_gpu.py .

# CMD ["python3","test_gpu.py"]
CMD ["bash"]