def dna_shingle(dna, k):
    shingles = []
    for i in range(len(dna)-k+1):
        shingles.append(dna[i:i+k])
    shingles = list(set(shingles))
    return shingles

def shingle2decimal(shingle):
    d = 0
    cmap = {}
    cmap['A'] = 0
    cmap['C'] = 1
    cmap['G'] = 2
    cmap['T'] = 3
    for i in range(len(shingle)):
        d = d*4 + cmap[shingle[i]]
    return d

def get_vector(dna,k):
    ss = dna_shingle(dna,k)
    v = [0]*(4**k)
    for s in ss:
        val = shingle2decimal(s)
        v[val] = 1
    return v

def minhash_dna(permutation, dna, k):
    v = get_vector(dna,k)
    for i in range(len(permutation)):
        if v[permutation[i]] == 1:
            return permutation[i]
