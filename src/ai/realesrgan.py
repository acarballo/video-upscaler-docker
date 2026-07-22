from pathlib import Path

from PIL import Image

from ai.base import Upscaler

from realesrgan import RealESRGAN
import torch


class RealESRGANUpscaler(Upscaler):

    def __init__(self):

        self.model = None

    def load(self):

        if self.model is not None:
            return

        device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model = RealESRGAN(
            device,
            scale=4
        )

        self.model.load_weights(
            "weights/RealESRGAN_x4.pth"
        )

    def upscale_image(self, source: Path, destination: Path):

        image = Image.open(source).convert("RGB")

        result = self.model.predict(image)

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        result.save(destination)