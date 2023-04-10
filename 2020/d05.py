from lib.mylib import loadData


def decode(code):
    rows, cols = list(range(128)), list(range(8))

    for c in code:
        if c == 'F':
            rows = rows[:len(rows) // 2]
        elif c == 'B':
            rows = rows[len(rows) // 2:]
        elif c == 'R':
            cols = cols[len(cols) // 2:]
        elif c == 'L':
            cols = cols[:len(cols) // 2]
    return rows[0] * 8 + cols[0]


class Seat:
    def __init__(self, code):
        self.__code = code

    def get_id(self):
        return decode(self.__code)


def main():
    seats = list(map(Seat, loadData().split('\n')))

    seat_ids = list(map(Seat.get_id, seats))

    print("\nPart 1")
    max_id = max(seat_ids)
    print(max_id)

    print("\nPart 2")
    min_id = min(seat_ids)
    my_seat, = set(range(min_id, max_id + 1)) - set(sorted(seat_ids))
    print(my_seat)


if __name__ == "__main__":
    main()
