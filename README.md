# Running Graph Algorithms on Obsidian Graph

This repository contains Python scripts for running graph algorithms on a graph extracted from an [Obsidian](https://obsidian.md) notes graph view.

## Introduction

Obsidian is a powerful note-taking app that allows users to create and link notes in a graph-like structure. The app has a graph view that displays the relationships between the notes as nodes and edges.

This repository provides a way to extract the graph structure from the Obsidian graph view and run graph algorithms on it using Python. This can be useful for analyzing the structure of your notes and identifying patterns and insights.

## Setup

You will need `git`, `python3` and `pip` installed.

You need to clone the repository:

```console
git clone https://github.com/MemerGamer/ObsidianNotes-GraphTheory.git
```

## Data extraction

For discretion I will not include my `graph.json` file, however I provide [my method for extracting the graph](./DataExtraction/).

## If you don't want to extract the Graph from Obsidian

At the moment of extracting the graph I found out the graphs JSON structure. I created examples which you can use for testing the algorithm implementations.
[Examples](./DataExtraction/examples/)

## Running the Algorithms

### Dependencies

Before we can run any python programs we need to install the dependencies for the projects

```console
pip install -r requirements.txt
```

**Note:** This `requirements.txt` is different than the one used in the Data Extraction method.

All the allgorithms will be in the [Algorithms](./Algorithms/) directory.

Running them will be as simple as running the script for the algorithm and giving the `path to the graph.json` as an argument.

For example:

```console
cd Algorithms

python3 bfs.py /path/to/graph.json
```
