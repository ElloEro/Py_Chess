from typing import List

# Colour as int
WHITE = 1
BLACK = 0
# Piece Name
KNIGHT = "knight"
ROOK = "rook"
QUEEN = "queen"
KING = "king"
BISHOP = "bishop"
PAWN = "pawn"

# Piece class
class Piece():
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
    
    def print_colour(self) -> str:
        if self.colour:
            return WHITE
        return BLACK
    
    def change_position(self, new_position: tuple[int, int]):
        self.position = new_position
    
    def to_chess_notation(self) -> str:
        x, y = self.position
        file = chr(x + ord('a'))
        rank = (1 + y)
        return file + rank

    def __repr__(self) -> str:
        return "Piece({name}, {position}, {colour})\n".format(name=self.get_name(), position=self.get_position(), colour=self.get_colour())

    def __str__(self) -> str:
        return "{colour} {piece} is on {position}".format(colour=self.print_colour(), piece=self.get_name(), position=self.to_chess_notation())

# The logic behind the controller
class Move():
    def __init__(self, piece: Piece, start, end, captured=None, special=None):
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
    
    def change_piece_position(self, new_position: tuple[int, int]):
        self.piece.change_position(new_position)

# The controller that controls Move and GUI
class Chess():
    def __init__(self):
        self.move_history = []
        self.pieces = self.setup()
        self.turn = "white"

    def play(self):
        print(self.move_history)
        print(self.pieces)
        return
    
    """
        Hard coded the pieces in to make it more easily readable and understandable
    """
    def setup(self) -> List[Piece]:
        return [# BLACK PIECES
                Piece(ROOK, (0, 0), BLACK),
                Piece(KNIGHT, (1, 0), BLACK),
                Piece(BISHOP, (2, 0), BLACK),
                Piece(QUEEN, (3, 0), BLACK),
                Piece(KING, (4, 0), BLACK),
                Piece(BISHOP, (5, 0), BLACK),
                Piece(KNIGHT, (6, 0), BLACK),
                Piece(ROOK, (7, 0), BLACK)
                ] + [Piece(PAWN, (i, 1), BLACK) for i in range(8)] + \
                [# WHITE PIECES
                Piece(ROOK, (0, 7), WHITE),
                Piece(KNIGHT, (1, 7), WHITE),
                Piece(BISHOP, (2, 7), WHITE),
                Piece(QUEEN, (3, 7), WHITE),
                Piece(KING, (4, 7), WHITE),
                Piece(BISHOP, (5, 7), WHITE),
                Piece(KNIGHT, (6, 7), WHITE),
                Piece(ROOK, (7, 7), WHITE)
                ] + [Piece(PAWN, (i, 7), WHITE) for i in range(8)]
    
    def make_move(self, piece, start, end, captured=None, special=None):
        move = Move(piece, start, end, captured, special)
        self.move_history.append(move)

    def undo_move(self):
        if self.move_history:
            last_move = self.move_history.pop()
            self.revert_move(last_move)

    def revert_move(self, last_move: Move):
        # Change the position of the last move piece
        last_move.piece.change_position(last_move.get_start())
        # Restore any captured piece
        if last_move.get_captured():
            self.place_piece(last_move.get_captured())

    def place_piece(self, captured: Piece):
        self.pieces.append(captured)

def main():
    chess = Chess()
    chess.play()

if __name__ == "__main__":
    main()