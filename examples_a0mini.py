#!/usr/bin/env python3
"""
Example usage scenarios for Agent Zero Mini.

This demonstrates the capabilities without requiring API keys.
For actual usage, you'll need to set up API credentials.
"""

print("""
╔══════════════════════════════════════════════════════════════════╗
║                  Agent Zero Mini - Examples                      ║
╚══════════════════════════════════════════════════════════════════╝

Agent Zero Mini is a minimal implementation inspired by agent-zero
that brings general-purpose AI assistance to your terminal.

KEY FEATURES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 🧠 General Purpose Assistant
   - Adapts to any task, not pre-programmed for specific domains
   - Learns from experience and stores successful solutions
   - Natural conversation interface

2. 💻 Computer as a Tool
   - Executes Python code and shell commands
   - Creates and runs scripts on demand
   - Installs packages and manages files
   - No single-purpose tools - creates what it needs

3. 🤝 Multi-Agent Cooperation
   - Delegates complex subtasks to subordinate agents
   - Hierarchical structure keeps context clean
   - Each agent reports back to its superior

4. 🔧 Fully Customizable
   - All behavior defined through prompts
   - Transparent operation - nothing hidden
   - Extensible tool system

EXAMPLE USE CASES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 Development Tasks:
   $ python a0mini.py "Create a Python script to analyze CSV files"
   $ python a0mini.py "Write unit tests for my calculator function"
   $ python a0mini.py "Set up a basic Flask web server"

🔍 Research & Analysis:
   $ python a0mini.py "Find the latest Python best practices for async code"
   $ python a0mini.py "Compare different sorting algorithms"
   $ python a0mini.py "Summarize recent AI developments"

📊 Data Processing:
   $ python a0mini.py "Parse this JSON file and create a summary report"
   $ python a0mini.py "Convert all PNG images to JPEG in this directory"
   $ python a0mini.py "Find all TODO comments in Python files"

⚙️ System Tasks:
   $ python a0mini.py "Check disk usage and list large files"
   $ python a0mini.py "Create a backup script for my projects"
   $ python a0mini.py "Monitor system resources"

INTERACTIVE MODE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Start an interactive session:
   $ python a0mini.py

Example conversation:
   👤 User: Create a fibonacci calculator
   🤖 Agent Zero: I'll create a Python script...
   
   🔧 Executing python code
   ✓ Created fibonacci.py
   
   The script calculates fibonacci numbers. Try: python fibonacci.py 10
   
   👤 User: Now add memoization to make it faster
   🤖 Agent Zero: I'll optimize it with memoization...
   
   ✓ Updated fibonacci.py with memoized version
   
   👤 User: quit
   👋 Goodbye!

MODEL SELECTION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Choose your preferred AI model:
   $ python a0mini.py claude    # Anthropic Claude (default)
   $ python a0mini.py gpt       # OpenAI GPT
   $ python a0mini.py gemini    # Google Gemini

ARCHITECTURE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────┐
│           User / Superior Agent              │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│         Agent Zero Mini (Agent 0)            │
│  ┌────────────────────────────────────────┐ │
│  │  Context & Memory                      │ │
│  │  - Logs & History                      │ │
│  │  - Solutions Database                  │ │
│  │  - Learned Facts                       │ │
│  └────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────┐ │
│  │  Tools                                 │ │
│  │  - Code Execution (Python/Bash)        │ │
│  │  - Terminal Commands                   │ │
│  │  - Web Search                          │ │
│  │  - Memory Storage                      │ │
│  │  - Task Delegation                     │ │
│  └────────────────────────────────────────┘ │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
        ┌─────────┴─────────┐
        ▼                   ▼
┌───────────────┐   ┌───────────────┐
│ Subordinate   │   │ Subordinate   │
│ Agent 0.0     │   │ Agent 0.1     │
└───────────────┘   └───────────────┘

HOW IT WORKS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. User provides a task or question
2. Agent analyzes the request
3. Agent plans its approach
4. Agent uses available tools:
   - Executes code to accomplish tasks
   - Searches web for information
   - Delegates complex subtasks
5. Agent reports results
6. Successful solutions stored in memory
7. Future similar tasks completed faster

GETTING STARTED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Install dependencies:
   $ pip install openai-agents

2. Set your API key (choose one):
   $ export ANTHROPIC_API_KEY=your_key_here    # For Claude
   $ export OPENAI_API_KEY=your_key_here       # For GPT
   $ export GEMINI_API_KEY=your_key_here       # For Gemini

3. Run the agent:
   $ python a0mini.py                          # Interactive mode
   $ python a0mini.py "your task here"         # Single prompt mode

COMPARISON WITH OTHER AGENTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• code.py (250 lines): Specialized for coding tasks
  - File editing tools
  - Build and test integration
  - Repository-focused

• cua.py (100 lines): Computer use automation
  - Screen capture and mouse/keyboard control
  - GUI automation
  - Visual task execution

• research.py (100 lines): Research and summarization
  - Multi-query planning
  - Parallel web searches
  - Report generation

• a0mini.py (350 lines): General-purpose agent-zero
  - ✓ All-purpose assistant
  - ✓ Code execution
  - ✓ Memory and learning
  - ✓ Multi-agent cooperation
  - ✓ Dynamic tool creation
  - ✓ Hierarchical task delegation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For more information, see:
  • README.md in this repository
  • https://github.com/agent0ai/agent-zero (original agent-zero)

To run tests:
  $ python test_a0mini.py

""")
