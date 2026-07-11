from encoder.base import BaseEncoder


class X265Encoder(BaseEncoder):

    def encode(self):
        print("Codificando con x265")