# Tiny Agents

Minimal coding, computer-use, and research agents using the OpenAI Agents SDK.

* [code.py](code.py) - A minimal coding agent in 250 lines of Python code.
* [cua.py](cua.py) - A minimal computer-use agent in 100 lines of Python code.
* [research.py](research.py) - A minimal research agent in 100 lines of Python code.
* [a0mini.py](a0mini.py) - A minimal agent-zero inspired agent in 350 lines of Python code.

## Get started

Clone this repository, install the OpenAI Agents SDK, and set the OpenAI API key

```bash
git clone https://github.com/lutzroeder/agents
pip install openai-agents
# Windows
set OPENAI_API_KEY=...
# macOS/Linux
export OPENAI_API_KEY=...
```

## Coding Agent

A minimal coding agent inspired by [Raising the bar on SWE-bench](https://www.anthropic.com/engineering/swe-bench-sonnet) in 250 lines of Python code.

```bash
python code.py <directory>
```
```
👤 User: Explain this code to me
🤖 I'll help you understand the code in this repository. Let's first explore the repository structure to get a better understanding of what we're looking at.
🔍 > view .
Let's check the main code file, gpt2.py:
🔍 > view gpt2.py
Let's also check the README to understand more about this project:
🔍 > view README.md
This repository contains a minimalist implementation of OpenAI's GPT-2 language model using PyTorch.
...
```

## Computer-Use Agent

A minimal computer-use agent in 100 lines of Python code.

```bash
pip install pyautogui
python cua.py
```
```
👤 User: Open browser at lutzroeder.com
   screenshot {}

🤖 Action: Opening web browser, checking Edge icon
   click {'button': 'left', 'x': 1388, 'y': 1544}
   wait {}

🤖 Action: Navigating to lutzroeder.com in Edge
   click {'button': 'left', 'x': 1056, 'y': 104}
   type {'text': 'lutzroeder.com'}
   keypress {'keys': ['ENTER']}
   wait {}

🤖 Agent: The website lutzroeder.com is open in the browser...

👤 User: 
```

## Research Agent

A minimal research agent in 100 lines of Python code.

```bash
python research.py
```
```
👤 User: top news today
🤖 Planning ✔
🔍 Searching ✔
📝 Summarizing ✔

This comprehensive report synthesizes today's top news...
```

## Agent Zero Mini

A minimal agent-zero inspired agent in 350 lines of Python code based on [agent-zero](https://github.com/agent0ai/agent-zero).

```bash
python a0mini.py
```

Agent Zero Mini is a general-purpose AI assistant that:
- **Adapts organically** - Not pre-programmed for specific tasks, learns as you use it
- **Uses computer as a tool** - Executes code and terminal commands to accomplish tasks
- **Supports multi-agent cooperation** - Can delegate subtasks to subordinate agents
- **Has persistent memory** - Stores successful solutions for future reference
- **Fully transparent** - All behavior defined through customizable prompts

```
╔══════════════════════════════════════════════════════╗
║         🤖 Agent Zero Mini                          ║
║                                                      ║
║  A minimal agent-zero inspired implementation       ║
║  - General purpose assistant                        ║
║  - Execute code and commands                        ║
║  - Learn and adapt                                  ║
║  - Multi-agent cooperation                          ║
╚══════════════════════════════════════════════════════╝

👤 User: Create a Python script that calculates fibonacci numbers
🤖 Agent Zero: I'll create a Python script that calculates Fibonacci numbers...

🔧 Executing python code
✓ Created fibonacci.py

The script is ready. You can run it with: python fibonacci.py

👤 User: quit
👋 Goodbye!
```

### Features

**General Purpose**: Agent Zero Mini can handle a wide variety of tasks by adapting its approach based on the request. It's not limited to specific domains.

**Code Execution**: The agent can write and execute Python code or shell commands to accomplish tasks, making it capable of:
- Creating and running scripts
- Processing data
- Automating tasks
- Installing packages
- File manipulation

**Memory System**: Simple in-memory storage allows the agent to:
- Remember facts and context
- Store successful solutions
- Retrieve past experiences
- Learn from previous interactions

**Multi-Agent Cooperation**: Complex tasks can be broken down and delegated to subordinate agents, keeping each agent's context clean and focused.

**Flexible Models**: Supports multiple LLM backends:
```bash
python a0mini.py claude    # Use Claude (default)
python a0mini.py gpt       # Use GPT
python a0mini.py gemini    # Use Gemini
```

### Single Prompt Mode

You can also use it in single-prompt mode for quick tasks:
```bash
python a0mini.py "What's the weather like today?"
python a0mini.py "Create a script to organize files by extension"
```
