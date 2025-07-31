import random

def simulate_dice_rolls(trials=10000):
    count_sum_7 = 0
    count_sum_2 = 0
    count_sum_gt_10 = 0

    for _ in range(trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        if total == 7:
            count_sum_7 += 1
        if total == 2:
            count_sum_2 += 1
        if total > 10:
            count_sum_gt_10 += 1

    prob_7 = count_sum_7 / trials
    prob_2 = count_sum_2 / trials
    prob_gt_10 = count_sum_gt_10 / trials

    print(f"Probability of sum == 7: {prob_7:.4f}")
    print(f"Probability of sum == 2: {prob_2:.4f}")
    print(f"Probability of sum > 10: {prob_gt_10:.4f}")
