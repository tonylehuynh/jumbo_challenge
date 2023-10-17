import itertools			# Package to calculate all possible number combinations from list

## Dictionary to determine division prize depending on amount of winning numbers
def calculate_prize(matches):
    division_prizes = {
        6: "Division 1",
        5: "Division 2",
        4: "Division 3",
        3: "Division 4"
    }
    # If amount of matching numbers is lower than 3, then "no prize"
    return division_prizes.get(matches, "no prize")

## Results output
def result(name, ticket):
    # Iterate over each game of player's ticket
    for index, game in enumerate(ticket):
            # Determine how many matching numbers
            matches = len(set(game) & set(winning_numbers))
            # Determine if there is a div prize and what type 
            division_prize = calculate_prize(matches)
            # Determine what are the matching numbers and sort in ascending order
            match_numbers = sorted(set(game) & set(winning_numbers))
            
			# Output results string
            print(f"{name} wins {division_prize} on game #{index + 1} with matches {', '.join(map(str, match_numbers))} for ticket numbers {', '.join(map(str, game))}")
    print(" ")

## Winning numbers array
winning_numbers = [7, 22, 24, 31, 33, 40]

## Store John and Mary games as arrays within a ticket array in order to later retrieve index (this will represent game number)
john_ticket = [
        [7, 9, 13, 24, 33, 40],
        [16, 19, 22, 29, 31, 39],
        [1, 7, 18, 22, 30, 36]
    ]

mary_ticket = [
        [2, 22, 13, 24, 32, 39],
        [7, 22, 24, 31, 33, 40],
        [3, 7, 18, 21, 37, 38]
    ]

jack_systemTicket = [3, 5, 7, 11, 22, 24, 31, 34, 40]

result("John", john_ticket)
result("Mary", mary_ticket)

###### ADDITIONAL CHALLENGE ######

## Uses the itertools library to find all possible combinations
def game_combinations(numbers, r):
    return list(itertools.combinations(numbers, r))

# List of all possible 6 number combinations for jack's system ticket
jack_games = game_combinations(jack_systemTicket, 6)

result("Jack", jack_games)










