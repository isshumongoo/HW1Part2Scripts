import math
from scipy.stats import binom

def max_simultaneous_users(total_bandwidth, user_bandwidth):
    return int(total_bandwidth / user_bandwidth)

def prob_no_users(num_users, access_prob):
    return (1 - access_prob) ** num_users

def prob_one_particular_user(access_prob):
    return access_prob

def prob_exactly_one_user(num_users, access_prob):
    return num_users * access_prob * (1 - access_prob) ** (num_users - 1)

def prob_two_particular_users(access_prob):
    return access_prob ** 2

def prob_exactly_two_users(num_users, access_prob):
    return math.comb(num_users, 2) * access_prob**2 * (1 - access_prob)**(num_users - 2)

def prob_at_least_n_users(num_users, n, access_prob):
    return 1 - sum(binom.pmf(k, num_users, access_prob) for k in range(n))

def max_users_for_congestion_free(target_prob, max_simultaneous, access_prob):
    def prob_congestion(n, k):
        return 1 - sum(binom.pmf(i, n, access_prob) for i in range(k))
    
    n = max_simultaneous  # Start from the minimum possible number of users
    while True:
        congestion_prob = prob_congestion(n, max_simultaneous + 1)
        if congestion_prob > 1 - target_prob:
            return n - 1  # Return the last valid number of users
        n += 1

def main():
    total_bandwidth = 170  # Mbps
    user_bandwidth = 9.4   # Mbps
    access_prob = 0.1      # 10%

    # 1. Max simultaneous users
    max_users = max_simultaneous_users(total_bandwidth, user_bandwidth)

    # 2. Probabilities with 28 users
    num_users = 28
    p_no_users = prob_no_users(num_users, access_prob)
    p_one_particular = prob_one_particular_user(access_prob)
    p_exactly_one = prob_exactly_one_user(num_users, access_prob)
    p_two_particular = prob_two_particular_users(access_prob)
    p_exactly_two = prob_exactly_two_users(num_users, access_prob)

    # 3. Probability of at least N users out of 150
    p_at_least_n = prob_at_least_n_users(150, max_users + 1, access_prob)

    # 4. Max users for 99.99% congestion-free time
    max_subscribed_users = max_users_for_congestion_free(0.9999, max_users, access_prob)

    # Format and print the answer string
    answer = f"{max_users}, {p_no_users:.5f}, {p_one_particular:.5f}, {p_exactly_one:.5f}, " \
             f"{p_two_particular:.5f}, {p_exactly_two:.5f}, {p_at_least_n:.5f}, {max_subscribed_users}"
    print(answer)

if __name__ == "__main__":
    main()