import time
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = "meta-llama/Llama-3.1-8B-Instruct"

print("=" * 60)
print("GPU:", torch.cuda.get_device_name(0))
print("VRAM:", round(torch.cuda.get_device_properties(0).total_memory / 1024**3, 2), "GB")
print("=" * 60)

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL)

print("Loading model...")
start = time.time()

model = AutoModelForCausalLM.from_pretrained(
    MODEL,
    torch_dtype=torch.float16,
    device_map="cuda"
)

load_time = time.time() - start

print(f"\nModel loaded in {load_time:.2f} seconds")

allocated = torch.cuda.memory_allocated() / 1024**3
reserved = torch.cuda.memory_reserved() / 1024**3

print(f"Allocated VRAM : {allocated:.2f} GB")
print(f"Reserved VRAM  : {reserved:.2f} GB")

prompt = "Explain Machine Learning like I'm 10 years old."

inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

print("\nGenerating...")

start = time.time()

output = model.generate(
    **inputs,
    max_new_tokens=150
)

generation_time = time.time() - start

print("\nGenerated Text:\n")
print(tokenizer.decode(output[0], skip_special_tokens=True))

print("\nGeneration Time:", round(generation_time, 2), "seconds")