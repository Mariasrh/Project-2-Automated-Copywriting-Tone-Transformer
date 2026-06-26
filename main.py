import os
import asyncio
from openai import AsyncOpenAI

# Initialize client (Groq is OpenAI-compatible)
client = AsyncOpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Template Engine: Separates prompt structure from logic
PROMPT_TEMPLATES = {
    "LinkedIn": "Act as a professional B2B marketer. Write a LinkedIn post for {product_name}. Tone: {tone}. Use professional, industry-focused language.",
    "Instagram": "Act as a lifestyle influencer. Write an Instagram caption for {product_name}. Tone: {tone}. Use engaging, fun language with emojis and hashtags.",
    "Email": "Act as a direct-response copywriter. Write a sales email for {product_name}. Tone: {tone}. Focus on benefits and a strong call-to-action."
}

async def generate_copy(product_name, platform, tone, temp, top_p):
    # Dynamic Compilation
    prompt = PROMPT_TEMPLATES.get(platform).format(
        product_name=product_name,
        tone=tone
    )
    
    # Inference Tuning
    response = await client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        temperature=temp,
        top_p=top_p
    )
    
    return f"--- {platform} ---\n{response.choices[0].message.content}"

async def main():
    # User Input Simulation
    requests = [
        {"product": "Eco-Friendly Water Bottle", "platform": "LinkedIn", "tone": "Formal", "temp": 0.2, "top_p": 0.9},
        {"product": "Eco-Friendly Water Bottle", "platform": "Instagram", "tone": "Energetic", "temp": 0.9, "top_p": 1.0}
    ]
    
    tasks = [generate_copy(r["product"], r["platform"], r["tone"], r["temp"], r["top_p"]) for r in requests]
    
    # Concurrency Management: Executing requests in parallel
    results = await asyncio.gather(*tasks)
    
    for res in results:
        print(res + "\n")

if __name__ == "__main__":
    asyncio.run(main())