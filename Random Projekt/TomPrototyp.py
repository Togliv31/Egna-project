game = [[{"Öppna" : 2}, {"Stäng" : 1}, {"Vänta": 3}], [], [], []]

for i in range(len(game)):
    for e in range(len(game[i])):
        print(f"{e+1}. {game[i][e].keys()}")
    answer = input().capitalize()
    