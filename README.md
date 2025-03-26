# Cold Mail Generator

## Overview
The **Cold Mail Generator** is a Python-based tool designed to automatically generate cold emails for business development purposes. By providing job descriptions and relevant links, this tool crafts personalized and professional cold emails to potential clients, helping businesses reach out with tailored offerings.The idea is inspired from Codebasics and this is an updated version of that project

## Features
- Generate cold emails for business development purposes.
- Utilize job descriptions and links to showcase relevant portfolios.
- Powered by AI-based language models for personalized and effective messaging.

## Requirements
- Python 3.7+
- Install the necessary Python libraries via the `requirements.txt` file:
  - `Streamlit 1.44.0`
  - `bs4` (for web scraping)
  - `langchain	0.3.21`
  - `langchain-community	0.3.20`	
  - `langchain-core	0.3.48`	
  - `langchain-groq	0.3.1`

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cold-mail-generator.git
    cd cold-mail-generator
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and provide the required environment variables:
    ```
    GROQ_API_KEY=your_GROQ_api_key
    ```

4. Configure the cold mail generation settings and job descriptions as needed.

## Usage

To use the Cold Mail Generator, follow these steps:

1. **Prepare Your Input Data**:
   - **Job Description**: A detailed description of the job posting you're targeting.
   - **Relevant Links**: Links to your portfolio, case studies, or anything relevant to the business you're contacting.
   
2. **Run the Generator**:
   Use the following command to run the cold mail generation:

   ```bash
    streamlit run main.py
