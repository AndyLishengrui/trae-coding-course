import sys
import os
import json
# Add parent directory to path to import xmuoj-mcp
sys.path.append(os.path.join(os.getcwd(), 'xmuoj-mcp'))

from server import XMUOJClient

def main():
    client = XMUOJClient()
    try:
        print("Searching for 'ACW'...")
        # Search usually matches title or ID
        results = client.search_problem("ACW", limit=100)
        
        if results:
            print(f"Found {len(results)} problems.")
            
            # Filter: Must start with ACW and have Low difficulty
            candidates = []
            for p in results:
                display_id = p.get('_id', '')
                difficulty = p.get('difficulty', '')
                
                if display_id.startswith('ACW'):
                    # Check difficulty. 
                    if difficulty == 'Low':
                         candidates.append(p)
            
            print(f"Found {len(candidates)} 'Low' difficulty ACW problems.")
            
            # Sort by Numeric ID: ACW1076 -> 1076
            def get_id_num(p):
                did = p.get('_id', '')
                # Extract number part
                import re
                match = re.search(r'\d+', did)
                if match:
                    return int(match.group(0))
                return 999999
            
            candidates.sort(key=get_id_num)
            
            # Take top 5
            top_5 = candidates[:5]
            if top_5:
                ids = [p['_id'] for p in top_5]
                print("ids=" + ",".join(ids))
                
                # Print titles for user confirmation
                for p in top_5:
                    print(f"- {p['_id']}: {p['title']}")
            else:
                print("No suitable problems found.")
        else:
            print("No problems found with keyword 'ACW'.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
