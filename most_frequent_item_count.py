def most_frequent_item_count(collection: list):
    if collection:
        return max([collection.count(item) for item in collection])
    return 0


print("Starting tests for most_frequent_item_count...")

assert most_frequent_item_count([3, -1, -1]) == 2
assert most_frequent_item_count([]) == 0
assert most_frequent_item_count([3]) == 1

print("All test cases passed successfully!")
