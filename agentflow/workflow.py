from typing import List, Dict, Any, Union
from pydantic import BaseModel, Field

from .agent import Agent

class WorkflowStep(BaseModel):
    agent: Agent
    prompt: str
    # Add more complex step attributes like 'condition', 'output_parser', etc. if needed

class Workflow(BaseModel):
    name: str
    steps: List[WorkflowStep]
    # Add a state management or context passing mechanism here for complex workflows

    def run(self, initial_context: Any = None) -> Any:
        current_context = initial_context
        print(f"\n--- Starting Workflow: {self.name} ---")

        for i, step_data in enumerate(self.steps):
            agent = step_data.agent
            prompt = step_data.prompt

            # In a real system, the prompt for subsequent steps would often 
            # incorporate the output/context from previous steps.
            if current_context:
                step_prompt = f"{prompt} (Previous context: {current_context})"
            else:
                step_prompt = prompt

            print(f"\n--- Workflow Step {i+1}: Agent '{agent.name}' ---")
            step_output = agent.invoke(step_prompt)
            current_context = step_output # Update context for next step
            print(f"--- Step {i+1} Output: {step_output[:100]}... ---")

        print(f"\n--- Workflow: {self.name} Completed ---")
        return current_context
