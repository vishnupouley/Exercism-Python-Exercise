def saddle_points(matrix):
    if not matrix: 
        return matrix
    if len(set([len(tree_row) for tree_row in matrix])) != 1:
        raise ValueError("irregular matrix")
    suitable_tree = []
    for index_1, trees_column_1 in enumerate(matrix):
        max_height = max(trees_column_1)
        max_indices = [i for i, x in enumerate(trees_column_1) if x == max_height]
        column = 0
        for max_index in max_indices:
            for index_2, trees_column_2 in enumerate(matrix):
                if index_2 == index_1 and len(matrix) > 1:
                    continue
                else:
                    if trees_column_2[max_index] >= max_height:
                        column = max_index + 1
                    else:
                        column = 0
            if column:
                suitable_tree.append({"row": index_1 + 1, "column": column})
    return suitable_tree