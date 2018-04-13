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
isPartnerMatch = df['dec_o']
sameRace = df['samerace']
ratingFromPartner = df['attr_o']
ratingFromPartner.fillna(-1, inplace=True)

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

    out.save("AllNodesWithConnections.png")

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
            if g.get_eid(currentIID, currentPID, directed=False, error=False) == -1 and isMatch[n] == 1 and isPartnerMatch[n] == 1:
                g.add_edges([(currentIID, currentPID)])


    g.vs["label"] = g.vs["person"]

    layout = g.layout("kk")

    community = g.community_multilevel()

    out = plot(community, layout=layout, bbox=(3000,3000), mark_groups=True, vertex_size=30, vertex_label_size=15)

    out.save("NodesThatHaveMatched.png")

def printAllSameRaceMatches():
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
            if g.get_eid(currentIID, currentPID, directed=False, error=False) == -1 and isMatch[n] == 1 and isPartnerMatch[n] == 1 and sameRace[n] == 1:
                g.add_edges([(currentIID, currentPID)])

    g.vs["label"] = g.vs["person"]

    layout = g.layout("kk")

    community = g.community_multilevel()

    out = plot(community, layout=layout, bbox=(3000,3000), mark_groups=True, vertex_size=30, vertex_label_size=15)

    out.save("SameRaceMatches.png")

def printAllDifferentRaceMatches():
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
            if g.get_eid(currentIID, currentPID, directed=False, error=False) == -1 and isMatch[n] == 1 and isPartnerMatch[n] == 1 and sameRace[n] == 0:
                g.add_edges([(currentIID, currentPID)])

    g.vs["label"] = g.vs["person"]

    layout = g.layout("kk")

    community = g.community_multilevel()

    out = plot(community, layout=layout, bbox=(3000,3000), mark_groups=True, vertex_size=30, vertex_label_size=15)

    out.save("DifferentRaceMatches.png")

def printConnectionsWherePartnerRatedAtLeast5():
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
            if g.get_eid(currentIID, currentPID, directed=False, error=False) == -1 and ratingFromPartner[n] >= 5:
                g.add_edges([(currentIID, currentPID)])

    g.vs["label"] = g.vs["person"]

    layout = g.layout("kk")

    community = g.community_multilevel()

    out = plot(community, layout=layout, bbox=(3000,3000), mark_groups=True, vertex_size=30, vertex_label_size=15)

    out.save("ConnectionsWherePartnerRatedAtLeast5.png")

def printConnectionsWherePartnerRatedAtLeast6():
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
            if g.get_eid(currentIID, currentPID, directed=False, error=False) == -1 and ratingFromPartner[n] >= 6:
                g.add_edges([(currentIID, currentPID)])

    g.vs["label"] = g.vs["person"]

    layout = g.layout("kk")

    community = g.community_multilevel()

    out = plot(community, layout=layout, bbox=(3000,3000), mark_groups=True, vertex_size=30, vertex_label_size=15)

    out.save("ConnectionsWherePartnerRatedAtLeast6.png")

def printConnectionsWherePartnerRatedAtLeast7():
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
            if g.get_eid(currentIID, currentPID, directed=False, error=False) == -1 and ratingFromPartner[n] >= 7:
                g.add_edges([(currentIID, currentPID)])

    g.vs["label"] = g.vs["person"]

    layout = g.layout("kk")

    community = g.community_multilevel()

    out = plot(community, layout=layout, bbox=(3000,3000), mark_groups=True, vertex_size=30, vertex_label_size=15)

    out.save("ConnectionsWherePartnerRatedAtLeast7.png")

def printConnectionsWherePartnerRatedAtLeast8():
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
            if g.get_eid(currentIID, currentPID, directed=False, error=False) == -1 and ratingFromPartner[n] >= 8:
                g.add_edges([(currentIID, currentPID)])

    g.vs["label"] = g.vs["person"]

    layout = g.layout("kk")

    community = g.community_multilevel()

    out = plot(community, layout=layout, bbox=(3000,3000), mark_groups=True, vertex_size=30, vertex_label_size=15)

    out.save("ConnectionsWherePartnerRatedAtLeast8.png")

def printConnectionsWherePartnerRatedAtLeast9():
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
            if g.get_eid(currentIID, currentPID, directed=False, error=False) == -1 and ratingFromPartner[n] >= 9:
                g.add_edges([(currentIID, currentPID)])

    g.vs["label"] = g.vs["person"]

    layout = g.layout("kk")

    community = g.community_multilevel()

    out = plot(community, layout=layout, bbox=(3000,3000), mark_groups=True, vertex_size=30, vertex_label_size=15)

    out.save("ConnectionsWherePartnerRatedAtLeast9.png")

def printConnectionsWherePartnerRatedAtLeast10():
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
            if g.get_eid(currentIID, currentPID, directed=False, error=False) == -1 and ratingFromPartner[n] >= 10:
                g.add_edges([(currentIID, currentPID)])

    g.vs["label"] = g.vs["person"]

    layout = g.layout("kk")

    community = g.community_multilevel()

    out = plot(community, layout=layout, bbox=(3000,3000), mark_groups=True, vertex_size=30, vertex_label_size=15)

    out.save("ConnectionsWherePartnerRatedAtLeast10.png")
