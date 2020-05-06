# This program stores people's favorite numbers, and displays them.
favorite_numbers = {'ricky': [3, 11, 19, 23, 42],
                    'martin': [2, 4, 5],
                    'billie': [5, 35, 120],
                    }

# Display each person's favorite numbers.
for name in favorite_numbers:
    print("\n%s's favorite numbers are:" % name.title())
    
    # Each value is itself a list, so let's put that list in a variable.
    current_favorite_numbers = favorite_numbers[name]
    for favorite_number in current_favorite_numbers:
        print(favorite_number)  


===============
letter_counts = {}
for letter in "Mississippi":
    letter_counts[letter] = letter_counts.get(letter,0) +1
print(letter_counts)

================

dict = {}
dict[1] = 2
dict['1'] = 4
dict[1] += 2
count = 0

for key in dict:
    count += dict[key]

print(count)