import itertools			# Package to calculate all possible number combinations from list

def calculate_prize(matches, powerball_drawn):
    division_prizes_with_powerball = {
        7: "Division 1",
        6: "Division 3",
        5: "Division 5",
        4: "Division 6",
        3: "Division 8",
        2: "Division 9"
    }
    division_prizes_no_powerball = {
        7: "Division 2",
        6: "Division 4",
        5: "Division 7",
    }
    if powerball_drawn:
        return division_prizes_with_powerball.get(matches, "no prize")
    else:
        return division_prizes_no_powerball.get(matches, "no prize")
         
def result(name, ticket):
    # Initialize game number
    game_number = 1
    
    # Iterate over each game of player's ticket
    for game, powerball_drawn in ticket.items():
        # Determine how many matching numbers
        matches = len(set(game) & set(winning_numbers))
        match_numbers = sorted(set(game) & set(winning_numbers))
        
        if powerball_drawn == powerball:
            division_prize = calculate_prize(matches, True)
            print(f"{name} wins {division_prize} on game {game_number} with matches {', '.join(map(str, match_numbers))} for ticket numbers {', '.join(map(str, game))}. You drew the Powerball.")
        else:
            division_prize = calculate_prize(matches, False)
            print(f"{name} wins {division_prize} on game {game_number} with matches {', '.join(map(str, match_numbers))} for ticket numbers {', '.join(map(str, game))}. No powerball was drawn.")
        # Increment game number
        game_number += 1
        
    print(" ")
    
## Winning numbers array
winning_numbers = [7, 22, 24, 31, 33, 40, 50]
powerball = 2

## Store Mary games as a dictionary where each key is a tuple representing the main numbers and the value is the powerball number
mary_ticket = {
    (2, 22, 13, 24, 32, 39, 70): 5,
    (7, 22, 24, 31, 33, 40, 50): 2,
    (3, 7, 18, 21, 37, 38, 45): 8
}

john_ticket = {
        (7, 9, 13, 24, 33, 40): 2,
        (16, 19, 22, 29, 31, 39): 2,
        (1, 7, 18, 22, 30, 36): 7
}

result("Mary", mary_ticket)
result("John", john_ticket)

jack_ticket = {
        (3, 5, 7, 11, 22, 24, 31, 34, 40): 2,
}

## Uses the itertools library to find all possible combinations
def game_combinations(numbers, r):
    return list(itertools.combinations(numbers, r))

# List of all possible 6 number combinations for jack's system ticket
jack_games = game_combinations(next(iter(jack_ticket.keys())), 6)  # Extract the key as a tuple

result("Jack", {jack_game: jack_ticket[next(iter(jack_ticket.keys()))] for jack_game in jack_games})  # Pass the extracted key and powerball value