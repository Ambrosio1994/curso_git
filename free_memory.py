def memory():
	"""Retorna o uso de memoria do computador"""    
	memory = psutil.virtual_memory()
	print(f"Uso de memória: {memory.percent}%")
	print(f"Memória total: {memory.total / 1024**3:.2f} GB")
	print(f"Memória disponível: {memory.available / 1024**3:.2f} GB")
	print(f"Memória usada: {memory.used / 1024**3:.2f} GB")

