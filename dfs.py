graph = { "1" : ["2", "3"],
          "2" : ["1", "4", "10"],
          "3" : ["5", "6", "8"],
          "4" : ["2", "7", "9"],
          "5" : ["3", "8"],
          "6" : ["3", "8"],
          "7" : ["4", "9"],
          "8" : ["5", "6", "10", "11"],
          "9" : ["4", "7", "12", "13"],
          "10" : ["2", "8"],
          "11" : ["8"],
          "12" : ["9"],
          "13" : ["9"]
          }
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

visited = dfs(graph,"1", [])
print(visited)
