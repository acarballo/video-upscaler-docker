from abc import ABC, abstractmethod
from pathlib import Path
from tqdm import tqdm

class Upscaler(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def upscale_image(self, source: Path, destination: Path):
        pass

    def upscale_images(self, images):

        for source, destination in tqdm(images, desc="Upscaling"):

            self.upscale_image(
                source,
                destination
            )