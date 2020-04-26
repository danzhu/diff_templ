def bfs_by_row(root):
    visited = set()
    row = [root]
    while len(row) > 0:
        next_row = []
        for node in row:
            for child in node.children:
                if child in visited:
                    continue
                next_row.append(child)
                visited.add(child)
        row = next_row
