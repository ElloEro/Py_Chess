from typing import List
import pygame

# Colour as int
WHITE = 1
BLACK = 0
# Piece Name
KNIGHT = "Knight"
ROOK = "Rook"
QUEEN = "Queen"
KING = "King"
BISHOP = "Bishop"
PAWN = "Pawn"
# BLACK PIECES
BLACK_QUEEN = pygame.transform.scale(pygame.image.load("assets/images/black queen.png"), (45, 45))
BLACK_ROOK = pygame.transform.scale(pygame.image.load("assets/images/black rook.png"), (45, 45))
BLACK_BISHOP = pygame.transform.scale(pygame.image.load("assets/images/black bishop.png"), (45, 45))
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load("assets/images/black knight.png"), (45, 45))
BLACK_KING = pygame.transform.scale(pygame.image.load("assets/images/black king.png"), (45, 45))
BLACK_PAWN = pygame.transform.scale(pygame.image.load("assets/images/black pawn.png"), (45, 45))
# WHITE PIECES
WHITE_QUEEN = pygame.transform.scale(pygame.image.load("assets/images/white queen.png"), (45, 45))
WHITE_ROOK = pygame.transform.scale(pygame.image.load("assets/images/white rook.png"), (45, 45))
WHITE_BISHOP = pygame.transform.scale(pygame.image.load("assets/images/white bishop.png"), (45, 45))
WHITE_KNIGHT = pygame.transform.scale(pygame.image.load("assets/images/white knight.png"), (45, 45))
WHITE_KING = pygame.transform.scale(pygame.image.load("assets/images/white king.png"), (45, 45))
WHITE_PAWN = pygame.transform.scale(pygame.image.load("assets/images/white pawn.png"), (45, 45))
# Movement
KING_MOVES = [
            (-1, -1) , (-1, 0) , (-1, 1), # Upper Row
            ( 0, -1)           , ( 0, 1), # Middle Row
            ( 1, -1) , ( 1, 0) , ( 1, 1)  # Bottom Row
]
ORTHOGANAL_MOVES = [
    (0, 1), # Move Down
    (0, -1), # Move Up
    (-1, 0), # Move Left
    (1, 0) # Move Right
]
DIAGONAL_MOVES = [
    (-1, 1), # Bottom Left
    (1, 1), # Bottom Right
    (-1, -1), # Top Left
    (1, -1) # Top Right
]
QUEEN_MOVES = ORTHOGANAL_MOVES + DIAGONAL_MOVES
KNIGHT_MOVES = [
    (-1, 2), # Bot Left
    (1, 2), # Bot Right

    (-1 , -2), # Top Left
    (1, -2), # Top Right

    (2, -1), # Right Top
    (2, 1), # Right Bot

    (-2, -1), # Left Top
    (-2, 1) # Left Bot
]
BLACK_PAWN_MOVE = [
            ( 0, 1) # Move Down
]
BLACK_PAWN_TAKE = [
            (-1, 1), # Take Bottom Left
            ( 1,  1)  # Take Bottom Right
]
WHITE_PAWN_MOVE = [
            ( 0,  -1) # Move Up 
]
WHITE_PAWN_TAKE = [
            (-1,  -1), # Take Top Left
            ( 1,  -1)  # Take Top Right
]

# Piece class
class Piece():
    def __init__(self, piece: str, colour: int, position: tuple[int, int]):
        self.piece = piece
        self.position = position
        self.colour = colour
        self.rule = None

    def valid_move(self):
        return None

    def get_piece(self):
        return self.piece
    
    def get_position(self) -> tuple[int, int]:
        return self.position
    
    def get_colour(self) -> int:
        return self.colour
    
    def get_rule(self):
        return self.rule
    
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
        return "{name}({colour}, {position})\n".format(name=self.get_piece(), position=self.get_position(), colour=self.get_colour())

    def __str__(self) -> str:
        return "{colour} {piece} is on {position}".format(colour=self.print_colour(), piece=self.get_piece(), position=self.to_chess_notation())

class King(Piece):
    def __init__(self, colour: str, position: tuple) -> None:
        super().__init__(KING, colour, position)
        self.image = self.load_colour_image(colour)
        self.rule = KING_MOVES
    
    def load_colour_image(self, colour: str) -> str:
        if colour == WHITE:
            return WHITE_KING
        return BLACK_KING
    
    def valid_move(self, old_position: tuple[int, int], _, __) -> List[tuple[int, int]]:
        valid_pos = []
        king_x, king_y = old_position

        for move_x, move_y in self.get_rule():
            if (move_x + king_x < 0 or move_x + king_x > 7):
                continue
            if (move_y + king_y < 0 or move_y + king_y > 7):
                continue
            valid_pos.append((king_x + move_x, king_y + move_y))
        return valid_pos

class Queen(Piece):
    def __init__(self, colour: str, position: tuple) -> None:
        super().__init__(QUEEN, colour, position)
        self.image = self.load_colour_image(colour)
        self.rule = QUEEN_MOVES

    def load_colour_image(self, colour: str) -> str:
        if colour == WHITE:
            return WHITE_QUEEN
        return BLACK_QUEEN

    def valid_move(self, old_position: tuple[int, int], enemy: tuple[int, int], ally: tuple[int, int]) -> List[tuple[int, int]]:
        valid_pos = []

        for move_x, move_y in self.get_rule():
            queen_x, queen_y = old_position
            while (0 <= move_x + queen_x <= 7 and 0 <= move_y + queen_y <= 7 and (move_x + queen_x, move_y + queen_y) not in ally):
                # If we encounter an enemy piece on the next square
                if (move_x + queen_x, move_y + queen_y) in enemy:
                    valid_pos.append((move_x + queen_x, move_y + queen_y))
                    break
                # Else just append the next move
                queen_x += move_x
                queen_y += move_y
                valid_pos.append((queen_x, queen_y))
        return valid_pos

class Rook(Piece):
    def __init__(self, colour: str, position: tuple) -> None:
        super().__init__(ROOK, colour, position)
        self.image = self.load_colour_image(colour)
        self.rule = ORTHOGANAL_MOVES

    def load_colour_image(self, colour: str) -> str:
        if colour == WHITE:
            return WHITE_ROOK
        return BLACK_ROOK

    def valid_move(self, old_position: tuple[int, int], enemy: tuple[int, int], ally: tuple[int, int]) -> List[tuple[int, int]]:
        valid_pos = []

        for move_x, move_y in self.get_rule():
            rook_x, rook_y = old_position
            while (0 <= move_x + rook_x <= 7 and 0 <= move_y + rook_y <= 7 and (move_x + rook_x, move_y + rook_y) not in ally):
                # If we encounter an enemy piece on the next square
                if (move_x + rook_x, move_y + rook_y) in enemy:
                    valid_pos.append((move_x + rook_x, move_y + rook_y))
                    break
                # Else just append the next move
                rook_x += move_x
                rook_y += move_y
                valid_pos.append((rook_x, rook_y))
        return valid_pos



class Knight(Piece):
    def __init__(self, colour: str, position: tuple) -> None:
        super().__init__(KNIGHT, colour, position)
        self.image = self.load_colour_image(colour)
        self.rule = KNIGHT_MOVES
    
    def load_colour_image(self, colour: str) -> str:
        if colour == WHITE:
            return WHITE_KNIGHT
        return BLACK_KNIGHT

    """
    this is the fancy version for list comprehension
    new_list = [(move_x + knight_x, move_y + knight_y) for move_x, move_y in KNIGHT_MOVES \
            if (0 <= move_x + knight_x <= 7) and (0 <= move_y + knight_y <= 7)]
    """
    def valid_move(self, old_position: tuple[int, int], _, __) -> List[tuple[int, int]]:
        valid_pos = []
        knight_x, knight_y = old_position

        for move_x, move_y in self.get_rule():
            if (move_x + knight_x < 0 or move_x + knight_x > 7):
                continue
            if (move_y + knight_y < 0 or move_y + knight_y > 7):
                continue
            valid_pos.append((move_x + knight_x, move_y + knight_y))
        return valid_pos

class Bishop(Piece):
    def __init__(self, colour: str, position: tuple) -> None:
        super().__init__(BISHOP, colour, position)
        self.image = self.load_colour_image(colour)
        self.rule = DIAGONAL_MOVES

    def load_colour_image(self, colour: str) -> str:
        if colour == WHITE:
            return WHITE_BISHOP
        return BLACK_BISHOP

    def valid_move(self, old_position: tuple[int, int], enemy: tuple[int, int], ally: tuple[int,int]) -> List[tuple[int,int]]:
        valid_pos = []

        for move_x, move_y in self.get_rule():
            bishop_x, bishop_y = old_position
            while (0 <= move_x + bishop_x <= 7 and 0 <= move_y + bishop_y <= 7 and (move_x + bishop_x, move_y + bishop_y) not in ally):
                # If we encounter an enemy piece on the next square
                if (move_x + bishop_x, move_y + bishop_y) in enemy:
                    valid_pos.append((move_x + bishop_x, move_y + bishop_y))
                    break
                # Else just append the next move
                bishop_x += move_x
                bishop_y += move_y
                valid_pos.append((bishop_x, bishop_y))
        return valid_pos

class Pawn(Piece):
    def __init__(self, colour: str, position: tuple) -> None:
        super().__init__(PAWN, colour, position)
        self.image = self.load_colour_image(colour)
        if (self.get_colour() == BLACK):
            self.rule = [BLACK_PAWN_MOVE, BLACK_PAWN_TAKE]
        else:
            self.rule = [WHITE_PAWN_MOVE, WHITE_PAWN_TAKE] 

    def load_colour_image(self, colour: str) -> str:
        if colour == WHITE:
            return WHITE_PAWN
        return BLACK_PAWN

    def valid_move(self, old_position: tuple[int, int], enemy: tuple[(int, int)], _) -> List[tuple[int, int]]:
        valid_pos = []
        cur_x, cur_y = old_position[0], old_position[1]
        # Check for movement
        for move_x, move_y in self.get_rule()[0]:
            if (move_x + cur_x < 0 or move_x + cur_x > 7):
                continue
            if (move_y + cur_y < 0 or move_y + cur_y > 7):
                continue
            if (move_x + cur_x, move_y + cur_y) in enemy:
                continue
            valid_pos.append((move_x + cur_x, move_y + cur_y))
        # Check for diagonal take
        for move_x, move_y in self.get_rule()[1]:
            if (move_x + cur_x, move_y + cur_y) not in enemy:
                    continue
            valid_pos.append((move_x + cur_x, move_y + cur_y))
        return valid_pos

    def promote(self) -> bool:
        if (self.get_colour() == WHITE and self.get_position()[1] == 0):
            return True
        if (self.get_colour() == BLACK and self.get_position()[1] == 7):
            return True
        return False
    

        

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

# The controller that controls Move and GUI
class Chess():
    def __init__(self):
        self.move_history = []
        self.pieces = self.setup()
        self.turn = WHITE

    def play(self):
        print(self.move_history)
        print(self.pieces)
        self.make_move(self.pieces[8], self.pieces[0].get_position(), (0, 1))
        print(self.pieces)
        return
    
    """
        Hard coded the pieces in to make it more easily readable and faster
    """
    def setup(self) -> List[Piece]:
        return [# BLACK PIECES
                Rook(BLACK, (0, 0)),
                Knight(BLACK, (1, 0)),
                Bishop(BLACK, (2, 0)),
                Queen(BLACK, (3, 0)),
                King(BLACK, (4, 0)),
                Bishop(BLACK, (5, 0)),
                Knight(BLACK, (6, 0)),
                Rook(BLACK, (7, 0))
                ] + [Pawn(BLACK, (i, 0)) for i in range(8)] + \
                [# WHITE PIECES
                Rook(WHITE, (0, 7)),
                Knight(WHITE, (1, 7)),
                Bishop(WHITE, (2, 7)),
                Queen(WHITE, (3, 7)),
                King(WHITE, (4, 7)),
                Bishop(WHITE, (5, 7)),
                Knight(WHITE, (6, 7)),
                Rook(WHITE, (7, 7))
                ] + [Pawn(WHITE, (i, 7)) for i in range(8)]
    
    def make_move(self, piece: Piece, start: tuple[int, int], end: tuple[int, int], captured=None, special=None):
        # Normal Movement and Takes
        if end in piece.valid_move(piece.get_position(), [pieces for pieces in self.pieces if pieces.get_colour() != self.turn], [pieces for pieces in self.pieces if pieces.get_colour() == self.turn and pieces.get_position() != start]):
            # Get the history of the move
            move = Move(piece, start, end, captured, special)
            self.move_history.append(move)

            # Change the Piece's position since we moved it
            piece.change_position(end)
        
        # Castle

        # En Passant

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

    def castle(self):
        pass

    def enpassant(self):
        pass

    def place_piece(self, captured: Piece):
        self.pieces.append(captured)

def main():
    chess = Chess()
    chess.play()

if __name__ == "__main__":
    main()