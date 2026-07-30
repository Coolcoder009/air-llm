import time
import psutil
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = "meta-llama/Llama-3.1-8B-Instruct"

print("=" * 60)
print("Running on CPU")
print(f"CPU : {torch.get_num_threads()} Threads Available")
print(f"System RAM : {psutil.virtual_memory().total / 1024**3:.2f} GB")
print("=" * 60)

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL)

print("Loading model...")
start = time.time()

model = AutoModelForCausalLM.from_pretrained(
    MODEL,
    torch_dtype=torch.float32,   # CPU works best with float32
    device_map="cpu"
)


print(f"RSS : {mem.rss / 1024**3:.2f} GiB")
print(f"VMS : {mem.vms / 1024**3:.2f} GiB")
load_time = time.time() - start

print(f"\nModel loaded in {load_time:.2f} seconds")

print(f"RAM Used : {psutil.virtual_memory().used / 1024**3:.2f} GB")

prompt = "Capital of India is"

inputs = tokenizer(prompt, return_tensors="pt")

print("\nGenerating...")

start = time.time()

output = model.generate(
    **inputs,
    max_new_tokens=20
)

generation_time = time.time() - start

print("\nGenerated Text:\n")
print(tokenizer.decode(output[0], skip_special_tokens=True))

print(f"\nGeneration Time : {generation_time:.2f} sec")