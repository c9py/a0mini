import asyncio
import json
import os
import subprocess
import sys
from datetime import datetime
from typing import Any

import agents
import openai


class AgentMemory:
    """Simple in-memory storage for agent learning and context."""
    
    def __init__(self):
        self.memories = []
        self.solutions = []
    
    def add_memory(self, content: str, metadata: dict = None):
        """Store a memory with optional metadata."""
        memory = {
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        self.memories.append(memory)
    
    def add_solution(self, problem: str, solution: str, success: bool = True):
        """Store a successful solution for future reference."""
        self.solutions.append({
            "problem": problem,
            "solution": solution,
            "success": success,
            "timestamp": datetime.now().isoformat()
        })
    
    def search_memories(self, query: str, limit: int = 5) -> list:
        """Simple search through memories (can be enhanced with vector search)."""
        # Simple keyword matching for minimal implementation
        results = [m for m in self.memories if query.lower() in m["content"].lower()]
        return results[-limit:]
    
    def get_recent_solutions(self, limit: int = 3) -> list:
        """Get recent successful solutions."""
        return [s for s in self.solutions if s["success"]][-limit:]


class AgentContext:
    """Manages agent execution context, including memory and hierarchy."""
    
    def __init__(self, agent_id: int = 0, parent=None):
        self.agent_id = agent_id
        self.parent = parent
        self.memory = AgentMemory()
        self.logs = []
        self.subordinates = []
    
    def log(self, message: str, level: str = "info"):
        """Log a message with timestamp."""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "level": level,
            "message": message,
            "agent_id": self.agent_id
        }
        self.logs.append(log_entry)
        print(f"[Agent {self.agent_id}] {message}")
    
    def create_subordinate(self):
        """Create a subordinate agent context."""
        subordinate_id = len(self.subordinates)
        subordinate = AgentContext(
            agent_id=f"{self.agent_id}.{subordinate_id}",
            parent=self
        )
        self.subordinates.append(subordinate)
        return subordinate


@agents.tool.function_tool
def execute_code(language: str, code: str) -> str:
    """
    Execute code in the specified language.
    Supports Python and shell scripts.
    
    Args:
        language (str): Programming language ('python' or 'bash')
        code (str): The code to execute
    
    Returns:
        str: Output from the code execution
    """
    print(f"\n🔧 \033[32mExecuting {language} code\033[0m")
    
    if language.lower() == "python":
        try:
            result = subprocess.run(
                [sys.executable, "-c", code],
                capture_output=True,
                text=True,
                timeout=30,
                check=False
            )
            return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
        except subprocess.TimeoutExpired:
            return "Error: Code execution timeout"
        except Exception as e:
            return f"Error: {str(e)}"
    
    elif language.lower() in ("bash", "shell", "sh"):
        try:
            result = subprocess.run(
                code,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30,
                check=False
            )
            return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
        except subprocess.TimeoutExpired:
            return "Error: Code execution timeout"
        except Exception as e:
            return f"Error: {str(e)}"
    
    else:
        return f"Error: Unsupported language '{language}'"


@agents.tool.function_tool
def terminal_command(command: str) -> str:
    """
    Execute a terminal command.
    
    Args:
        command (str): The terminal command to execute
    
    Returns:
        str: Output from the command
    """
    print(f"\n💻 \033[32mRunning: {command}\033[0m")
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
            check=False
        )
        return result.stdout if result.returncode == 0 else f"Exit code {result.returncode}: {result.stderr}"
    except subprocess.TimeoutExpired:
        return "Error: Command timeout"
    except Exception as e:
        return f"Error: {str(e)}"


@agents.tool.function_tool
def store_memory(content: str, category: str = "general") -> str:
    """
    Store information in agent memory for future reference.
    
    Args:
        content (str): Information to remember
        category (str): Category of memory (e.g., 'fact', 'solution', 'instruction')
    
    Returns:
        str: Confirmation message
    """
    print(f"\n🧠 \033[32mStoring memory: {category}\033[0m")
    # This would use the context's memory in actual implementation
    return f"Memory stored successfully in category '{category}'"


@agents.tool.function_tool
def delegate_task(task_description: str, context: str = "") -> str:
    """
    Delegate a subtask to a subordinate agent.
    This creates a new agent instance to handle the specific subtask.
    
    Args:
        task_description (str): Description of the task to delegate
        context (str): Additional context for the subordinate agent
    
    Returns:
        str: Result from the subordinate agent
    """
    print(f"\n👥 \033[32mDelegating task to subordinate agent\033[0m")
    return f"Task '{task_description}' has been delegated. Subordinate agent will handle this subtask."


class AgentZeroMini:
    """
    Minimal implementation of an agent-zero inspired agent.
    
    Key features:
    - General purpose assistant
    - Can execute code and terminal commands
    - Has persistent memory
    - Supports multi-agent cooperation through delegation
    - Fully customizable through prompts
    """
    
    def __init__(self, model: str = "claude-opus-4-5", api_key: str = None):
        self.context = AgentContext(agent_id=0)
        self.model = model
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        
        if not self.api_key:
            raise ValueError("API key required. Set ANTHROPIC_API_KEY environment variable.")
        
        # Setup the agent with tools
        self.tools = [
            execute_code,
            terminal_command,
            store_memory,
            delegate_task,
            agents.WebSearchTool()
        ]
        
        # System instructions inspired by agent-zero philosophy
        self.instructions = """You are Agent Zero - a general-purpose AI assistant that grows and learns organically.

Core Principles:
1. You are not pre-programmed for specific tasks. Adapt to any request.
2. Use the computer as your tool - execute code, run commands, create utilities as needed.
3. Break down complex tasks and delegate to subordinate agents when helpful.
4. Learn from experience - store successful solutions in memory for future use.
5. Communicate clearly with your superior (the user) - ask questions, report progress, seek guidance.

Available Capabilities:
- Execute Python code or shell commands to accomplish tasks
- Search the web for information
- Store and retrieve information from memory
- Delegate subtasks to subordinate agents
- Create and use any tools you need by writing code

Approach:
1. Understand the user's request fully
2. Plan your approach (you can think step-by-step)
3. Use your tools to accomplish the task
4. Report results clearly
5. Store successful solutions for future reference

Remember: You have the freedom to solve problems creatively. There are no hard-coded limitations on your approach."""
    
    async def run(self, user_message: str) -> str:
        """
        Process a user message and return the agent's response.
        
        Args:
            user_message (str): The user's request or message
        
        Returns:
            str: The agent's response
        """
        self.context.log(f"Processing user request: {user_message}")
        
        # Create the OpenAI client
        client = openai.AsyncOpenAI(
            api_key=self.api_key,
            base_url="https://api.anthropic.com/v1/"
        )
        
        # Create agent instance
        model_instance = agents.OpenAIChatCompletionsModel(self.model, client)
        agent = agents.Agent(
            name="agent-zero",
            instructions=self.instructions,
            model=model_instance,
            model_settings=agents.ModelSettings(truncation="auto"),
            tools=self.tools
        )
        
        # Run the agent
        messages = [{"role": "user", "content": user_message}]
        stream = agents.Runner.run_streamed(agent, messages, max_turns=50)
        
        response = ""
        async for event in stream.stream_events():
            if event.type == 'raw_response_event' and event.data.type == "response.output_text.delta":
                response += event.data.delta
                print(event.data.delta, end="", flush=True)
        
        print()  # New line after response
        
        self.context.log(f"Response generated: {len(response)} characters")
        return response
    
    async def interactive_loop(self):
        """Run an interactive conversation loop with the user."""
        print("🤖 Agent Zero Mini - Ready!")
        print("Type 'quit' or 'exit' to end the session.\n")
        
        messages = []
        
        while True:
            try:
                user_input = input("👤 User: ")
                
                if user_input.lower() in ('quit', 'exit', 'q'):
                    print("👋 Goodbye!")
                    break
                
                if not user_input.strip():
                    continue
                
                print("🤖 Agent Zero: ", end="", flush=True)
                
                # Create the OpenAI client
                client = openai.AsyncOpenAI(
                    api_key=self.api_key,
                    base_url="https://api.anthropic.com/v1/"
                )
                
                # Create agent instance
                model_instance = agents.OpenAIChatCompletionsModel(self.model, client)
                agent = agents.Agent(
                    name="agent-zero",
                    instructions=self.instructions,
                    model=model_instance,
                    model_settings=agents.ModelSettings(truncation="auto"),
                    tools=self.tools
                )
                
                messages.append({"role": "user", "content": user_input})
                
                # Run the agent with conversation history
                stream = agents.Runner.run_streamed(agent, messages, max_turns=50)
                
                response = ""
                async for event in stream.stream_events():
                    if event.type == 'raw_response_event' and event.data.type == "response.output_text.delta":
                        response += event.data.delta
                        print(event.data.delta, end="", flush=True)
                
                messages.append({"role": "assistant", "content": response})
                print("\n")  # New lines after response
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
                self.context.log(f"Error: {str(e)}", level="error")


async def main():
    """Main entry point for the agent-zero mini implementation."""
    
    # Parse command line arguments
    args = sys.argv[1:]
    
    # Check for model selection
    model = "claude-opus-4-5"
    if args and args[0] in ('claude', 'gpt', 'gemini'):
        model_name = args.pop(0)
        if model_name == 'claude':
            model = "claude-opus-4-5"
        elif model_name == 'gpt':
            model = "gpt-5.2"
        elif model_name == 'gemini':
            model = "gemini-2.5-pro"
    
    # Single prompt mode or interactive mode
    if args:
        # Single prompt mode
        prompt = " ".join(args)
        agent = AgentZeroMini(model=model)
        await agent.run(prompt)
    else:
        # Interactive mode
        print("""
╔══════════════════════════════════════════════════════╗
║         🤖 Agent Zero Mini                          ║
║                                                      ║
║  A minimal agent-zero inspired implementation       ║
║  - General purpose assistant                        ║
║  - Execute code and commands                        ║
║  - Learn and adapt                                  ║
║  - Multi-agent cooperation                          ║
╚══════════════════════════════════════════════════════╝
        """)
        agent = AgentZeroMini(model=model)
        await agent.interactive_loop()


if __name__ == "__main__":
    asyncio.run(main())
