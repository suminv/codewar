def count_red_beads(n):
    if n < 2:
        return 0
    else:
        return 2 * (n - 1)


assert (count_red_beads(1)) == 0
assert (count_red_beads(3)) == 4
