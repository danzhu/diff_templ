def bfs_by_row(root):
    row = [root]
    while len(row) > 0:
        next_row = []
        for node in row:
            for child in node.children:
                if OK(child):
                    return FOUND(child)
                next_row.append(child)
        row = next_row
    return NOT_FOUND
