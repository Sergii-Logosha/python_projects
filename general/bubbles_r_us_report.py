# Sergii Logosha, 09 Jul 2022

# The program creates a report for Bubble-R-Us company (task from book Head First "Learn to Code"

scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .25, .33, .31, .25, .29, .27, .22, .31, .25, .25, .33, .21, .25,
         .25, .25, .28, .25, .24, .22, .20, .25, .30, .25, .24, .25, .25, .25, .27, .25, .26, .29]

length = len(scores)
high_score = 0
for i in range(length):
    print(f"Bubble solution #{i} score: {scores[i]}")
    if scores[i] > high_score:
        high_score = scores[i]

print(f"Bubbles tests: {length}")
print(f"Highest bubble score: {high_score}")

best_solutions = []

for i in range(length):
    if scores[i] == high_score:
        best_solutions.append(i)

print(f"Solutions with highest scores: {best_solutions}")

most_effective = 0
effective_cost = 100.0
for i in range(length):
    if scores[i] == high_score and costs[i] < effective_cost:
        effective_cost = costs[i]
        most_effective = i

print(f"Solution #{most_effective} is the most effective with the cost of ${effective_cost}.")
