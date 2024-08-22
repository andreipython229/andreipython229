import psutil

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes: .2f}{unit}{suffix}"
        bytes /= factor

vmem = psutil.virtual_memory()

print(f"Всего: {get_size(vmem.total)}")
print(f"Доступно: {get_size(vmem.available)}")
print(f"Используется: {get_size(vmem.used)}")
print(f"Используется в процентах: {vmem.percent}%")
