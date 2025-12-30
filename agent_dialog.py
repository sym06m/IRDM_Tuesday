class DialogAgent:
    def chat(self):
        print("Agent started. Type 'exit' to stop.")
        while True:
            user_input = input("User: ")
            if user_input.lower() == "exit":
                print("Agent stopped.")
                break
            print("Agent:", user_input.upper())

if __name__ == "__main__":
    DialogAgent().chat()
