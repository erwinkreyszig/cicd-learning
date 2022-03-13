# -*- coding: utf-8 -*-
"""make a janken program (vs a 'computer' <- randomize the computer's attempts),
 whoever wins three times is the winner"""
from random import randint


def janken(computer, player):
    if computer == "gu":
        if player == "gu":
            return "Even"
        if player == "choki":
            return "You lose"
        if player == "pa":
            return "You win"
    if computer == "choki":
        if player == "gu":
            return "You win"
        if player == "choki":
            return "Even"
        if player == "pa":
            return "You lose"
    if computer == "pa":
        if player == "gu":
            return "You lose"
        if player == "choki":
            return "You win"
        if player == "pa":
            return "Even"

def computer_attack_chance():
    computer_attack = randint(1, 3)
    if computer_attack == 1:
        return "gu"
    if computer_attack == 2:
        return "choki"
    if computer_attack == 3:
        return "pa"

def winner_counter():
    player_win_counter = 0
    computer_win_counter = 0
    while player_win_counter < 3 and computer_win_counter < 3:
        cpu = computer_attack_chance()
        player_hand = input("What's your hand? (rock: 'gu', scissors: 'choki', paper: 'pa'")
        if janken(cpu, player_hand) == "You win":
            player_win_counter += 1
            print(cpu, player_hand)
        if janken(cpu, player_hand) == "You lose":
            computer_win_counter += 1
            print(cpu, player_hand)
    if player_win_counter == 3:
        return "The winner is the player."
    else:
        return "The winner is the computer."


if __name__ == '__main__':
    # test1
    print(winner_counter())
    #assert janken(computer_attack_chance(), player_hand) == ("You win")
            