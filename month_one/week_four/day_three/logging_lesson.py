import logging
from typing import Optional
import random

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

def compare_game_scores(computer_score: int, user_score: int, name) -> Optional[str]:
    '''compares two scores, returns the higher one if equal return string "DRAW"'''
    logging.info(f"Match scores recieved. Computer: {computer_score}, User: {user_score}")
    try:
        if computer_score > user_score:
            return f"Computer wins! {computer_score} > {user_score}"
        elif computer_score == user_score:
            return "DRAW!"
        else:
            return f"{name} wins! {user_score} > {computer_score}"
    except Exception as e:
        logging.error(f"Error occured: {e}")
        
def simulate_rounds(rounds: int = 3) -> Optional[int]:
    '''Returns computers score first, then users'''
    variations = ["rock", "papper", "scissors"]
    computer_score = 0
    user_score = 0
    try:
        for _ in range(rounds):
            user_sign = input("rock, paper or scissors?\n")
            random_sign = random.choice(variations)
            if user_sign == random_sign:
                continue
            elif user_sign == "paper" and random_sign == "rock":
                user_score += 1
            elif user_sign == "paper" and random_sign == "scissors":
                computer_score += 1
            elif user_sign == "rock" and random_sign == "paper":
                computer_score += 1
            elif user_sign == "rock" and random_sign == "scissors":
                user_score += 1
            elif user_sign == "scissors" and random_sign == "rock":
                computer_score += 1
            elif user_sign == "scissors" and random_sign == "papper":
                user_score += 1
        return computer_score, user_score
    except Exception as e:
        logging.error(f"Error recieved: {e}")

def rock_papper_scissors(user_name: str, rounds: int=None) -> Optional[str]:
    '''default rounds == 3'''
    logging.info(f"Info received: rounds = {rounds} name = {user_name}")
    try:
        if rounds == None:
            computer_score, user_score = simulate_rounds()
        else:
            computer_score, user_score = simulate_rounds(rounds)
        result = compare_game_scores(computer_score, user_score, user_name)
        return result
    except Exception as e:
        logging.error(f"Error occured: {e}")

