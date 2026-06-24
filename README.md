# Automated Copywriting & Tone Transformer
This project is powered by DecodeLabs as part of the 2026 Generative AI Industrial Training Kit.

This project is a dynamic orchestration engine designed to automate the generation of professional marketing copy. It leverages generative AI to transform raw product descriptions into platform-specific content (LinkedIn, Instagram, Email) by precisely tuning creative hyper-parameters like Temperature and Top_P.

## Key Features
* **Dynamic Template Compilation:** Uses Python f-strings to inject user variables (Product_Name, Platform, Tone) into master instruction templates.
* **Asynchronous Execution:** Utilizes `httpx` and `asyncio` to manage high-volume API requests efficiently, reducing total wall-clock time by overlapping network waiting periods.
* **Parameter Control:** Programmatically adjusts model creativity and response length via Temperature and token limits.
* **Scalable Pipeline:** Designed to build scalable content pipelines through pure inference logic, ensuring brand voice protection through structural prompt enforcement.

## Project Structure
* `main.py`: The core orchestration engine and asynchronous loop implementation.
* `data.csv`: Input source for batch processing of metadata (Product, Target Tone, Platform Variables).
* `requirements.txt`: Project dependencies including `httpx` for non-blocking I/O.
* `.gitignore`: Ensures secure handling of environment variables (like API keys) and temporary system files

## How to Run

### 1. Prerequisites
Ensure you have Python 3.10+ installed.

### 2. Installation
Install the required asynchronous dependencies:
    ```bash
     pip install -r requirements.txt

### 3. Configuration
Set up your environment variables to securely store your API keys. 

> **Note:** Do not hardcode your keys directly into the script. Use a `.env` file instead.

### 4. Execution
Prepare your `data.csv` with the required columns (`Product_Name`, `Platform`, `Tone`) and run the orchestration engine:

```bash
python main.py
