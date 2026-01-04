import heapq
class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, node1, node2, weight):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1][node2] = weight
            self.graph[node2][node1] = weight 

    def display(self):
        for node, edges in self.graph.items():
            print(f"{node}: {edges}\n")
    
    def Dijkstra_alg(self,start_node,end_node):
        p_q = [(0.0 , start_node)]
        d = {n: float('inf') for n in self.graph}
        p = {n: None for n in self.graph}
        d[start_node] = 0

        while p_q:
            dist, node = heapq.heappop(p_q)
            if node == end_node: 
                break
            for nbr, w in self.graph[node].items():
                if dist + w < d[nbr]: 
                    d[nbr], p[nbr] = dist + w, node
                    heapq.heappush(p_q, (d[nbr], nbr))

        path = []
        while end_node: 
            path.append(end_node)
            end_node = p[end_node]
        return d[path[0]], path[::-1]
   


weighted_grapth = Graph()

weighted_grapth.add_node("Hung Hom")
weighted_grapth.add_node("Mong Kok East")
weighted_grapth.add_node("Central")
weighted_grapth.add_node("Admirality")
weighted_grapth.add_node("Jordan")
weighted_grapth.add_node("Sha tin")
weighted_grapth.add_node("Tai Wu")

weighted_grapth.add_edge("Hung Hom","Mong Kok East",2)
weighted_grapth.add_edge("Hung Hom","Central",6)
weighted_grapth.add_edge("Admirality","Mong Kok East",5)
weighted_grapth.add_edge("Admirality","Central",5)
weighted_grapth.add_edge("Admirality","Jordan",10)
weighted_grapth.add_edge("Admirality","Sha tin",15)
weighted_grapth.add_edge("Tai Wu","Jordan",2)
weighted_grapth.add_edge("Sha tin","Tai Wu",6)

weighted_grapth.display()
print(weighted_grapth.Dijkstra_alg("Hung Hom","Tai Wu"))