from pathlib import Path


def create_directory(path: Path):

    path.mkdir(parents=True, exist_ok=True)


def clean_directory(path: Path):

    if not path.exists():
        return

    for f in path.iterdir():
        if f.is_file():
            f.unlink()