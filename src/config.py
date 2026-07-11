from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:

    input_file: Path

    output_file: Path

    work_dir: Path = Path("/work")

    cache_dir: Path = Path("/cache")

    scale: int = 4

    model: str = "realesrgan"

    codec: str = "hevc"

    crf: int = 20

    preset: str = "slow"

    tile_size: int = 512

    batch_size: int = 500