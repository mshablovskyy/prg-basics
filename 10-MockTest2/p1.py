def f(player1, player2):
    v10 = ("A", "K", "Q", "J", "T")
    players = [player1, player2]
    scores = [0, 0]
    
    for i in range(2):
        for player in players[i]:
            for letter in player:
                if letter in v10:
                    scores[i] += 10
                else:
                    scores[i] += int(letter)
    
    if scores[0] >= scores[1]:
        return True
    else: return False
    
if __name__ == "__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))