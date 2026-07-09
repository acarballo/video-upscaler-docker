## Construcción

```bash
docker compose build
docker build -t video-upscaler .
```

## Uso

```bash
docker compose run upscaler pelicula.avi

MSYS_NO_PATHCONV=1 docker run --rm --gpus all \
-v /d/Peliculas/procesar:/videos \
video-upscaler \
"/videos/Los informaticos 1x01.avi"


```