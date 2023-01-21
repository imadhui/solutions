def get_index_of_parent(child_index):
    if child_index == 0: return 0
    if child_index%2 == 0:
        return int((child_index-2)/2)
    else:
        return int((child_index-1)/2)

def bubble_up(i, H):
    p = get_index_of_parent(i)
    while(H[p] > H[i]):
        H[i], H[p] = H[p], H[i]
        i = p
        p = get_index_of_parent(i)
    return H

def bubble_down(i, H):
    last_index = len(H)-1
    if 2*i+2 <= last_index:
        lc,rc = H[2*i+1], H[2*i+2]
    elif 2*i+1 <= last_index:
        lc, rc = H[2*i+1], H[i]+1
    else:
        lc = rc = H[i]+1
    #print(f"bubble_down: i: {i}, H: {H}, H[i]: {H[i]}, lc: {lc}, rc: {rc}")
    if H[i] > lc or H[i] > rc:
        min_index = 2*i+1 if lc < rc else 2*i+2
        H[i], H[min_child] = H[min_child], H[i]
        return bubble_down(min_child, H)
    else:
        return H

def insert(element, H):
    H.append(element)
    length = len(H)
    last_index = length-1
    index_of_parent = get_index_of_parent(last_index)
    if H[index_of_parent] <= H[last_index]:
        return H
    else:
        return bubble_up(last_index, H)

def extract_min(H):
    last_index = len(H)-1
    min = H[0]
    H[0] = H[last_index]
    H.pop()
    return bubble_down(0, H) if H != [] else H

def minHeap(N, Q):
    H = []
    extract = None
    for query in Q:
        if query[0] == 0:
            insert(query[1], H)
            print(f"After inserting {query[1]}: {H}")
        else:
            extract = H[0]
            extract_min(H)
            print(f"After extracting min: {H}")
    return extract


Q1 = [[0,2],[0,1],[1]]
Q2 = [[0,1],[1]]
Q3 = [[0,5], [1],[0,43],[0,15],[0,5]]
Q4 = [[0,4],[1]]
queries = Q4
print(minHeap(len(queries), queries))




