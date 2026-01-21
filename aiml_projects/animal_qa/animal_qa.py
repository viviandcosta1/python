import aiml
import os
import time
import sys

# Monkey-patch time.clock for Python 3.8+ compatibility
if not hasattr(time, 'clock'):
    time.clock = time.perf_counter

class AnimalQASystem:
    def __init__(self):
        """Initialize the Animal Q&A system"""
        self.kernel = aiml.Kernel()
        
        # Get the directory where this script is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        aiml_file = os.path.join(current_dir, 'animals.aiml')
        
        if os.path.exists(aiml_file):
            print(f"Loading AIML file: {aiml_file}")
            self.kernel.learn(aiml_file)
            print("Animal Knowledge Base loaded successfully!")
        else:
            print(f"Error: AIML file not found at {aiml_file}")

    def ask_question(self, question):
        """Get answer to a question"""
        response = self.kernel.respond(question)
        return response

    def start_qa_session(self):
        """Start an interactive Q&A session"""
        print("\n" + "="*60)
        print("🦁 Animal Knowledge Base Q&A System 🦁")
        print("="*60)
        print("Ask me questions about animals!")
        print("Type 'HELP' for commands or 'QUIT' to exit\n")
        
        while True:
            try:
                question = input("Your Question: ").strip()
                
                if question.upper() == 'QUIT':
                    print("\nThank you for learning about animals! Goodbye!")
                    break
                
                if not question:
                    continue
                
                answer = self.ask_question(question)
                print(f"\nAnswer: {answer}\n")
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break

def main():
    # Initialize the Animal Q&A system
    qa_system = AnimalQASystem()
    
    # Start interactive Q&A session
    qa_system.start_qa_session()

if __name__ == "__main__":
    main()
