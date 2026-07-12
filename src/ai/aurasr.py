from pathlib import Path

from PIL import Image
from aura_sr import AuraSR

from ai.base import Upscaler


class AuraSRUpscaler(Upscaler):

    def __init__(self):
        self.model = None

    def load(self):

        if self.model is None:
            self.model = AuraSR.from_pretrained("fal/AuraSR-v2")

    def upscale_image(self, source: Path, destination: Path):

        image = Image.open(source)

        result = self.model.upscale_4x(image)

        destination.parent.mkdir(parents=True, exist_ok=True)

        result.save(destination)