
import os
from google import genai

# Connect to Gemini using the API key
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

print("Welcome to the AI Programming Assistant!")
print("Ask me questions about C++, Java, Python, or other programming topics.")
print("Type 'exit' to quit.")

while True:
    question = input("\nYour question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if not question.strip():
        print("Please enter a question.")
        continue

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=question,
            config={
                "system_instruction": (
                    "You are a helpful AI programming tutor. "
                    "Help users understand programming concepts, "
                    "explain code, and identify programming errors. "
                    "Keep explanations clear and easy to understand."
                )
            }
        )

        print("\nAI Assistant:")
        print(response.text if response.text else "No response was generated.")

    except Exception as error:
        print("\nAn error occurred:", error)
