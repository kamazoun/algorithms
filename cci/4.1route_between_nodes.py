R'''
Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
'''
import Collections

def route_between_nodes(graph, node1, node2):
    n = node1
    m = node2

    if not graph:
        return False

    if not n or not m or n == m:
        return True

    ht = Collections.defaultdict(int)
    qn = Collections.deque()
    qm = Collections.deque()

    qn.append(n)
    qm.append(m)

    while qn or qm:
        n = qn.popleft()
        m = qn.popleft()

        ht[n.data] ^= 1 << 1
        if ht[n.data] == 3:
            return True
        ht[m.data] ^= 1 << 0
        if ht[m.data] == 3:
            return True

        # Here I do not check if visited for the same reasons I put the flag into a hashtable: We would need to modify the underlying data structure for the vertices to have a visitedLeft and visitedRight (and also a flag set to 0 at the beginning). I will implement this model too. Here even if the vertex has been visited by qn, it can still be visited by qm, that's when the flag will be == 3 and we return True
        for vertex in n.adjacent:
            if ht[vertex.data] != 2:
                qn.append(vertex) # Hasn't been visited

        for vertex in m.adjacent:
            if ht[vertex.data] != 1:
                qm.append(vertex)

    return False


def route_between_nodes_ds(graph, node1, node2):
    R'''
    As explained in the comment in the function above, we will consider that we can change/update the data structure of the vertex node so as to have a flag property as well as visitedLeft and visitedRight properties.
    '''
    n = node1
    m = node2

    if not graph:
        return False

    if not n or not m or n == m:
        return True

    qn = Collections.deque()
    qm = Collections.deque()

    qn.append(n)
    qm.append(m)

    while qn or qm:
        n = qn.popleft()
        m = qn.popleft()

        n.flag ^= 1 << 1
        if n.flag == 3:
            return True
        m.flag ^= 1 << 0
        if m.flag == 3:
            return True

        for vertex in n.adjacent:
            if not vertex.visitedLeft:
                qn.append(vertex) # Hasn't been visited

        for vertex in m.adjacent:
            if not vertex.visitedRight:
                qm.append(vertex)

    return False
