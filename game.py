import pygame
import random

BLUE = [0, 0, 255]
BLACK = [0, 0, 0]

block_size = 50
left_margin = 100
upper_margin = 50

size = (left_margin + 30*block_size, upper_margin+15*block_size)

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Seabattle")

font_size = int(block_size//1.5)

font = pygame.font.SysFont('Courier New', font_size)


def draw_grid():
    letters = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И']
    for i in range(11):
        #for x in range(11):
        pygame.draw.line(screen, BLACK, (left_margin, upper_margin + i * block_size),
                             (left_margin + 10 * block_size, upper_margin + i * block_size), 1)
        pygame.draw.line(screen, BLACK, (left_margin + i * block_size, upper_margin),
                         (left_margin + i * block_size, upper_margin + 10 * block_size), 1)
        pygame.draw.line(screen, BLACK, (left_margin + 15 * block_size, upper_margin +
                                         i * block_size),
                         (left_margin + 25 * block_size, upper_margin + i * block_size), 1)
        pygame.draw.line(screen, BLACK, (left_margin + (i + 15) * block_size, upper_margin),
                         (left_margin + (i + 15) * block_size, upper_margin + 10 * block_size), 1)
        if i < 10:
            num_ver = font.render(str(i+1), True, BLACK)
            letter_hor = font.render(letters[i], True, BLACK)
            num_ver_width = num_ver.get_width()
            num_ver_height = num_ver.get_height()
            letters_hor_width = letter_hor.get_width()

            screen.blit(num_ver, (left_margin - (block_size//2+num_ver_width//2), upper_margin+i*block_size+(block_size//2- num_ver_height//2)))
            screen.blit(letter_hor,(left_margin + i*block_size + (block_size//2 - letters_hor_width//2), upper_margin+10*block_size))
            screen.blit(num_ver, (left_margin - (block_size // 2 + num_ver_width // 2)+15*block_size,
                                  upper_margin + i * block_size + (block_size // 2 - num_ver_height // 2)))
            screen.blit(letter_hor, (
            left_margin + i * block_size + (block_size // 2 - letters_hor_width // 2)+15*block_size, upper_margin + 10 * block_size))
def main():
    game_over = False
    screen.fill(BLUE)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        draw_grid()
        pygame.display.update()

main()
pygame.quit()