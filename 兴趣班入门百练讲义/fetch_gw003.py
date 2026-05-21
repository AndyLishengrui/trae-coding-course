import sys
import os
# Add the directory containing server.py to sys.path
sys.path.append(os.path.join(os.getcwd(), 'xmuoj-mcp'))
from server import XMUOJClient

def main():
    client = XMUOJClient()
    try:
        print("Logging in...")
        msg = client.login("andy", "andy@5dg")
        print(msg)
        
        print("Fetching problem GW003...")
        problem = client.get_problem("GW003")
        
        print("---PROBLEM START---")
        print(f"Title: {problem['title']}")
        print(f"Description: {problem['description']}")
        print(f"Input: {problem['input_description']}")
        print(f"Output: {problem['output_description']}")
        print(f"Samples: {problem['samples']}")
        print("---PROBLEM END---")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
