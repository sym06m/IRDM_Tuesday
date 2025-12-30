class BasicAgent:
    def __init__(self, name):
        self.name = name

    def run(self, prompt):
        return f"[{self.name}] processed prompt: {prompt}"

if __name__ == "__main__":
    agent = BasicAgent("BasicADKAgent")
    result = agent.run("What is Agent Development Kit?")
    print(result)
