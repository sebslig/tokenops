# AgentFlow SDK

A Python SDK for orchestrating multi-step AI agent workflows with tool calling capabilities.

## Features

- Define agents with roles and tools.
- Create multi-step workflows with sequential or conditional logic.
- Integrate custom tools for agents to use.
- Simple, declarative API.

## Installation

```bash
pip install agentflow-sdk
```

## Quick Start

```python
from agentflow import Agent, Workflow, Tool

# Define a simple tool
def search_web(query: str):
    return f"Search results for: {query}"

search_tool = Tool(name="web_search", description="Searches the web for a query", func=search_web)

# Define agents
researcher = Agent(name="Researcher", role="Finds information online", tools=[search_tool])
analyzer = Agent(name="Analyzer", role="Analyzes research results")

# Define a workflow
workflow = Workflow(
    name="Research Workflow",
    steps=[
        {"agent": researcher, "prompt": "Research the latest AI trends."},
        {"agent": analyzer, "prompt": "Summarize the research results provided by the Researcher."}
    ]
)

# Execute the workflow
result = workflow.run()
print(result)
```

## Development

```bash
git clone https://github.com/yourusername/agentflow-sdk.git
cd agentflow-sdk
pip install -e .
```
