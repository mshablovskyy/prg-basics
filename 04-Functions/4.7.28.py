def f(dice):
        max_count = 1
        max_digit = dice[0]
        current_count = 1
        
        for i in range(0, len(dice)):
            if dice[i] == dice[i - 1]:
                current_count += 1
            else:
                if current_count > max_count:
                    max_digit = dice[i-1]
                    max_count = current_count
                current_count = 1
        
        if current_count > max_count:
            max_digit = dice[i-1]
        
        return max_digit
        
print(f("5233165554211"))