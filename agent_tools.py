def search_tool(query):
    return f"Search result for '{query}': ADK is a framework for building AI agents."

class ToolAgent:
    def run(self, prompt):
        if "search" in prompt.lower():
            return search_tool(prompt)
        return "No tool used."

if __name__ == "__main__":
    agent = ToolAgent()
    print(agent.run("search ADK framework"))
