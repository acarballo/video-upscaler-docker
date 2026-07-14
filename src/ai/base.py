from abc import ABC, abstractmethod
from pathlib import Path

class Upscaler(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def upscale_image(self, source: Path, destination: Path):
        pass

    def upscale_images(self, context, images):

        context.progress.start(
            total=len(images),
            title="Reescalando fotogramas..."
        )

        for source, destination in images:

            self.upscale_image(
                source,
                destination
            )

            context.progress.increment()

        context.progress.finish()