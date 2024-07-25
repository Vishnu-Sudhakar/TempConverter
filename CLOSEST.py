# Step 1: Input the number of guesses
n = int(input("Enter the number of guesses: "))

# Step 2: Input the guesses and store them in a list
guesses = []
for i in range(n):
    guess = float(input(f"Enter guess number {i+1}: "))
    guesses.append(guess)

# Step 3: Input the price tag of the item
price_tag = float(input("Enter the price tag of the item: "))

# Step 4: Calculate differences between each guess and the price tag
differences = [abs(guess - price_tag) for guess in guesses]

# Step 5: Find the minimum and maximum differences
min_difference = min(differences)
max_difference = max(differences)

# Step 6: Find all guesses that have the minimum difference
closest_guesses = [guess for guess, diff in zip(guesses, differences) if diff == min_difference]

# Step 7: Find the guess that has the maximum difference
furthest_guess = guesses[differences.index(max_difference)]

# Step 8: Count how many times the closest guess appears
closest_guess_count = closest_guesses.count(closest_guesses[0])  # All elements in closest_guesses will be the same

# Step 9: Print the closest guess, its count, and the furthest guess
print(f"The closest guess to the price tag is: {closest_guesses[0]}")
print(f"The number of times this closest guess appears is: {closest_guess_count}")
print(f"The furthest guess from the price tag is: {furthest_guess}")
