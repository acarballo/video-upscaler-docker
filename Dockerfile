# ======================================================
# Video AI Upscaler
# CUDA + PyTorch + Real-ESRGAN
# ======================================================

FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

#--------------------------------------------------------
# Dependencias del sistema
#--------------------------------------------------------
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    wget \
    unzip \
    ffmpeg \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

#--------------------------------------------------------
# Actualizar pip
#--------------------------------------------------------
RUN python3 -m pip install --upgrade pip setuptools wheel

#--------------------------------------------------------
# PyTorch con CUDA 11.8
#--------------------------------------------------------
RUN pip3 install --no-cache-dir \
    torch \
    torchvision \
    torchaudio \
    --index-url https://download.pytorch.org/whl/cu118

#--------------------------------------------------------
# Clonar Real-ESRGAN
#--------------------------------------------------------
WORKDIR /opt

RUN git clone https://github.com/xinntao/Real-ESRGAN.git

WORKDIR /opt/Real-ESRGAN

#--------------------------------------------------------
# Dependencias Python
#--------------------------------------------------------
RUN pip install --no-cache-dir -r requirements.txt

RUN python3 setup.py develop

#--------------------------------------------------------
# Descargar modelo x4
#--------------------------------------------------------
RUN mkdir -p weights && \
    wget -O weights/RealESRGAN_x4plus.pth \
https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth

#--------------------------------------------------------
# Directorio de trabajo
#--------------------------------------------------------
WORKDIR /app

COPY process.sh .

RUN chmod +x process.sh

ENTRYPOINT ["/app/process.sh"]