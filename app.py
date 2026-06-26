import streamlit as st
import os
from openai import AsyncOpenAI
import asyncio

# Setup Client
client = AsyncOpenAI(api_key=os.environ.get("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1")

st.title(" Marketing Copy Generator")

# Sidebar for Hyper-parameters
st.sidebar.header("Inference Parameters")
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
top_p = st.sidebar.slider("Top_P", 0.0, 1.0, 1.0)

# User Inputs
product_name = st.text_input("Product Name", "Smart Coffee Maker")
platform = st.selectbox("Platform", ["LinkedIn", "Instagram", "Email"])
tone = st.selectbox("Tone", ["Professional", "Witty", "Persuasive", "Casual"])

if st.button("Generate Copy"):
    with st.spinner('Generating...'):
        prompt = f"Act as a copywriter. Write a {platform} post for {product_name} with a {tone} tone."
        
        # Async execution within the GUI
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        async def call_api():
            return await client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=temperature,
                top_p=top_p
            )
        
        response = loop.run_until_complete(call_api())
        st.success("Done!")
        st.text_area("Generated Copy", response.choices[0].message.content, height=200)