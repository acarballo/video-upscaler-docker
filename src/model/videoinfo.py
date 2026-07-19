from dataclasses import dataclass


@dataclass
class VideoInfo:

    filename: str

    # Vídeo
    width: int
    height: int
    fps: float
    total_frames: int
    codec: str
    pixel_format: str

    # Audio
    has_audio: bool
    audio_codec: str | None
    audio_channels: int |None
    sample_rate: int | None

    # General
    duration: float
    bitrate: int

    def __str__(self):

        return f"""
Archivo
-------
{self.filename}

Vídeo
------
Resolución : {self.width}x{self.height}
FPS        : {self.fps:.3f}
Codec      : {self.codec}
Formato    : {self.pixel_format}

Audio
------
Presente   : {self.has_audio}
Codec      : {self.audio_codec}
Canales    : {self.audio_channels}
Frecuencia : {self.sample_rate}

General
-------
Duración   : {self.duration:.2f} segundos
Bitrate    : {self.bitrate:,} bps
"""
