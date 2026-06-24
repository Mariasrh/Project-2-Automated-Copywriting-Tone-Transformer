import tkinter as tk
from tkinter import scrolledtext
import csv
import asyncio
import httpx
import threading
import os

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-1.5-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

MASTER_TEMPLATE = "Rédige une copie marketing pour le produit : {product_name}. Plateforme : {platform}. Ton : {tone}. Contraintes : {constraints}"
PLATFORM_CONSTRAINTS = {
    "LinkedIn": "Professionnel, hashtags, 150-300 mots.",
    "Instagram": "Visuel, emojis, max 50 mots.",
    "Email": "Persuasif, objet accrocheur, structuré."
}

async def generate_copy(client, product_name, platform, tone):
    constraints = PLATFORM_CONSTRAINTS.get(platform, "Concis et engageant.")
    prompt = MASTER_TEMPLATE.format(product_name=product_name, platform=platform, tone=tone, constraints=constraints)

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        response = await client.post(API_URL, json=payload, timeout=30.0)
        
        if response.status_code == 200:
            data = response.json()
            text = data['candidates'][0]['content']['parts'][0]['text']
            return f"--- {product_name} ---\n{text}"
        else:
            return f"Error {response.status_code} for {product_name}: {response.text}"
    except Exception as e:
        return f"Error for {product_name}: {str(e)}"

async def process_csv(text_widget):
    if not os.path.exists('data.csv'):
        text_widget.insert(tk.END, "Error: data.csv file missing.\n")
        return

    async with httpx.AsyncClient() as client:
        with open('data.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            tasks = [generate_copy(client, row['Product_Name'], row['Platform'], row['Tone']) for row in reader]
            
            results = await asyncio.gather(*tasks)
            for output in results:
                text_widget.insert(tk.END, f"{output}\n{'-'*30}\n")
                text_widget.see(tk.END)

def run_async_loop(text_widget):
    asyncio.run(process_csv(text_widget))

def start_process():
    result_area.delete(1.0, tk.END)
    threading.Thread(target=run_async_loop, args=(result_area,), daemon=True).start()

#  GUI 
root = tk.Tk()
root.title("Marketing Tone Transformer")
root.geometry("500x600")

tk.Label(root, text="Batch Copy Generator", font=("Arial", 14, "bold")).pack(pady=10)
tk.Button(root, text="Start Processing", command=start_process, bg="#2196F3", fg="white").pack(pady=5)

result_area = scrolledtext.ScrolledText(root, width=60, height=25)
result_area.pack(pady=10)

root.mainloop()
