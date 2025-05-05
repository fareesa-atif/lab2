
#---------------------------------------
#  Game Mechanics
#    Student A (team lead)
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    #------------------------
    print ("Welcome to Trivia Trek!")
    #------------------------
    
    #------------------------
#---------------------------------------
    
def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    #------------------------
    choice = int(input "Choose a category from 1 to 4: ")
    cat = ["1) Science", "2) history","3) pop culture","4) geography"]
    print (cat)
    if choice == 1:
        print("Science")
    elif choice == 2:
        print("History")
    elif choice == 3:
        print("Pop culture")
    elif choice == 4:
        print("Geography")

    #------------------------
    # raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    #------------------------
    print (f"Your score is {score}")
    print (f"Round number is {round_number}")
    #------------------------
    # raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------
    
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    #------------------------
    print (f"Game over! Your final score is {final_score}")

    #------------------------
    # raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    #------------------------
    score = 0
    round_number = 1
    incorrect_answers = 0
    allowed_skips = 2 # For skip_question()

    selected_category = choose_category(categories)

    while round_number <= 5:
        question, correct_answer = select_random_question(selected_category)
        print(f"\nQuestion: {question}")


    want_to_skip = input("Do you want to skip this question? (yes/no): ").lower()
    if want_to_skip == "yes" and skip_question(allowed_skips):
        allowed_skips -= 1
        print("Question skipped!")
        round_number = next_round(round_number)

    continue

    player_answer = input("Your Answer: ")

    correct = validate_answer(player_answer, correct_answer)
    provide_feedback(correct)

    if correct:
        score = update_score(score, True)
    else:
        incorrect_answers += 1
    
    display_correct_answer(correct_answer)

    display_score(score, round_number)

    if check_game_over(incorrect_answers):
        break

    round_number = next_round(round_number)

    game_over_message(score)
    player_name = input("Enter your name for the leaderboard: ")
    save_score(player_name, score)
    leaderboard = load_top_scores()
    display_leaderboard(leaderboard)
    restart_or_exit()

#---------------------------------------

def validate_answer(player_answer, correct_answer):
"""
Validate the player's answer.
"""

    #------------------------
return player_answer.strip().lower() == correct_answer.strip().lower()

    # raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------
        
def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    #------------------------
    return player_answer.strip().lower() == correct_answer.strip().lower()
    #------------------------
    #raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    #------------------------
    return score + 10 if correct else score
    #------------------------
    # raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    #------------------------
    return current_round + 1

    #------------------------
    # raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    #------------------------
    return incorrect_answers >= 3
    #------------------------
    # raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    #------------------------
    choice = input("Would you like to play again? (yes/no): ").strip().lower()
    if choice == "yes":
        trivia_trek()
    else:
        print("Thanks for playing Trivia Trek!")
    #------------------------
    # raise NotImplementedError("This function is not implemented yet.")
    #------------------------
    if __name__ == "__main__":
        trivia_trek()

#---------------------------------------
