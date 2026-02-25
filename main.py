import datetime
import os

class Assistant:
    def __init__(self, name):
        self.name = name

    def greet(self):
        hour = datetime.datetime.now().hour
        greeting = "Good morning" if hour < 12 else "Good afternoon" if hour < 18 else "Good evening"
        return f"{greeting}! I am {self.name}, your AI study partner."

    def get_time(self):
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

    def add_task(self, task):
        with open("todo.txt", "a") as f:
            f.write(f"{task}\n")
        return f"Added '{task}' to your study list."

def main():
    bot = Assistant("Jarvis")
    print(bot.greet())
    
    while True:
        command = input("\nHow can I help? (type 'exit' to quit): ").lower()
        
        if "time" in command:
            print(bot.get_time())
        elif "add task" in command:
            task = input("What do you need to get done? ")
            print(bot.add_task(task))
        elif "exit" in command:
            print("Goodbye! Happy coding.")
            break
        else:
            print("I'm still learning. Try 'time' or 'add task'.")

if __name__ == "__main__":
    main()
