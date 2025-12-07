#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from agentic_researcher.crew import AgenticResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    # Get topic from user or use default
    import sys
    if len(sys.argv) > 1:
        topic = ' '.join(sys.argv[1:])
    else:
        print("\n=== Scientific Research Assistant ===")
        print("This assistant will help you write a 1-page scientific document.\n")
        topic = input("Enter a scientific topic (e.g., 'CRISPR gene editing', 'quantum entanglement', 'neuroplasticity'): ").strip()
        if not topic:
            topic = 'CRISPR gene editing technology'
            print(f"Using default topic: {topic}\n")
    
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }

    try:
        result = AgenticResearcher().crew().kickoff(inputs=inputs)
        print("\n" + "="*60)
        print("✓ Research complete! Your 1-page scientific document has been saved to 'report.md'")
        print("="*60 + "\n")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    Runs the crew multiple times with different inputs to optimize agent behavior and task execution
    """
    inputs = {
        "topic": "quantum computing applications in drug discovery",
        'current_year': str(datetime.now().year)
    }
    try:
        AgenticResearcher().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AgenticResearcher().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    Tests the crew execution and evaluates performance
    """
    inputs = {
        "topic": "neural mechanisms of memory consolidation",
        "current_year": str(datetime.now().year)
    }

    try:
        AgenticResearcher().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = AgenticResearcher().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
