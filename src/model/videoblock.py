from dataclasses import dataclass


@dataclass
class VideoBlock:

    index: int

    first_frame: int

    frame_count: int