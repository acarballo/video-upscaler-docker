import json
import subprocess

from ffprobe.parser import FFProbeParser


class VideoDetector:

    def analyze(self, filename):

        cmd = [
            "ffprobe",
            "-v",
            "quiet",
            "-print_format",
            "json",
            "-show_streams",
            "-show_format",
            filename
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )

        data = json.loads(result.stdout)

        return FFProbeParser().parse(filename, data)