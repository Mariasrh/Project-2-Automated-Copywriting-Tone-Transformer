Automated Copywriting & Tone Transformer

This project is a dynamic orchestration engine designed to automate the generation of professional marketing copy. Developed as part of the DecodeLabs Generative AI Industrial Training Kit (**2026**), it enables users to transform raw product descriptions into platform-specific content (LinkedIn, Instagram, Email) by precisely tuning creative hyper-parameters like Temperature and Top_P.

### Key Features

Dynamic Template Compilation: Uses structured templates to inject user-defined variables (Product_Name, Platform, Tone) into prompts, ensuring consistent brand voice.

Interactive **GUI**: Built with Streamlit, providing an intuitive interface to control inference parameters and generate content in real-time.

Asynchronous Inference: Utilizes asyncio and the openai **SDK** to manage non-blocking **API** requests efficiently.

Parameter Control: Offers granular control over model creativity via adjustable sliders for Temperature and Top_P.

Scalable Pipeline: Designed to build scalable content pipelines through pure inference logic.

### Project Structure

app.py: The core Streamlit application providing the interactive user interface and asynchronous **API** orchestration.

requirements.txt: Project dependencies including streamlit, openai, httpx, and python-dotenv.

.gitignore: Ensures secure handling of environment variables (like **API** keys) and excludes temporary system files.

How to Run ## Prerequisites Ensure you have Python 3.10+ installed on your system.

## Installation

Install the required dependencies:

    ```Bash
    pip install -r requirements.txt

## Configuration

Create a file named `.env` in the root directory.

Add your Groq **API** key to the file:

    ```Bash
    GROQ_API_KEY=gsk_your_actual_key_here

## Execution

Launch the interactive web interface:

    ```Bash
    streamlit run app.py

This will open a local browser window where you can start generating copy.

### Key Skills Demonstrated

Dynamic Prompt Compilation: Managing variable injection for multi-platform output.

Inference Tuning: Mastering the balance between creativity and structure using **LLM** hyper-parameters.

Asynchronous Integration: Optimizing network I/O for efficient Generative AI applications.

Powered by DecodeLabs | **2026** Batch
