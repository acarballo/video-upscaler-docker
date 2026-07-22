from ai.realesrgan import RealESRGANUpscaler
from ai.aurasr import AuraSRUpscaler
# from ai.basicvsr import BasicVSR


class UpscalerFactory:

    @staticmethod
    def create(name):

        if name == "realesrgan":
            return RealESRGANUpscaler()

        if name == "aurasr":
            return AuraSRUpscaler()

        # if name == "basicvsr":
        #     return BasicVSR()

        raise Exception(f"Modelo desconocido: {name}")