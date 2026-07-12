from aura_sr import AuraSR
import time

print("Import correcto")

print("Inicio:", time.strftime("%H:%M:%S"))

print("Llamando a from_pretrained()...")

model = AuraSR.from_pretrained()

print("Modelo cargado:", time.strftime("%H:%M:%S"))