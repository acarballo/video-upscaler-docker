from pathlib import Path
import shutil

class Workspace:

    def __init__(self, info):

        self.input_video = Path(info.filename)

        self.root = Path("cache") / self.input_video.stem

        self.frames = self.root / "frames"
        self.upscaled = self.root / "upscaled"

        self.audio = self.root / "audio"
        self.encode = self.root / "encode"

        self.output = self.root / "output"
        self.temp = self.root / "temp"

        self._create_directories()

    def _create_directories(self):

        self.frames.mkdir(parents=True, exist_ok=True)
        self.upscaled.mkdir(parents=True, exist_ok=True)

        self.audio.mkdir(parents=True, exist_ok=True)
        self.encode.mkdir(parents=True, exist_ok=True)

        self.output.mkdir(parents=True, exist_ok=True)
        self.temp.mkdir(parents=True, exist_ok=True)

    # ==================================================
    # Audio
    # ==================================================

    def audio_track(self, index):

        return self.audio / f"audio_{index:02d}.mp3"

    # ==================================================
    # Frames originales
    # ==================================================

    def frames_dir(self, block):

        path = self.frames / f"block_{block.index:06d}"
        path.mkdir(parents=True, exist_ok=True)

        return path

    def frame_pattern(self, block):

        return self.frames_dir(block) / "frame_%08d.png"

    # ==================================================
    # Frames reescalados
    # ==================================================

    def upscaled_dir(self, block):

        path = self.upscaled / f"block_{block.index:06d}"
        path.mkdir(parents=True, exist_ok=True)

        return path

    def upscaled_pattern(self, block):

        return self.upscaled_dir(block) / "frame_%08d.png"


    # ==================================================
    # Delete frames originales y Frames reescalados
    # ==================================================

    def clean_block(self, block):

        shutil.rmtree(
            self.frames_dir(block),
            ignore_errors=True
        )

        shutil.rmtree(
            self.upscaled_dir(block),
            ignore_errors=True
        )


    # ==================================================
    # Vídeos codificados por bloque
    # ==================================================

    def encoded_block(self, block):

        return self.encode / f"block_{block.index:06d}.mp4"

    def encoded_blocks(self):

        return sorted(
            self.encode.glob("block_*.mp4")
        )

    def existing_blocks(self):

        return sorted(
            self.encode.glob("block_*.mp4")
        )

    # ==================================================
    # Archivos temporales para concatenar
    # ==================================================

    @property
    def concat_list(self):

        return self.temp / "blocks.txt"

    @property
    def concatenated_video(self):

        return self.temp / "video.mp4"

    # ==================================================
    # Salida final
    # ==================================================

    @property
    def output_video(self):

        return self.output / "salida.mkv"