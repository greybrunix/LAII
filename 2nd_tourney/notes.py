# Graph Problems

def build(arestas):
    adj = {}
    for o,d in arestas:
        if o not in adj:
            adj[o] = set();
        if d not in adj:
            adj[d] = set()
        adj[o].add(d)
        adj[d].add(o)
    return adj;

def dfs(adj, o):
    return dfs_aux(adj, o, set(), {});

def dfs_aux(adj, o, vis, par):
   vis.add(o)
   for d in adj[o]:
       if d not in vis:
           pai[d] = 0;
           dfs_aux(adj, d, vis, par);
   return par;

def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
      v = queue.pop(0)
      for d in adj[v]:
        if d not in vis:
          vis.add(d)
          pai[d] = v;
          queue.append(d)
    return pai;

def build_weighted(arestas):
    adj = {}
    for o,d,p in arestas:
        if o not in adj:
            adj[o] = {}
        if d not in adj:
            adj[d] = {}
        adj[o][d] = p
        adj[d][o] = p
    return adj

def dijkstra(adj, o):
    par = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla, key= lambda x: dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v;
                dist[d] = dist[v] + adj[v][d]
    return pai


def saltos(o,d):
    # bfs
    vis = {o};
    queue = [o]
    num = 1
    pai = {}
    if o == d:
        queue.clear()
    while queue:
        v = queue.pop(0)
        x,y = v
        cena = [(x+1,y-2),(x+2,y-1),
                  (x+1,y+2),(x+2,y+1),
                  (x-1,y+2),(x-2,y+1),
                  (x-1,y-2),(x-2,y-1)
                  ]
        if d in cena:
            pai[d] = v;
            queue.clear();
        else:
            for f in cena:
                if f not in vis:
                    vis.add(f)
                    pai[f] = v;
                    queue.append(f)
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0,d)
    return len(caminho)-1;



