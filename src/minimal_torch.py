import torch

print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"Number of GPUs: {torch.cuda.device_count()}")

for i in range(torch.cuda.device_count()):
    print(f"  GPU {i}: {torch.cuda.get_device_name(i)}")
    print(f"    Memory: {torch.cuda.get_device_properties(i).total_memory / 1e9:.1f} GB")



"""
Example output on a machine with one GPU:

PyTorch version: 2.6.0+cu124
CUDA available: True
Number of GPUs: 1
  GPU 0: NVIDIA A100 80GB PCIe
    Memory: 80.0 GB
"""