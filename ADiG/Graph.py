import csv
import math
from igraph import *
import pandas as pd

df = pd.read_csv('/Users/davidjia/Desktop/SpeedDatingData.csv', encoding = "ISO-8859-1")
iid = df['iid']
personid = df['id']
pid = df['pid']
partnerid = df['partner']
isMatch = df['match']

def printAllConnections():
    g = Graph()

    g.add_vertices(iid.nunique())

    g.vs["person"] = iid.unique()

    for n in range(0,iid.size):
        if not math.isnan(iid[n]) and not math.isnan(pid[n]):
            currentIID = iid[n] - 1
            currentPID = int(pid[n]) - 1
            if iid[n] > 117:
                currentIID = currentIID - 1
            if pid[n] > 117:
                currentPID = currentPID - 1
            if g.get_eid(currentIID, currentPID, directed=False, error=False) == -1:
                g.add_edges([(currentIID, currentPID)])


    g.vs["label"] = g.vs["person"]

    layout = g.layout("kk")

    community = g.community_multilevel()

    out = plot(community, layout=layout, bbox=(3000,3000), mark_groups=True, vertex_size=30, vertex_label_size=15)

    out.save("Graph.png")

def printAllMatches():
    g = Graph()

    g.add_vertices(iid.nunique())

    g.vs["person"] = iid.unique()

    for n in range(0,iid.size):
        if not math.isnan(iid[n]) and not math.isnan(pid[n]):
            currentIID = iid[n] - 1
            currentPID = int(pid[n]) - 1
            if iid[n] > 117:
                currentIID = currentIID - 1
            if pid[n] > 117:
                currentPID = currentPID - 1
            if g.get_eid(currentIID, currentPID, directed=False, error=False) == -1 and isMatch[n] == 1:
                g.add_edges([(currentIID, currentPID)])


    g.vs["label"] = g.vs["person"]

    layout = g.layout("kk")

    community = g.community_multilevel()

    out = plot(community, layout=layout, bbox=(3000,3000), mark_groups=True, vertex_size=30, vertex_label_size=15)

    out.save("Graph.png")
