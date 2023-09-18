from src.algo.traverse import floydwarshall

def test_correctness():
    """Test against known graphs."""
    # directed graph
    adj = [[(2,-2)], [(0,4),(2,3)], [(3,2)], [(1,-1)]]
    m = len(adj)
    exp = [[0,-1,-2,0], [4,0,2,4], [5,1,0,2], [3,-1,1,0]]
    mat = floydwarshall(adj)
    assert len(mat) == len(exp)
    assert len(mat[0]) == len(exp[0])
    for i in range(m):
        for j in range(m):
            assert exp[i][j] == mat[i][j]
