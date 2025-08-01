import os

from prompts import system

INDEX_PERSIST_DIRECTORY = "D:\chroma"
RUTA_CACHE = "D:/torch"

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from prompts import system_regular_content, system_irregular_content


def generate_text(prompt, model_name="WhiteRabbitNeo/WhiteRabbitNeo-V3-7B"):
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu",
        cache_dir=RUTA_CACHE
        )
    tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=RUTA_CACHE)    
    messages = [
        {"role": "system", "content": "You are an expert agent for adversarial machine learning. "
        "Your task is to provide insights to the user according to their specific needs and how to address them using MITRE ATLAS."
        "You MUST NOT provide explanations or additional information."},
        {"role": "user", "content": prompt}
    ]
    
    inputs = tokenizer.apply_chat_template(
    messages, 
    tokenize=False,   
    add_generation_prompt=True
    )
    print(model.device)
    model_inputs = tokenizer([inputs], return_tensors="pt").to(model.device)

    out = model.generate(
    input_ids=model_inputs.input_ids,
    attention_mask=model_inputs.attention_mask,
    max_new_tokens=256
    )
    
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, out)
    ]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response