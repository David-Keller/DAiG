## install.packages("igraph")

## Load package
library(igraph)

dat = read.csv("SpeedDatingData.csv")

impute_missing_data = function(x) {
  stopifnot(length(x) > 0 && sum(!is.na(x)) > 0)
  x[is.na(x)] = -1
  return(x)
}

dat$age = impute_missing_data(dat$age)
dat$age_o = impute_missing_data(dat$age_o)
dat$race = impute_missing_data(dat$race)
dat$income = as.factor(dat$income)

dat2 = data.frame(iid=unique(dat$iid))
dat2$age = aggregate(age ~ iid, data = dat, mean)$age
dat2$gender = aggregate(gender ~ iid, data = dat, mean)$gender
dat2$race = aggregate(race ~ iid, data = dat, mean)$race
dat2$hasMatch = aggregate(match ~ iid, data = dat, max)$match
dat2$metWithSameRace = aggregate(samerace ~ iid, data = dat, max)$samerace

iidOfSameRace = dat[dat$samerace == 1,]$iid
pidOfSameRace = dat[dat$samerace == 1,]$pid

x = c(1,2,2,3,3,4,4,5,1,5,5,1,116,117,117,118,118,119,119,120)
edges = c()

i = 0
while (i < length(iidOfSameRace)) {
  iid = iidOfSameRace[i+1]
  pid = pidOfSameRace[i+1]
  if (iid > 117) {
    iid = iid - 1
  }
  if (pid > 117) {
    pid = pid - 1
  }
  edges = c(edges, iid)
  edges = c(edges, pid)
  i = i + 1
}

layout.by.attr <- function(graph, wc, cluster.strength=1,layout=layout.auto) {  
  g <- graph.edgelist(get.edgelist(graph)) # create a lightweight copy of graph w/o the attributes.
  E(g)$weight <- 1
  
  attr <- cbind(id=1:vcount(g), val=wc)
  g <- g + vertices(unique(attr[,2])) + igraph::edges(unlist(t(attr)), weight=cluster.strength)
  
  l <- layout(g, weights=E(g)$weight)[1:vcount(graph),]
  return(l)
}

g = make_empty_graph(n = length(unique(dat$iid)), directed=FALSE) %>% add_edges(edges)
g = simplify(g, remove.multiple=TRUE)
V(g)$label = unique(dat$iid)
plot(g, vertex.size=2, edge.width=1, edge.color="red", vertex.label.cex=0.5, vertex.label.dist=0.4, vertex.label.degree=-pi/2, layout=layout.by.attr(g, wc=1))

compDF = data.frame(components(g)$membership)
compTableDF = data.frame(table(components(g)$membership))
nameMatchVar = setNames(as.character(compTableDF$Freq), compTableDF$Var1)
totalCompDF = data.frame(lapply(y, function(i) nameMatchVar[i]))
componentTotalNodes = totalCompDF$components.g..membership

dat2$componentTotalNodes = componentTotalNodes

