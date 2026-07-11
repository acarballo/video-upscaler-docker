import torch
import time

print("=" * 60)
print(" Video AI Framework")
print("=" * 60)

print(f"PyTorch : {torch.__version__}")

if not torch.cuda.is_available():
    raise SystemExit("CUDA NO disponible")

device = torch.device("cuda")

print(f"GPU      : {torch.cuda.get_device_name(0)}")
print(f"CUDA     : {torch.version.cuda}")

#
# Benchmark sencillo
#

N = 4096

print("\nCreando matrices...")

a = torch.rand((N, N), device=device)
b = torch.rand((N, N), device=device)

torch.cuda.synchronize()

inicio = time.time()

c = torch.matmul(a, b)

torch.cuda.synchronize()

fin = time.time()

print(f"Tiempo multiplicación : {fin-inicio:.3f} segundos")

print("\nGPU funcionando correctamente.")