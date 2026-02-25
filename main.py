import os
from google import genai

# Setup
GEMINI_API_KEY = "AIzaSyAI5o_eaRQGLAv3i5jFaIxfI6O5tVYtk_Q"
client = genai.Client(api_key=GEMINI_API_KEY)

class SmartAssistant:
    def __init__(self):
        # We define the "personality" of the tutor here
        self.tutor_instruction = (
            "You are an expert Computer Science Tutor. When a user asks about code, "
            "don't just give the answer. Explain the 'why', mention time complexity (Big O), "
            "and suggest best practices. Be concise but insightful."
        )

    def ask_tutor(self, user_query):
        try:
            # We pass the system instruction along with the user prompt
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=f"{self.tutor_instruction}\n\nUser Question: {user_query}"
            )
            return response.text
        except Exception as e:
            return f"Error: {e}"

def main():
    bot = SmartAssistant()
    print("--- CS Coding Tutor Mode Active ---")
    print("Type 'exit' to quit. Ask me anything about Python, DSA, or SQL!")
    
    while True:
        prompt = input("\nStudent: ")
        if prompt.lower() in ["exit", "quit"]:
            break
            
        print("\nTutor: Analyzing...")
        result = bot.ask_tutor(prompt)
        print(f"\nTutor: {result}")

if __name__ == "__main__":
    main()
