from dataclasses import dataclass, field
from pathlib import Path

from config import Config
from common.progress import Progress

from model.videoinfo import VideoInfo
from workspace import Workspace


@dataclass
class PipelineContext:

    config: Config

    progress: Progress = field(default_factory=Progress)

    video_info: VideoInfo | None = None

    workspace: Workspace | None = None

    frames: list[Path] = field(default_factory=list)

    audio_file: Path | None = None

    encoded_video: Path | None = None

    output_video: Path | None = None

    upscaler = None    