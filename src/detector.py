import json
import subprocess

from model.videoinfo import VideoInfo


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

        return self._parse(filename, data)


    def _parse(self, filename, data):

        video_stream = self._get_video_stream(data)
        audio_stream = self._get_audio_stream(data)

        return VideoInfo(
            filename=filename,
            width=int(video_stream["width"]),
            height=int(video_stream["height"]),
            fps=self._calculate_fps(video_stream),
            codec=video_stream["codec_name"],
            pixel_format=video_stream.get("pix_fmt", ""),
            has_audio=audio_stream is not None,
            audio_codec=audio_stream.get("codec_name") if audio_stream else None,
            audio_channels=audio_stream.get("channels") if audio_stream else None,
            sample_rate=int(audio_stream.get("sample_rate")) if audio_stream else None,
            duration=float(data["format"]["duration"]),
            bitrate=int(data["format"]["bit_rate"])
        )

    def _get_video_stream(self, data):

        for stream in data["streams"]:

            if stream["codec_type"] == "video":
                return stream

        raise RuntimeError("No se encontró ningún stream de vídeo")        

    def _get_audio_stream(self, data):

        for stream in data["streams"]:

            if stream["codec_type"] == "audio":
                return stream

        return None

    def _calculate_fps(self, stream):

        fps = stream.get("avg_frame_rate", "0/1")

        numerador, denominador = fps.split("/")

        numerador = float(numerador)
        denominador = float(denominador)

        if denominador == 0:
            return 0.0

        return numerador / denominador        