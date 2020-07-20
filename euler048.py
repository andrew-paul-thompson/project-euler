def self_power_series(n):
    return sum([n ** n for n in range(1, n + 1)])


print(str(self_power_series(1000))[-10:])
