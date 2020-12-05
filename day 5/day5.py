passes = [line.strip() for line in open("input.txt").readlines()]


def seat_id(row: int, seat: int):
    return (row * 8) + seat


def recursive_search(commands: str, potential_answers: range) -> int:
    if len(potential_answers) == 1:
        return potential_answers[0]
    else:
        midpoint = int(len(potential_answers)/2)
        if commands[0] in ("F", "L"):
            return recursive_search(commands[1:], potential_answers[:midpoint])
        elif commands[0] in ("B", "R"):
            return recursive_search(commands[1:], potential_answers[midpoint:])


# part 1 answer 866
all_seat_ids = {seat_id(recursive_search(boarding[:7], range(128)), recursive_search(boarding[7:], range(8))) for boarding in passes}

print(max(all_seat_ids))

# part 2, answer 583
all_possible_seats = {(row, column) for row in range(128) for column in range(8)}
for potential in all_possible_seats:
    seat = seat_id(*potential)
    if seat not in all_seat_ids and seat + 1 in all_seat_ids and seat -1 in all_seat_ids:
        print(seat)
