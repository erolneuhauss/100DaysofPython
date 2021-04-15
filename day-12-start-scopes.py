#!/usr/bin/env python
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

drink_potion()
print(player_health)

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    drink_potion()

print(player_health)

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)

print(" 1. Cell ".center(30, '-'))
enemies = 1
print(enemies)
def increase_enemies():
    global enemies
    enemies += 1

print(" 2. Cell ".center(30, '-'))
increase_enemies()

print(" 3. Cell ".center(30, '-'))
enemies = increase_enemies()
print(enemies)

print(" 4. Cell ".center(30, '-'))
def increase_enemies():
    return enemies + 1

print(enemies)
