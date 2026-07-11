from ai.base import BaseUpscaler


class BasicVSRUpscaler(BaseUpscaler):

    def load(self):
        print("BasicVSR cargado")

    def upscale(self, input_dir, output_dir):
        print("Aquí irá BasicVSR")