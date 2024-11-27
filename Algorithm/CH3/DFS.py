def dfs(grpah, start, visited) :
    if start not in visited:
        visited.add(start)
        print(start, end= ' ')
        nbr = grpah[start] - visited
        for v in nbr:
            dfs(grpah, v, visited)