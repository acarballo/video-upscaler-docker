import subprocess
from pathlib import Path

from ai.base import Upscaler


class RealESRGAN(Upscaler):

    def load(self):
        print("RealESRGAN cargado")

    def upscale_image(self, source: Path, destination: Path):

        subprocess.run(
            [
                "realesrgan-ncnn-vulkan",

                "-i",
                str(source),

                "-o",
                str(destination),

                "-n",
                "realesrgan-x4plus"
            ],
            check=True
        )