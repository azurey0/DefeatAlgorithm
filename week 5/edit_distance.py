# Uses python3
import numpy as np
def edit_distance(s, t):
    rows = len(s) + 1
    cols = len(t) + 1
    D = np.zeros([rows,cols], dtype = int)
    D[0] = np.arange(cols)
    D[:,0] = np.arange(rows)

    for i in range(1, cols):
        for j in range(1, rows):
            # print(D[i,j])
            insertion = D[j, i-1] + 1
            deletion = D[j-1, i] + 1
            match = D[j-1, i-1]
            mismatch = D[j-1, i-1] + 1
            if s[j - 1] == t[i - 1]:
                D[j, i] = min(insertion, deletion, match)
            else:
                D[j, i] = min(insertion, deletion, mismatch)
    # print(D)
    return D[len(s), len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance('short', 'ports'))
