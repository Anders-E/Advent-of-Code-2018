from sys import stdin

starting_recipes = [3,7]
recipes = []
for c in starting_recipes:
    recipes.append(int(c))

i = 0
j = 1

goal_length = int(stdin.readline()) + 10
while len(recipes) < goal_length:
    #print(recipes)
    combined = recipes[i] + recipes[j]
    combined = [int(x) for x in str(combined)]
    recipes += combined
    i = (i + recipes[i] + 1) % len(recipes)
    j = (j + recipes[j] + 1) % len(recipes)

scores = recipes[goal_length - 10: goal_length]
for x in scores:
    print(x, end='')
print()

