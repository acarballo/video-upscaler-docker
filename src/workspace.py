from pathlib import Path


class Workspace:

    def __init__(self, info):

        self.input_video = Path(info.filename)

        self.root = Path("cache") / self.input_video.stem

        self.frames = self.root / "frames"
        self.audio = self.root / "audio"
        self.upscaled = self.root / "upscaled"
        self.encode = self.root / "encode"
        self.output = self.root / "output"
        self.temp = self.root / "temp"

        self._create_directories()

    def _create_directories(self):

        self.frames.mkdir(parents=True, exist_ok=True)
        self.audio.mkdir(parents=True, exist_ok=True)
        self.upscaled.mkdir(parents=True, exist_ok=True)
        self.encode.mkdir(parents=True, exist_ok=True)
        self.output.mkdir(parents=True, exist_ok=True)
        self.temp.mkdir(parents=True, exist_ok=True)

    @property
    def audio_file(self):
        return self.audio / "audio.mp3"

    @property
    def output_video(self):
        return self.output / "salida.mkv"

    @property
    def frame_pattern(self):
        return self.frames / "frame_%08d.png"

    @property
    def upscaled_pattern(self):
        return self.upscaled / "frame_%08d.png"