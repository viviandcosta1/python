import aiml
import os
import time
import sys

# Monkey-patch time.clock for Python 3.8+ compatibility
if not hasattr(time, 'clock'):
    time.clock = time.perf_counter

class AIMLChatbot:
    def __init__(self):
        """Initialize the AIML kernel and load AIML files"""
        self.kernel = aiml.Kernel()
        
        # Get the directory where this script is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        aiml_file = os.path.join(current_dir, 'startup.aiml')
        
        if os.path.exists(aiml_file):
            print(f"Loading AIML file: {aiml_file}")
            self.kernel.learn(aiml_file)
            print("AIML model loaded successfully!")
        else:
            print(f"Error: AIML file not found at {aiml_file}")

    def chat(self, user_input):
        """Get response from AIML model"""
        response = self.kernel.respond(user_input)
        return response

    def start_conversation(self):
        """Start an interactive conversation with the chatbot"""
        print("\n" + "="*50)
        print("Welcome to PyBot - AIML Chatbot")
        print("="*50)
        print("Type 'HELP' for commands or 'QUIT' to exit\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.upper() == 'QUIT':
                    print("Bot: Goodbye! Thanks for chatting!")
                    break
                
                if not user_input:
                    continue
                
                response = self.chat(user_input)
                print(f"Bot: {response}\n")
                
            except KeyboardInterrupt:
                print("\nBot: Goodbye!")
                break

def main():
    # Initialize the chatbot
    chatbot = AIMLChatbot()
    
    # Start interactive conversation
    chatbot.start_conversation()

if __name__ == "__main__":
    main()
