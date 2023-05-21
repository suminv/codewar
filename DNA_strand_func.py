def DNA_strand(dna):
    result = ""
    if len(dna) == 0:
        return result
    else:
        for i in dna:
            if i == "A":
                result += "T"
            elif i == "T":
                result += "A"
            elif i == "C":
                result += "G"
            elif i == "G":
                result += "C"
        return result


assert (DNA_strand("AAAA")) == "TTTT"
assert (DNA_strand("ATTGC")) == "TAACG"
assert (DNA_strand("GTAT")) == "CATA"
assert (DNA_strand("AAGG")) == "TTCC"
assert (DNA_strand("CGCG")) == "GCGC"
assert (DNA_strand("ATTGC")) == "TAACG"
