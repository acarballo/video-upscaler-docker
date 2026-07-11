from ai.realesrgan import RealESRGANUpscaler
from ai.basicvsr import BasicVSRUpscaler


class UpscalerFactory:

    @staticmethod
    def create(name):

        if name == "realesrgan":
            return RealESRGANUpscaler()

        if name == "basicvsr":
            return BasicVSRUpscaler()

        raise Exception(f"Modelo desconocido: {name}")