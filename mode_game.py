from random import randint
import players_actions
import map_game


class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = players_actions.AI(co, pl)
        self.us = players_actions.User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = map_game.Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = map_game.Ship(map_game.Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except map_game.BoardWrongShipException:
                    pass
        board.begin()
        return board

    def greet(self):
        print("————")
        print(" █ █ █ █ █ █ █ █ █ █ █")
        print(" █       Добро       █")
        print(" █     пожаловать    █")
        print(" █   в морской бой   █")
        print(" █ █ █ █ █ █ █ █ █ █ █")
        print(" █ формат ввода: x y █")
        print(" █ x - номер строки  █")
        print(" █ y - номер столбца █")
        print(" █ █ █ █ █ █ █ █ █ █ █")

    def loop(self):
        num = 0
        while True:
            print("—" * 27)
            print("Поле пользователя:")
            print(self.us.board)
            print("—" * 27)
            print("Поле противника:")
            print(self.ai.board)
            if num % 2 == 0:
                print("—" * 27)
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("—" * 27)
                print("Ходит противник!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("—" * 20)
                print("Пользователь выиграл!")
                break

            if self.us.board.count == 7:
                print("—" * 20)
                print("Противник выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()
