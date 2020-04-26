def bfs_by_row(root):
    dist = 0
    row = [root]
    while len(row) > 0:
        dist += 1
        next_row = []
        for node in row:
            for child in node.children:
                # here `dist` is distance from `root` to `child`
                next_row.append(child)
        row = next_row
