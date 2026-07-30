# 🚀 AirLLM Memory Streaming Demo

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red?style=for-the-badge&logo=pytorch)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge)
![AirLLM](https://img.shields.io/badge/AirLLM-Streaming-success?style=for-the-badge)
![GPU](https://img.shields.io/badge/RTX-3050%206GB-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</p>

---

# 📖 Overview

This repository demonstrates how **AirLLM** enables inference of Large Language Models that are significantly larger than the available GPU memory.

Instead of loading an entire model into VRAM, AirLLM:

- Stores model layers on disk
- Loads one layer at a time
- Performs computation
- Frees GPU memory
- Streams the next layer

This allows models like **Qwen3-32B** to run on a laptop equipped with only **6GB VRAM**.

---

# 💻 Test Machine

| Component | Specification |
|------------|---------------|
| Laptop | Acer ALG (2025) |
| CPU | Intel Core i5-13420H |
| RAM | 16 GB DDR5 |
| GPU | NVIDIA RTX 3050 Laptop (6GB VRAM) |
| Storage | 512GB SSD |
| OS | Windows 11 |
| Python | 3.11 |

---

# 🧠 Models Tested

| Model | Status |
|--------|--------|
| Llama-3.1-8B | ✅ Standard Transformers |
| Llama-3.1-8B (CPU) | ✅ |
| Qwen3-32B | ✅ AirLLM |
| Meta-Llama-3-70B | ❌ Disk Space Limitation |

---

# 📂 Repository Structure

```
.
│
├── baseline_gpu.py
├── baseline_cpu.py
├── run_airllm.py
├── memory_test.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<username>/airllm-memory-demo.git

cd airllm-memory-demo
```

Create virtual environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 HuggingFace Login

Some models require authentication.

```bash
huggingface-cli login
```

Paste your HuggingFace access token.

---

# ▶️ Running Standard Transformers

```bash
python baseline_gpu.py
```

or

```bash
python baseline_cpu.py
```

---

# ▶️ Running AirLLM

```python
from airllm import AutoModel

model = AutoModel.from_pretrained(
    "Qwen/Qwen3-32B"
)

output = model.generate(...)
```

Run

```bash
python run_airllm.py
```

---

# 🏗 AirLLM Workflow

```
                HuggingFace Hub
                        │
                        ▼
             Download Model Files
                        │
                        ▼
      Split into Individual Layer Files
                        │
                        ▼
          Store Layers on Local SSD
                        │
                        ▼
     ┌────────────────────────────────┐
     │ During Inference               │
     │                                │
     │ Load Layer 0 into VRAM         │
     │        │                       │
     │        ▼                       │
     │ Compute                        │
     │        │                       │
     │ Free VRAM                      │
     │        │                       │
     │ Load Layer 1                   │
     │        │                       │
     │ Repeat Until Final Layer       │
     └────────────────────────────────┘
                        │
                        ▼
               Generated Response
```

---

# 📦 Layer Storage

Example location on Windows

```
C:\Users\<User>\.cache\huggingface\hub\
```

Example

```
splitted_model/

model.embed_tokens.safetensors

model.layers.0.safetensors

model.layers.1.safetensors

...

model.layers.63.safetensors

model.norm.safetensors

lm_head.safetensors
```

Each file represents one neural network layer.

---

# 🧠 Memory Comparison

## Standard Transformers

```
SSD
 │
 ▼
Load Entire Model
 │
 ▼
GPU VRAM

Need enough VRAM for all weights.
```

---

## AirLLM

```
SSD
 │
 ▼
Layer 0 → GPU

Compute

Free Memory

Layer 1 → GPU

Compute

Free Memory

...

Repeat
```

Only one layer occupies VRAM at a time.

---

# 📊 Successful Run

Model

```
Qwen3-32B
```

Hardware

```
RTX 3050 Laptop GPU
6GB VRAM
16GB RAM
```

Output

```
What is the capital of United States?

The capital of the United States is Washington, D.C.
```

The model successfully generated text despite requiring far more memory than the available GPU VRAM.

---

# ❌ 70B Experiment

Attempted

```
Meta-Llama-3-70B
```

Result

```
Download completed

Layer reconstruction started

Disk storage exhausted

SafetensorError:
There is not enough space on the disk.
```

The failure was caused by insufficient SSD storage rather than GPU memory.

---

# 📚 What This Project Demonstrates

✅ Traditional model loading

✅ CPU inference

✅ GPU inference

✅ VRAM limitations

✅ AirLLM layer streaming

✅ HuggingFace cache structure

✅ Large model inference on consumer hardware

---

# 🙏 Acknowledgements

- AirLLM
- HuggingFace Transformers
- Meta AI
- Qwen Team
- PyTorch

---

# ⭐ If you found this useful...

Leave a ⭐ on the repository!

It helps others discover the project.