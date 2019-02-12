from sys import stdin

starting_recipes = [3,7]
recipes = []
for c in starting_recipes:
    recipes.append(int(c))

i = 0
j = 1

goal = [int(x) for x in stdin.readline().rstrip()]
while recipes[-len(goal):] != goal and recipes[-len(goal) - 1:-1] != goal:
    combined = recipes[i] + recipes[j]

    if combined >= 10:
        recipes.append(1)
        recipes.append(combined - 10)
    else:
        recipes.append(combined)
    
    i = (i + recipes[i] + 1) % len(recipes)
    j = (j + recipes[j] + 1) % len(recipes)

print(len(recipes) - (len(goal) if recipes[-len(goal):] == goal else len(goal) + 1))
