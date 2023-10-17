import itertools

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
    
## Return amount of matching numbers that overlap via sets, which are the winning numbers for the ticket
def count_winningNumbers(game, winning_numbers):
    return len(set(game) & set(winning_numbers))

# Return the matching numbers, that are the winning numbers for the ticket
def matching_numbers(game, winning_numbers):
    return set(game) & set(winning_numbers)

## Determine division prize depending on amount of winning numbers
def calculate_prize(matches):
    if matches == 6:
        return "Division 1"
    elif matches == 5:
        return "Division 2"
    elif matches == 4:
        return "Division 3"
    elif matches == 3:
        return "Division 4"
    else:
        return "no prize"

# Results output
def result(name, ticket):
    ## Iterate over each game of player's ticket
    for index, game in enumerate(ticket):
            ## Determine how many matching numbers
            matches = count_winningNumbers(game, winning_numbers)
            ## Determine if there is a div prize and what type 
            division_prize = calculate_prize(matches)
            ## Determine what are the matching numbers
            match_numbers = matching_numbers(game, winning_numbers)
            
            print(f"{name} wins {division_prize} on game #{index + 1} with matches {match_numbers} for ticket numbers {game}")

result("John", john_ticket)
print(" ")
result("Mary", mary_ticket)
print(" ")

###### ADDITIONAL CHALLENGE ######

## Uses the itertools library to find all possible combinations
def game_combinations(numbers, r):
    return list(itertools.combinations(numbers, r))

## List of all possible 6 number combinations for jack's system ticket
jack_games = game_combinations(jack_systemTicket, 6)

result("Jack", jack_games)











