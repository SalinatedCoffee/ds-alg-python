from src.algo.traverse import floydwarshall

def test_correctness():
    """Test against known graphs."""
    # directed graph
    adj = [[(2,-2)], [(0,4),(2,3)], [(3,2)], [(1,-1)]]
    m = len(adj)
    # expected cost matrix
    exp = [[0,-1,-2,0], [4,0,2,4], [5,1,0,2], [3,-1,1,0]]
    mat = floydwarshall(adj)
    # check if returned matrix has correct dimensions
    assert len(mat) == len(mat[0]) == m
    # check contents of cost matrices
    for i in range(m):
        for j in range(m):
            assert exp[i][j] == mat[i][j]

    # undirected graph with positive edge weights
    adj = [[(1,4),(2,1)], [(0,4),(2,3),(3,1)], [(0,1),(1,3),(3,2)], [(1,1),(2,2)]]
    m = len(adj)
    exp = [[0,4,1,3], [4,0,3,1], [1,3,0,2], [3,1,2,0]]
    mat = floydwarshall(adj)
    assert len(mat) == len(mat[0]) == m
    for i in range(m):
        for j in range(m):
            assert exp[i][j] == mat[i][j]
