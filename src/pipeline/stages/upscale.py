from pipeline.stages.base import Stage

from ai.factory import UpscalerFactory


class UpscaleStage(Stage):

    def __init__(self, model):

        self.upscaler = UpscalerFactory.create(model)

    def run(self, context):

        context.progress.step("Inicializando AuraSR...")

        self.upscaler.load()

        context.progress.info("AuraSR cargado correctamente.")

        images = []

        for frame in context.frames:

            images.append((
                frame,
                context.workspace.upscaled / frame.name
            ))

        context.progress.step(
            f"Reescalando {len(images)} fotograma(s)..."
        )

        self.upscaler.upscale_images(images)

        context.progress.info("Reescalado finalizado.")