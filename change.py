# A Question for returning the optimal amount of change
#   Given a number in the range 0-99 find the smallest collection of coins whose value is the number

# Greedy solution, adding coins one by one
def change_a(cents):
    """
    Make change for the given cents value.
    Coin values 25c, 10c, 5c, 1c
    Pre-conditions:
        :param cents: an integer
    Return: 
        a list of counts for the coins used.
    """
    coins = [25, 10, 5, 1]
    coin_index = 0
    counts = [0, 0, 0, 0]
    remaining = cents
    while remaining > 0:
        if coins[coin_index] <= remaining:
            counts[coin_index] += 1
            remaining -= coins[coin_index]
        else:
            coin_index += 1
    return counts


# Greedy solution, calculating each quantity of coins exactly
def change_b(cents):
    """
    Make change for the given cents value.
    Coin values of 25c, 10c, 5c, 1c
    Pre-conditions:
        :param cents: an integer
    Return: 
        a list of counts for the coins used.
    """
    coins = [25, 10, 5, 1]
    coin_index = 0
    counts = [0] * len(coins)
    remaining = cents
    while remaining > 0:
        counts[coin_index] = remaining // coins[coin_index]
        remaining = remaining % coins[coin_index]
        coin_index += 1
    return counts


# Brute force solution finding the smallest of all combinations of coins
def change_c(cents):
    """
    Make change for the given cents value.
    Coin values 25c, 10c, 5c, 1c
    :param cents: an integer
    :return: a list of counts for the coins used.
    """
    coins = [25, 10, 5, 1]

    def combinations(counts):
        """
        Cycle through every possible combination, looking
        for a combo that adds up to the right value, and 
        has the smallest number of coins
        :param counts: a 4-tuple
        :return: a pair (True, list) if list is the best 
                 combination
        """
        value = sum([counts[i] * v for i, v in enumerate(coins)])
        if value == cents:
            return True, counts
        elif value > cents:
            # don't add more coins to this combination because it's already too big
            return False, None
        else:
            (c0, c1, c2, c3) = counts
            # add 1 to each number of coins separately
            trying = [(c0 + 1, c1, c2, c3), (c0, c1, c2 + 1, c3),
                      (c0, c1 + 1, c2, c3), (c0, c1, c2, c3 + 1)]
            # try to find the best combination, by using the lowest number of coins
            best_size = 100
            best_counts = None
            for combo in trying:
                flagged, res = combinations(combo)
                if flagged and sum(res) < best_size:
                    best_size = sum(res)
                    best_counts = res
            if best_size == 100:
                # nothing worked!
                return False, None
            else:
                return True, best_counts
    flag, result = combinations((0, 0, 0, 0))
    if flag:
        return result
    else:
        return None


def display_change():
    print("\nQuestion 1: Make Change\n")
    examples = [0, 18, 39, 42, 50, 81, 92, 99]
    for e in examples:
        print('Greedy Algorithm 1:', e, change_a(e))
        print('Greedy Algorithm 2:', e, change_b(e))
        # print('Brute Force Algorithm:', e, change_c(e))
