import pygame
from typing import List

"""
    TODO:
        > ADD CASTLING
        > ADD EN PASSENTE
        > ADD CHECK
        > ADD CHECKMATE
        > ADD PROMOTE
        > PLAYER TURN
    FUTURE MAYBE:
        > UNDO BUTTON
"""

# GLOBAL CONSTANT VARIABLES
BLACK = "BLACK"
WHITE = "WHITE"
SIZE = (400, 400)
FLAGS = 0
SQUARE_SIZE = 50
# COLOURS
COLOUR_WHITE = "#964B00" #technically brown but eeehhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
COLOUR_GREEN = "#69923e"
# PIECES
PAWN = "Pawn"
KNIGHT = "Knight"
BISHOP = "Bishop"
ROOK = "Rook"
QUEEN = "Queen"
KING = "King"
# LOAD IMAGES
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
# LOGIC FOR MOVEMENT
KING_MOVES = [
            (-1, -1) , (-1, 0) , (-1, 1), # Upper Row
            ( 0, -1)           , ( 0, 1), # Middle Row
            ( 1, -1) , ( 1, 0) , ( 1, 1)  # Bottom Row
]
ROOK_MOVES = [
    (0, 1), # Move Down
    (0, -1), # Move Up
    (-1, 0), # Move Left
    (1, 0) # Move Right
]
BISHOP_MOVES = [
    (-1, 1), # Bottom Left
    (1, 1), # Bottom Right
    (-1, -1), # Top Left
    (1, -1) # Top Right
]
QUEEN_MOVES = ROOK_MOVES + BISHOP_MOVES
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


"""
    [[(0,0),_,_,_,_,_,_,_]]
    [[_,_,_,_,_,_,_,_]]
    [[_,_,_,_,_,_,_,_]]
    [[_,_,_,_,_,_,_,_]]
    [[_,_,_,_,_,_,_,_]]
    [[_,_,_,_,_,_,_,_]]
    [[_,_,_,_,_,_,_,_]]
    [[_,_,_,_,_,_,_,(7,7)]]
"""
class Piece():
    def __init__(self, piece: str, colour: str, position: tuple) -> None:
        self._piece = piece
        self.colour = colour
        self.position = position
        self.image = "NULL"
        self.rule = None

    def move(self, new_position: tuple[int, int]):
        # Out of bounds check
        new_x, new_y = max(0, min(7, new_position[0] // SQUARE_SIZE)), max(0, min(7, new_position[1] // SQUARE_SIZE))
        self.position = (new_x, new_y)

    """
        Could maybe use **kwargs or *args for this?
    """
    def is_valid_move(self, ally: List[tuple[int, int]], enemy: List[tuple[int, int]], new_position: tuple[int, int], old_position: tuple[int, int]) -> bool:
        # Check if we are going to capture our own piece
        if new_position in ally:
            return False
        # Check if the move is valid within the piece
        if new_position not in self.valid_move(old_position, enemy, ally):
            return False
        return True

    # Return a list of valid move
    def valid_move(self, old_position: tuple[int, int]) -> List[tuple[int, int]]:
        pass

    def get_piece(self) -> str:
        return self._piece

    def get_colour(self) -> str:
        return self.colour
    
    def get_position(self) -> tuple:
        return self.position

    def get_rule(self) -> List[tuple[int, int]]:
        return self.rule
    
    def load_colour_image(self, colour: str) -> str:
        pass
    
    def get_image(self) -> pygame:
        return self.image
    
    def __str__(self):
        return "Piece: {piece} | Colour: {colour} | Position: {position}".format(piece = self.get_piece(), colour = self.get_colour(), position = self.get_position())

    def __repr__(self):
        return "{piece}({colour}, {position})\n".format(piece = self.get_piece(), colour = self.get_colour(), position = self.get_position())

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
        self.rule = ROOK_MOVES

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
        self.rule = BISHOP_MOVES

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


class Player():
    def __init__(self, pieces: List[Piece]) -> None:
        self.pieces = pieces
        self.captured_pieces = []
        self.has_king = True

    def get_pieces(self) -> List[Piece]:
        return self.pieces
    
    def get_captured_pieces(self) -> List[Piece]:
        return self.captured_pieces

    def get_position(self) -> List[tuple]:
        return [piece.get_position() for piece in self.get_pieces()]

    def get_king(self) -> bool:
        return self.has_king

    def add_piece(self, to_add: Piece):
        self.pieces.append(to_add)
    
    def remove_piece(self, to_remove: Piece):
        self.pieces.remove(to_remove)

    def remove_at(self, position: tuple[int, int]) -> Piece:
        for index, piece in enumerate(self.get_pieces()):
            if piece.get_position() != position:
                continue
            captured_piece = self.get_pieces()[index]
            self.remove_piece(captured_piece)
            return captured_piece

    
    def add_capture(self, captured_piece: Piece):
        self.captured_pieces.append(captured_piece)

    def print_position(self):
        print(self.get_position())

    def print_captured_pieces(self):
        print(self.get_captured_pieces)

    def print_pieces(self):
        for piece in self.get_pieces():
            print(piece)
        
class GameGrid():
    def __init__(self, screen: pygame) -> None:
        self._screen = screen

    def draw_grid(self) -> None:
        alt = True
        for col in range(8):
            for row in range(8):
                if alt:
                    pygame.draw.rect(self._screen, COLOUR_WHITE, [col * 50, row * 50, SQUARE_SIZE, SQUARE_SIZE])
                else:
                    pygame.draw.rect(self._screen, COLOUR_GREEN, [col * 50, row * 50, SQUARE_SIZE, SQUARE_SIZE])
                alt = not alt
            alt = not alt

    def draw_piece(self, black: Player, white: Player) -> None:
        # Draw Black Pieces
        for pieces in black.get_pieces():
            x, y = pieces.get_position()[0] * 50, pieces.get_position()[1] * 50
            self._screen.blit(pieces.get_image(), (x, y))
        # Draw White Pieces
        for pieces in white.get_pieces():
            x, y = pieces.get_position()[0] * 50, pieces.get_position()[1] * 50
            self._screen.blit(pieces.get_image(), (x, y))

class Game():
    def __init__(self) -> None:
        # Initialise pygames
        pygame.init()
        try:
            self.screen = pygame.display.set_mode(SIZE, FLAGS)
            self.timer = pygame.time.Clock()
            self.fps = 60
            self._run = True
            pygame.display.set_caption("Two-Player Chess!")
            self.grid = GameGrid(self.get_screen())
            [self.black, self.white] = self.setup()

        except Exception:
            pygame.quit()
            raise

    def play(self) -> None:
        dragging_piece = None
        prev_place = None
        cur = None
        # Draw the Chess Board and load initial piece placement
        while self.run():
            # event handling
            self.timer.tick(self.fps)
            self.screen.fill('dark gray')
            # Draw the board
            self.grid.draw_grid()
            # Draw the piece
            self.grid.draw_piece(self.black, self.white)
            # Draw the dragged piece
            if (dragging_piece):
                draw_x, draw_y = event.pos
                self.screen.blit(dragging_piece.get_image(), (draw_x - 20, draw_y - 20))

            for event in pygame.event.get():
                # Check if the user is attempting to drag and drop a piece
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    x, y = event.pos
                    # CHECK BLACK PIECES
                    for piece in self.black.get_pieces():
                        piece_position = piece.get_position()
                        if (piece_position[0] * 50 + 25 - 20 <= x <= piece_position[0] * 50 + 25 + 20) and (piece_position[1] * 50 + 25 - 20 <= y <= piece_position[1] * 50 + 25 + 20):
                            dragging_piece = piece
                            prev_place = piece.get_position()
                            cur = self.black.get_position()
                            self.black.remove_piece(piece)
                    # CHECK WHITE PIECES
                    for piece in self.white.get_pieces():
                        piece_position = piece.get_position()
                        if (piece_position[0] * 50 + 25 - 20 <= x <= piece_position[0] * 50 + 25 + 20) and (piece_position[1] * 50 + 25 - 20 <= y <= piece_position[1] * 50 + 25 + 20):
                            dragging_piece = piece
                            prev_place = piece.get_position()
                            cur = self.white.get_position()
                            self.white.remove_piece(piece)
                # Check if the user released mouse 1 and we are dragging a piece
                if (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1) and (dragging_piece):
                    if (dragging_piece.get_colour() == WHITE):
                        # WHITE
                        if (not dragging_piece.is_valid_move(cur, self.black.get_position(), (event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE), prev_place)):
                            dragging_piece.position = prev_place
                        self.white.add_piece(dragging_piece)
                        # Check if we are taking a piece
                        if (dragging_piece.get_position() in self.black.get_position()):
                            captured_piece = self.black.remove_at(dragging_piece.get_position())
                            self.white.add_capture(captured_piece)
                            print(self.white.get_captured_pieces())
                    else:
                        # BLACK
                        if (not dragging_piece.is_valid_move(cur, self.white.get_position(), (event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE), prev_place)):
                            dragging_piece.position = prev_place
                        self.black.add_piece(dragging_piece)
                        # Check if we are taking a piece
                        if (dragging_piece.get_position() in self.white.get_position()):
                            captured_piece = self.white.remove_at(dragging_piece.get_position())
                            self.black.add_capture(captured_piece)
                            print(self.black.get_captured_pieces())
                    dragging_piece = None
                    prev_place = None
                    cur = None
                # Check if the user is dragging
                if (event.type == pygame.MOUSEMOTION) and (dragging_piece):
                    dragging_piece.move(event.pos)
                # Check if the user has quit
                if event.type == pygame.QUIT:
                    self.set_run(False)
            pygame.display.update()

    def setup(self) -> List[Player]:
        # Set up Black Pieces
        black_pieces = self.set_pieces(BLACK)
        black = Player(black_pieces)
        # Set up White Pieces
        white_pieces = self.set_pieces(WHITE)
        white = Player(white_pieces)
        return [black, white]
    
    def set_pieces(self, colour: str) -> List[Piece]:
        if colour == BLACK:
            row = 0
            pawn_row = 1
        else:
            row = 7
            pawn_row = 6
        return [
            Rook(colour, (0,row)),
            Knight(colour, (1,row)),
            Bishop(colour, (2,row)),
            Queen(colour, (3,row)),
            King(colour, (4,row)),
            Bishop(colour, (5,row)),
            Knight(colour, (6,row)),
            Rook(colour, (7,row))
        ] + [Pawn(colour, (i, pawn_row)) for i in range(8)]

    def set_run(self, new_run: bool) -> None:
        self._run = new_run

    def run(self) -> bool:
        return self._run
    
    def get_screen(self) -> pygame.Surface:
        return self.screen
    

if __name__ == "__main__":
    chess = Game()
    chess.play()