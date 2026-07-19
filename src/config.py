from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Config:

    input_file: Path

    output_file: Path

    work_dir: Path = Path("/work")

    cache_dir: Path = Path("/cache")

    # Escalado
    scale: int = 4
    model: str = "aurasr"

    # Codificación
    codec: str = "hevc"
    crf: int = 20
    preset: str = "slow"

    # IA
    tile_size: int = 512
    batch_size: int = 500

    # Procesamiento por bloques
    block_size: int = 500

    from_block: int = 0

    block_count: int | None = None

    cleanup_blocks: bool = True

    # Limitar el número de fotogramas (pruebas)
    max_frames: int | None = None

    # Pistas de audio adicionales
    additional_audio_sources: list[Path] = field(default_factory=list)