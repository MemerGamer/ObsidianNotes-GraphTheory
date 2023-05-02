# Data Extractions

I needed to extract data from my Obsidian Graph view that was dinamically created by Obsidian real time.

For that I wrote a little python script called [exportGraph](./exportGraph.py)

## Note

By default the script expects that it's root directory is the vaults directory.
If you want to use it, you need to copy to the obsidian vaults folder.

## Dependencies for the script

- json
- networkx
- obsidiantools

You can install them with:

```console
pip install -r requirements.txt
```

## Running the script

You will need to run the script with python3

```console
python3 exportGraph.py
```

The output will be a `graph.json` file that contains the vault graph nodes and edges.
