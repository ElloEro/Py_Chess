import pygame
from typing import List

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

    def move(self, new_position: tuple):
        self.position = new_position

    def is_valid_move(self, board, new_position: tuple) -> tuple:
        pass

    def get_piece(self) -> str:
        return self._piece

    def get_colour(self) -> str:
        return self.colour
    
    def get_position(self) -> tuple:
        return self.position
    
    def load_colour_image(self, colour: str) -> str:
        pass
    
    def get_image(self) -> pygame:
        return self.image
    
    def __str__(self) -> str:
        print("Piece: {piece} | Colour: {colour} | Position: {position}".format(piece = self._piece, colour = self.colour, position = self.position))

class King(Piece):
    def __init__(self, colour: str, position: tuple) -> None:
        super().__init__(KING, colour, position)
        self.image = self.load_colour_image(colour)
    
    def load_colour_image(self, colour: str) -> str:
        if colour == WHITE:
            return WHITE_KING
        return BLACK_KING

class Queen(Piece):
    def __init__(self, colour: str, position: tuple) -> None:
        super().__init__(QUEEN, colour, position)
        self.image = self.load_colour_image(colour)

    def load_colour_image(self, colour: str) -> str:
        if colour == WHITE:
            return WHITE_QUEEN
        return BLACK_QUEEN

class Rook(Piece):
    def __init__(self, colour: str, position: tuple) -> None:
        super().__init__(ROOK, colour, position)
        self.image = self.load_colour_image(colour)

    def load_colour_image(self, colour: str) -> str:
        if colour == WHITE:
            return WHITE_ROOK
        return BLACK_ROOK

class Knight(Piece):
    def __init__(self, colour: str, position: tuple) -> None:
        super().__init__(KNIGHT, colour, position)
        self.image = self.load_colour_image(colour)
    
    def load_colour_image(self, colour: str) -> str:
        if colour == WHITE:
            return WHITE_KNIGHT
        return BLACK_KNIGHT

class Bishop(Piece):
    def __init__(self, colour: str, position: tuple) -> None:
        super().__init__(BISHOP, colour, position)
        self.image = self.load_colour_image(colour)

    def load_colour_image(self, colour: str) -> str:
        if colour == WHITE:
            return WHITE_BISHOP
        return BLACK_BISHOP

class Pawn(Piece):
    def __init__(self, colour: str, position: tuple) -> None:
        super().__init__(PAWN, colour, position)
        self.image = self.load_colour_image(colour)

    def load_colour_image(self, colour: str) -> str:
        if colour == WHITE:
            return WHITE_PAWN
        return BLACK_PAWN


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

    def print_position(self):
        print(self.get_position())

    def print_captured_pieces(self):
        print(self.get_captured_pieces)

    def print_pieces(self):
        print(self.get_pieces()) 

    def __str__(self) -> str:
        piece_info = []
        for piece in self.pieces:
            piece_info.append(f"Piece name: {piece.get_colour()} {piece.get_piece()} at {piece.get_position()}")
        return "\n".join(piece_info)

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

        # Draw the Chess Board and load initial piece placement
        while self.run():
            # event handling
            self.timer.tick(self.fps)
            self.screen.fill('dark gray')
            # Draw the board
            self.grid.draw_grid()
            # Draw the piece
            self.grid.draw_piece(self.black, self.white)

            for event in pygame.event.get():
                # Check if the user is attempting to drag and drop a piece
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                        print("HELLO WORLD!\n")
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