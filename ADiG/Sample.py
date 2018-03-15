import csv
import igraph

reader = csv.DictReader(open("/Users/davidjia/Desktop/SpeedDatingData.csv"), dialect="excel")
g = igraph.Graph.DictList(vertices=reader, edges=reader)

# Edgelist
# 2 columns of vertex labels
# person a -> person b
# person a -> person c
# Selection on raw Data
# Once I load data, think of statistics, how to filter based on edge criteria
# What is a good filter, what is bad, how to determine this?
# Can I make any filter in the first place?
# Work in parallel, given the graph that we make, how do we visualize the results?
# potential D3/3D? object, interactive widget
