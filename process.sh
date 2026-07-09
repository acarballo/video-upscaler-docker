#!/bin/bash
set -e

INPUT="$1"

if [ -z "$INPUT" ]; then
    echo "Uso: process.sh <video>"
    exit 1
fi

if [ ! -f "$INPUT" ]; then
    echo "No existe el fichero: $INPUT"
    exit 1
fi

BASENAME=$(basename "$INPUT")
NAME="${BASENAME%.*}"
DIR=$(dirname "$INPUT")

mkdir -p /tmp/frames
mkdir -p /tmp/upscaled

echo "Extrayendo FPS..."

FPS=$(ffprobe -v error \
    -select_streams v:0 \
    -show_entries stream=r_frame_rate \
    -of default=noprint_wrappers=1:nokey=1 \
    "$INPUT")

echo "FPS: $FPS"

echo "Extrayendo audio..."

ffmpeg -y -i "$INPUT" -vn -acodec flac /tmp/audio.flac

echo "Extrayendo fotogramas..."

ffmpeg -y -i "$INPUT" /tmp/frames/frame_%08d.png

echo "Escalando con IA..."

cd /opt/Real-ESRGAN

python3 inference_realesrgan.py \
    -n RealESRGAN_x4plus \
    -i /tmp/frames \
    -o /tmp/upscaled

echo "Reconstruyendo vídeo..."

ffmpeg -y \
    -framerate "$FPS" \
    -i /tmp/upscaled/frame_%08d_out.png \
    -i /tmp/audio.flac \
    -c:v hevc_nvenc \
    -preset p5 \
    -cq 20 \
    -c:a copy \
    "$DIR/${NAME}_upscaled.mkv"

echo "Limpiando..."

rm -rf /tmp/frames
rm -rf /tmp/upscaled
rm -f /tmp/audio.flac

echo "Finalizado."