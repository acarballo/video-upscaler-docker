from ai.realesrgan import RealESRGAN
from ai.aurasr import AuraSRUpscaler
# from ai.basicvsr import BasicVSR


class UpscalerFactory:

    @staticmethod
    def create(name):

        if name == "realesrgan":
            return RealESRGAN()

        if name == "aurasr":
            return AuraSRUpscaler()

        # if name == "basicvsr":
        #     return BasicVSR()

        raise Exception(f"Modelo desconocido: {name}")