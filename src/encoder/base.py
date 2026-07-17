from abc import ABC, abstractmethod
from pathlib import Path


class Upscaler(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def upscale_image(self, source: Path, destination: Path):
        pass

    def upscale_images(
        self,
        frames,
        destination_dir,
        progress=None
    ):

        total = len(frames)

        for index, source in enumerate(frames, start=1):

            destination = destination_dir / source.name

            self.upscale_image(
                source,
                destination
            )

            if progress:
                progress.update(index)