# -*- coding = utf - 8 -*-
# -*- coding: utf-8 -*-

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {i:j for i,j in zip(letters, points)}

print(letter_to_points)

letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for i in word.upper():
    if i in letter_to_points:
      point_total += letter_to_points[i]
  return point_total

brownie_points = score_word("brownie")

print(brownie_points)

player_to_word = {
					"player1": ["BLUE", "TENNIS", "EXIT"],
					"wordNerd": ["EARTH", "EYES", "MACHINE"],
					"Lexi Con": ["ERASER", "BELLY", "HUSKY"],
					"Prof Reader": ["ZAP", "COMA", "PERIOD"]
	}

player_to_points = {}

for player, words in player_to_word.items():    
    player_points = 0
    for i in words:
      player_points += score_word(i)
    player_to_points[player] = player_points
      
print(player_to_points)

def play_word(player, word):
  player_to_word[player].append(word) 
    
play_word("Lexi Con", "GOLF")
print(player_to_word)

def update_point_totals():
  player_to_points = {}
  for player, words in player_to_word.items():    
    player_points = 0
    for i in words:
      player_points += score_word(i)
    player_to_points[player] = player_points
  return player_to_points

print(update_point_totals())   
	
input("> ")
