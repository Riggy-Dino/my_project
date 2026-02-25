import os
from google import genai

# Configuration - Paste your key here or set it as an environment variable
os.getenv("GEMINI_API_KEY")
#GEMINI_API_KEY = ""
client = genai.Client(api_key=GEMINI_API_KEY)

class SmartAssistant:
    def __init__(self, name="Jarvis"):
        self.name = name

    def ask_ai(self, prompt):
        try:
            # Using the latest gemini-3-flash model
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error connecting to AI: {e}"

def main():
    bot = SmartAssistant()
    print(f"--- {bot.name} is now online (AI Powered) ---")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["exit", "quit"]:
            break
            
        # The AI processing step
        print(f"\n{bot.name}: Thinking...")
        answer = bot.ask_ai(user_input)
        print(f"\n{bot.name}: {answer}")

if __name__ == "__main__":
    main()
