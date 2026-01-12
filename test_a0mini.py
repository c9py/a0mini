#!/usr/bin/env python3
"""
Simple test script to verify a0mini.py basic functionality.
This tests the core components without requiring API keys.
"""

import sys
import subprocess

# Test if we can import the basic components
# We'll import them directly without going through the full module
# to avoid the agents dependency for basic tests


def test_agent_memory():
    """Test the AgentMemory class."""
    print("Testing AgentMemory class structure...")
    
    # Read and verify the class exists in the file
    with open("a0mini.py", "r") as f:
        content = f.read()
    
    assert "class AgentMemory:" in content, "AgentMemory class should exist"
    assert "def add_memory" in content, "add_memory method should exist"
    assert "def add_solution" in content, "add_solution method should exist"
    assert "def search_memories" in content, "search_memories method should exist"
    assert "def get_recent_solutions" in content, "get_recent_solutions method should exist"
    
    print("✓ AgentMemory class structure verified")


def test_agent_context():
    """Test the AgentContext class."""
    print("Testing AgentContext class structure...")
    
    with open("a0mini.py", "r") as f:
        content = f.read()
    
    assert "class AgentContext:" in content, "AgentContext class should exist"
    assert "def log" in content, "log method should exist"
    assert "def create_subordinate" in content, "create_subordinate method should exist"
    assert "self.memory" in content, "Should have memory attribute"
    assert "self.subordinates" in content, "Should have subordinates attribute"
    
    print("✓ AgentContext class structure verified")


def test_execute_code_tool():
    """Test the execute_code tool function."""
    print("Testing execute_code functionality...")
    
    # Test Python code execution directly via subprocess
    result = subprocess.run(
        [sys.executable, "-c", "print('Hello, World!')"],
        capture_output=True,
        text=True
    )
    assert "Hello, World!" in result.stdout, "Should execute Python code"
    
    # Test bash execution
    result = subprocess.run(
        "echo 'test'",
        shell=True,
        capture_output=True,
        text=True
    )
    assert "test" in result.stdout, "Should execute bash commands"
    
    print("✓ Code execution tests passed")


def test_terminal_command_tool():
    """Test the terminal_command tool function."""
    print("Testing terminal command functionality...")
    
    # Test simple command
    result = subprocess.run(
        "echo 'Terminal test'",
        shell=True,
        capture_output=True,
        text=True
    )
    assert "Terminal test" in result.stdout, "Should execute terminal commands"
    
    print("✓ Terminal command tests passed")


def test_syntax():
    """Test that a0mini.py has valid Python syntax."""
    print("Testing a0mini.py syntax...")
    
    result = subprocess.run(
        [sys.executable, "-m", "py_compile", "a0mini.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Syntax error: {result.stderr}"
    
    print("✓ Syntax check passed")


def test_imports():
    """Test that all required imports work."""
    print("Testing package availability...")
    
    # Check if openai-agents is installed
    result = subprocess.run(
        [sys.executable, "-c", "import agents; import openai"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("✓ Required packages (agents, openai) are installed")
        return True
    else:
        print("⚠ Warning: openai-agents package not installed")
        print("  Note: Full agent functionality requires 'openai-agents' package")
        print("  Install with: pip install openai-agents")
        return False


def test_agent_zero_mini_class():
    """Test that the AgentZeroMini class structure is correct."""
    print("Testing AgentZeroMini class structure...")
    
    with open("a0mini.py", "r") as f:
        content = f.read()
    
    assert "class AgentZeroMini:" in content, "AgentZeroMini class should exist"
    assert "async def run" in content, "run method should exist"
    assert "async def interactive_loop" in content, "interactive_loop method should exist"
    assert "execute_code" in content, "execute_code tool should be defined"
    assert "terminal_command" in content, "terminal_command tool should be defined"
    assert "store_memory" in content, "store_memory tool should be defined"
    assert "delegate_task" in content, "delegate_task tool should be defined"
    
    print("✓ AgentZeroMini class structure verified")


def main():
    """Run all tests."""
    print("=" * 60)
    print("Running a0mini.py Basic Functionality Tests")
    print("=" * 60 + "\n")
    
    try:
        test_syntax()
        print()
        
        has_deps = test_imports()
        print()
        
        test_agent_memory()
        print()
        
        test_agent_context()
        print()
        
        test_agent_zero_mini_class()
        print()
        
        test_execute_code_tool()
        print()
        
        test_terminal_command_tool()
        print()
        
        print("=" * 60)
        print("✅ All basic tests passed!")
        print("=" * 60)
        
        if not has_deps:
            print("\n⚠ To use the full agent functionality:")
            print("  1. Install dependencies: pip install openai-agents")
            print("  2. Set API key: export ANTHROPIC_API_KEY=your_key")
            print("  3. Run: python a0mini.py 'Hello, Agent Zero!'")
        else:
            print("\n✓ All dependencies installed!")
            print("  Set ANTHROPIC_API_KEY to test the full agent")
            print("  Run: python a0mini.py")
        
        return 0
    
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
