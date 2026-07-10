FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

LABEL maintainer="Andres"
LABEL description="Video AI Upscaler"

ARG REAL_ESRGAN_VERSION=v0.2.0

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    ffmpeg \
    wget \
    unzip \
    curl \
    git \
    ca-certificates \
    libvulkan1 \
    vulkan-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN wget -q \
https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan/releases/download/${REAL_ESRGAN_VERSION}/realesrgan-ncnn-vulkan-${REAL_ESRGAN_VERSION}-ubuntu.zip \
-O realesrgan.zip \
 && unzip realesrgan.zip \
 && mv realesrgan-ncnn-vulkan-v0.2.0-ubuntu realesrgan \
 && rm realesrgan.zip

ENV PATH="/opt/realesrgan:$PATH"

WORKDIR /app

CMD ["bash"]

