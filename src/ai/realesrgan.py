from ai.base import BaseUpscaler


class RealESRGANUpscaler(BaseUpscaler):

    def load(self):
        print("RealESRGAN cargado")

    def upscale(self, input_dir, output_dir):
        print("Aquí irá RealESRGAN")