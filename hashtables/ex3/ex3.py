def intersection(arrays):
    # add all occurrences for every number
    cache = {}

    for arr in arrays:
        for num in arr:
            if num in cache:
                cache[num] += 1
            else:
                cache[num] = 1

    # only the items have an occurrence will be returned
    # if values occur array length times, it means that int is in all arrays
    return [item[0] for item in cache.items() if item[1] == len(arrays)]



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))