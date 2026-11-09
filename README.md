# AI Programming Assistant

## Project Description

This project is a Python-based AI Programming Assistant that helps users understand programming concepts and answer questions about code.

The program connects to Google's Gemini AI through an API. Users can enter programming questions, and the assistant generates explanations and suggestions.

I created this project to practice working with Python, APIs, and artificial intelligence.

## Features

- Answers questions about programming languages such as C++, Java, and Python.
- Explains programming concepts and code.
- Helps users identify possible programming errors.
- Allows users to ask multiple questions.
- Handles empty inputs and basic API errors.

## Technologies Used

- Python
- Google Gemini API
- Google Gen AI Python SDK
- GitHub Codespaces

## How to Run

1. Open the project in GitHub Codespaces or another Python environment.
2. Install the required library:

   `python -m pip install google-genai`

3. Create an environment variable named `GEMINI_API_KEY` containing your own Gemini API key. In GitHub Codespaces, this can be configured using Codespaces Secrets.
4. Run the program:

   `python assistant.py`

5. Enter a programming question and press Enter. Type `exit` to close the program.

**Note:** The program requires an internet connection and a valid Gemini API key. API availability and usage limits depend on Google's service.

## What I Learned

Through this project, I learned how to connect a Python application to an AI model using an API. I also practiced handling user input, displaying generated responses, and managing errors when communicating with an external service.</Writing
