def isStochastic(P):
    nb_lines = len(P)
    nb_columns = len(P[0])
    if nb_lines != nb_columns:
        return False
    for line in P:
        for number in line:
            if number > 1 or number < 0:
                return False
    return True


def isBistochastic(P):
    for line in P:
        if sum(line) != 1:
            return False
    for i in range(len(P)):
        s = 0
        for j in range(len(P)):
            s += P[j][i]
        if s == 1:
            return False
    return True

# if G*h = h then h is a stable vector
def stableVector(G, h):
    # to multiply, nb of columns of G must = nb of rows of h 
    if len(G[0]) != len(h):
        return False
    
    column_values = [h[i][0] for i in range(len(h))]
    # print(column_values)
    resulting_vector = []
    for line in G:
        value = 0
        for i in range(len(line)):
            value += (line[i] * column_values[i])
        resulting_vector.append(value)
    if resulting_vector == column_values:
        return True
    else: 
        return False

    




vector = [
        [.5,.2,.3],
        [.2,.1,.7],
        [.7,.1,.2]]

print(f"The matrix is{' not' if not isStochastic(vector) else ''} Stochastic")
print(f"The matrix is{' not' if not isBistochastic(vector) else ''} Bistochastic")

h = [
    [1/3],
    [1/3],
    [1/3]]

print(f"The vector h is{' not' if not stableVector(vector, h) else ''} stable")

