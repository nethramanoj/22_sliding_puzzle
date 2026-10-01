
import random


class Puzzle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.make_board()

    def make_board(self):
        # Start with the solved arrangement
        tiles = list(range(1, self.size * self.size)) + [0]
        board = [
            tiles[r * self.size:(r + 1) * self.size]
            for r in range(self.size)
        ]

        # Scramble by making legal moves of the blank
        r, c = self.size - 1, self.size - 1
        previous_blank = None

        for _ in range(100 * self.size * self.size):
            possible_moves = []

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < self.size and 0 <= nc < self.size:
                    # Avoid immediately reversing the last move
                    if (nr, nc) != previous_blank:
                        possible_moves.append((nr, nc))

            if not possible_moves:
                break

            nr, nc = random.choice(possible_moves)

            # Move the adjacent tile into the blank
            board[r][c], board[nr][nc] = board[nr][nc], board[r][c]

            previous_blank = (r, c)
            r, c = nr, nc

        return board

    def blank_pos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c

    def move(self, direction):
        directions = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1)
        }

        if direction not in directions:
            return False

        r, c = self.blank_pos()
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < self.size and 0 <= nc < self.size):
            return False

        self.board[r][c], self.board[nr][nc] = (
            self.board[nr][nc], self.board[r][c]
        )
        return True
    def solved(self):
        return sum(self.board, []) == (
            list(range(1, self.size * self.size)) + [0]
        )