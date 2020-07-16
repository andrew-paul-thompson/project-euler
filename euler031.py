coins = [200, 100, 50, 20, 10, 5, 2, 1]


def ways_to_make_change(curr_money, denomination=0):
    ways = 0
    loops = curr_money // coins[denomination] + 1
    for i in range(loops):
        if curr_money - coins[denomination] * i == 0:
            ways += 1
        elif denomination < len(coins) - 1:
            ways += ways_to_make_change(curr_money - coins[denomination] * i, denomination + 1)
    return ways


total_ways = ways_to_make_change(200)
print(total_ways)
