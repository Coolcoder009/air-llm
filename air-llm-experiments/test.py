# import torch

# print(torch.cuda.is_available())
# print(torch.version.cuda)
# True
# 12.8


# import torch

# print(torch.cuda.get_device_name(0))
# print(torch.cuda.get_device_properties(0).total_memory / 1024**3)
# NVIDIA GeForce RTX 3050 6GB Laptop GPU
# 5.99951171875


# import psutil

# vm = psutil.virtual_memory()

# print(f"Total     : {vm.total / 1024**3:.2f} GB")
# print(f"Available : {vm.available / 1024**3:.2f} GB")
# print(f"Used      : {vm.used / 1024**3:.2f} GB")
# print(f"Percent   : {vm.percent}%")

# import psutil

# vm = psutil.virtual_memory()
# swap = psutil.swap_memory()

# print(f"RAM Used      : {vm.used/1024**3:.2f} GB")
# print(f"RAM Available : {vm.available/1024**3:.2f} GB")
# print(f"Swap Used     : {swap.used/1024**3:.2f} GB")
# print(f"Swap Total    : {swap.total/1024**3:.2f} GB")