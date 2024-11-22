WHITE = 1
BLACK = 0

# Piece class
class Piece:
    def __init__(self, name: str, position: tuple[int, int], colour: int):
        self.name = name
        self.position = position
        self.colour = colour

    def get_name(self) -> str:
        return self.name
    
    def get_position(self) -> tuple[int, int]:
        return self.position
    
    def get_colour(self) -> int:
        return self.colour
    
    def change_position(self, new_position: tuple[int, int]):
        self.position = new_position

# The logic behind the controller
class Move:
    def __init__(self, piece, start, end, captured=None, special=None):
        self.piece = piece
        self.start = start
        self.end = end
        self.captured = captured
        self.special = special

    def get_piece(self):
        return self.piece
    
    def get_start(self):
        return self.start
    
    def get_end(self):
        return self.end
    
    def get_captured(self):
        return self.captured
    
    def get_special(self):
        return self.special

# The controller that controls Move and GUI
class Chess():
    def __init__(self):
        self.move_history = []
        self.turn = "white"

    def play(self):
        return
    
    def make_move(self, piece, start, end, captured=None, special=None):
        move = Move(piece, start, end, captured, special)
        self.move_history.append(move)

    def undo_move(self):
        if self.move_history:
            last_move = self.move_history.pop()
            self.revert_move(last_move)

    def revert_move(self, last_move: Move):
        last_move.piece.position = last_move.start

def main():
    chess = Chess()
    chess.play()

if __name__ == "__main__":
    main()