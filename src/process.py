import sys
import json

from config import Config
from detector import VideoDetector
from ffmpeg import FFmpeg
from ai.factory import UpscalerFactory


def main():

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

    # print(json.dumps(info, indent=4))
    print(info)

    ffmpeg = FFmpeg()

    upscaler = UpscalerFactory.create(config.model)

    upscaler.load()



if __name__ == "__main__":
    main()    