import sys
import json

from workspace import Workspace
from config import Config
from video.detector import VideoDetector
from video.ffmpeg import FFmpeg
from ai.factory import UpscalerFactory
from common.logger import Logger


def main():

    logger = Logger.get()

    if len(sys.argv) != 2:
        print("Uso:")
        print("python process.py <video>")
        sys.exit(1)

    video = sys.argv[1]

    config = Config(
        input_file=video,
        output_file="salida.mkv"
    )

    detector = VideoDetector()
    info = detector.analyze(config.input_file)
    workspace = Workspace(info)
    print(info)

    ffmpeg = FFmpeg()
    frames = ffmpeg.extract_frames(info, workspace.frames)
    print(frames)

    audio = ffmpeg.extract_audio(
        info,
        workspace.audio / "audio.flac"
    )
    print(audio)

    upscaler = UpscalerFactory.create(config.model)

    upscaler.load()



if __name__ == "__main__":
    main()    