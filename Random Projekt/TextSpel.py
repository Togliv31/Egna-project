"""
Det här spelet fungerar så att du kommer att möta olika fiender. Du kan göra tre saker varje tur.
Du får välja mellan "anfall" eller "försvar". Fienden kan också göra tre saker på sin tur,
men vad som väljs för den är random.
"""

import random
player_hp = 10
player_damage = 0
player_shield = 0
enemy_hp = 10
enemy_damage = 0
enemy_shield = 0

print("Du vaknar upp i en grotta.\nDu blinkar, men det är väldigt mörkt, det enda du kan se är skelett bredvid dig, och du hör ett morrande från andra sidan grottan.\nEn varg står där, redo att anfalla. Du drar din dolk.")

while True:
    for i in range(3):
        move = input("Vad gör du?\n").lower()
        if move == "anfall":
            player_damage += 3
        elif move == "försvar":
            player_shield += 1
        else:
            print("Nåt annat, i den här situationen?!")
    for i in range(3):
        x = random.randint(0,2)
        if x <= 1:
            enemy_damage += 2
        else:
            enemy_shield += 2
    
    if player_damage > enemy_shield:
        enemy_hp -= (player_damage - enemy_shield)
        print(f"Vargen tar {player_damage - enemy_shield} skada!")
    
    if enemy_hp <= 0:
        print("Du besegrade vargen!")
        break
    
    if enemy_damage > player_shield:
        player_hp -= (enemy_damage - player_shield)
        print(f"Du tar {enemy_damage - player_shield} skada. Du har bara {player_hp} hp kvar!")

    if player_hp <= 0:
        print("Vargen besegrade dig!")
        break

    player_damage = 0
    player_shield = 0
    enemy_damage = 0
    enemy_shield = 0