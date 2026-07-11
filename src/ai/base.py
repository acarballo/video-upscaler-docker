from abc import ABC, abstractmethod


class BaseUpscaler(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def upscale(self, input_dir, output_dir):
        pass