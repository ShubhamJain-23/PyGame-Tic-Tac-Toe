import numpy as np
import pygame
import math

ROWS = 3
COLUMNS = 3

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WIDTH  = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
CIRCLE = pygame.image.load('assets/circle.png')
X = pygame.image.load('assets/x.png')

# Assign a value to a box (row and column) for a player
def mark(row, col, player):
    board[row][col] = player

# Check if a box (row and column) is empty    
def is_valid_mark(row, col):
    return board[row][col] == 0

# Check if the board is full
def is_board_full():
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col] == 0:
                return False
    return True

def draw_board():
    for col in range(COLUMNS):
        for row in range(ROWS):
            if board[row][col] == 1:
                window.blit(CIRCLE, ((col * WIDTH / COLUMNS) + 50, (row * HEIGHT / ROWS) + 50))
            elif board[row][col] == 2:
                window.blit(X, ((col * WIDTH / COLUMNS) + 50, (row * HEIGHT / ROWS) + 50))
        pygame.display.update()


def draw_lines(rows, height, width):
    width_row = width / rows
    for i in range(rows - 1):
        pygame.draw.line(window, BLACK, (width_row, 0), (width_row, height), 7)
        width_row += width / rows
    
    width_column = width / rows
    for i in range(rows - 1):
        pygame.draw.line(window, BLACK, (0, width_column), (width, width_column), 7)
        width_column += width / rows
    pass

def is_winning_move(player):
    if player == 1:
        winning_colour = BLUE
    else:
        winning_colour = RED
    for row in range(ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            pygame.draw.line(window, winning_colour, (0, (row + 1) * WIDTH / ROWS), (WIDTH, (row + 1) * WIDTH / ROWS), 7)
            return True
    for col in range(COLUMNS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            pygame.draw.line(window, winning_colour, ((col + 1) * WIDTH / COLUMNS, 0), ((col + 1) * WIDTH / COLUMNS, HEIGHT), 7)
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        pygame.draw.line(window, winning_colour, (0+10, 0+10), (WIDTH - 10, HEIGHT - 10), 7)
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        pygame.draw.line(window, winning_colour, (HEIGHT - 10, 10), (10, WIDTH - 10), 7)
        return True

board = np.zeros((ROWS, COLUMNS))

game_over = False

Turn = 0

pygame.init()
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Tic-Tac-Toe')
window.fill(WHITE)
draw_lines(ROWS, WIDTH, HEIGHT)
pygame.display.update()
pygame.time.wait(2000)


# Looping the Input
while not game_over:

    for event in pygame.event.get():
        # Check if the user wants to close 
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()
        
        # Check is the mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

            if Turn%2 == 0:
                # Player 1
                row = math.floor(event.pos[1]/(HEIGHT/ROWS))
                col = math.floor(event.pos[0]/(WIDTH/COLUMNS))
                if is_valid_mark(row, col):
                    mark(row, col, 1)   # If input is valid, mark the box
                    if is_winning_move(1):
                        game_over = True
                else:
                    print("Block Already Filled")
                    Turn -= 1

            else:
                # Player 2
                row = math.floor(event.pos[1]/(HEIGHT/ROWS))
                col = math.floor(event.pos[0]/(WIDTH/COLUMNS))
                if is_valid_mark(row, col):
                    mark(row, col, 2)   # If input is valid, mark the box
                    if is_winning_move(2):
                        game_over = True
                else:
                    print("Block Already Filled")
                    Turn -= 1
            Turn += 1
            print(board)
            draw_board()
    
    if is_board_full():
        game_over = True
        
    if game_over == True:
        print("Game Over")
        pygame.time.wait(2000)
        board.fill(0)
        window.fill(WHITE)
        draw_lines(ROWS, WIDTH, HEIGHT)
        draw_board()
        game_over = False
        pygame.display.update()