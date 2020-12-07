from app.board import choose_start_position, Tile

tile_position = []


def character_in(board):
    for a in range(choose_start_position.start_pos_x):
        for b in range(choose_start_position.start_pos_y):
            char_pos = Tile(a, b)
            tile_position.append(char_pos)
            placed_char_pos = tile_position[-1]
