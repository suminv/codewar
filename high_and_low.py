def high_and_low(numbers):
    """In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number."""
    test_list = sorted(list(map(int, numbers.split())))
    last = test_list[-1]
    first = test_list[0]

    return f"{last} {first}"


assert (high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")) == "42 -9"
