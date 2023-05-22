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

or

```console
./exportGraph.py
```

The output will be a `graph.json` file that contains the vault graph nodes and edges.

## Simplyfing the data

The node names in the `graph.json` will likely be long strings, because each node represents a title of a subject or a class.

That is why we needed to simplify, rename the graph to be a little more readable for the human eye.

For this I provided a python script that will rename each node according to a scheme.

The scheme will be the following:

- ${node}_i,\space \forall i \in S , {where} \space S \space is \space the \space Graph$; the first node will be: `node1`, the second `node2` and so on.

## Running the script for renaming the graph

The script will need two arguments:

- The `graph.json`
- And the new `renamed.json`, this will be created from the first `graph.json`

```console
python3 renameGraph.py /path/to/graph.json /path/to/renamed.json
```

or

```console
./renameGraph.py /path/to/graph.json /path/to/renamed.json
```
