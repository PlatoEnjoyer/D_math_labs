cache_part1 = {}

def count_paths_part1(x, y, target_x, target_y):
    if x == target_x and y == target_y:
        return 1
    if x > target_x or y > target_y:
        return 0

    key = (x, y)
    if key in cache_part1:
        return cache_part1[key]

    ways_right = count_paths_part1(x + 1, y, target_x, target_y)
    ways_up    = count_paths_part1(x, y + 1, target_x, target_y)

    total_ways = ways_right + ways_up

    cache_part1[key] = total_ways
    return total_ways

target_x = 19
target_y = 16
result1 = count_paths_part1(0, 0, target_x, target_y)
print(result1)



cache_part2 = {}

def count_paths_part2(x, y, target_x, target_y, last_was_up):
    if x == target_x and y == target_y:
        return 1
    if x > target_x or y > target_y:
        return 0

    key = (x, y, last_was_up)
    if key in cache_part2:
        return cache_part2[key]

    total = 0

    total += count_paths_part2(x + 1, y, target_x, target_y, False)

    if not last_was_up:
        total += count_paths_part2(x, y + 1, target_x, target_y, True)

    cache_part2[key] = total
    return total

target_x = 19
target_y = 16
result2 = count_paths_part2(0, 0, target_x, target_y, False)
print(result2)