import json
import glob
import os

notebooks = glob.glob("*.ipynb")
for nb_file in notebooks:
    with open(nb_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for cell in data.get("cells", []):
        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
            
    with open(nb_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1)
        
print("All notebook outputs have been cleared.")
