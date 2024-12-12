# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    res = 0
    for row in seats:
        res += len(row)
    return res

def check_seats(seats, argument):
    num = 0
    for row in seats:
        for item in row:
            if item == argument:
                num += 1
    return num
    
def seats_available(seats):
    return check_seats(seats, "A")

def seats_booked(seats):
    return check_seats(seats, "B")

def seat_status(seats, row, place):
    if seats[row - 1][place - 1] == "A":
        return "Available"
    elif seats[row - 1][place - 1] == "B":
        return "Booked"

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))