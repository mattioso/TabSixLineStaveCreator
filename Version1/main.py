
import sys, pygame

pygame.init()

size = width, height = 2480, 3508
screen = pygame.display.set_mode(size)

colour = (255, 255, 255)

lines = []
letters = []
exampleLetters = ['e', 'B', 'G', 'D', 'A', 'E']
font = pygame.font.Font('raleway\Raleway-Black.ttf', 35)

startX = 50
endX = 50
startY = 50

class Letters (object):

    def __init__(self, x, y):

        self.pos = (15, (40 * y) + (x * 350) + (50 - int(35 / 2)))
        self.renderedText =  font.render(exampleLetters[y], 1, (0, 0, 0))

for x in range(9):
    for y in range(6):
        lines.append([50, (40 * y) + (x * 350) + 50, width - 50, (40 * y) + (x * 350) + 50])
        letters.append(Letters(x, y))

for x in range(len(lines)):
    print(lines[x][1])

screen.fill(colour)

for x in range(len(lines)):
    pygame.draw.line(screen, (0, 0, 0), (lines[x][0], lines[x][1]), (lines[x][2], lines[x][3]), 3)
    screen.blit(letters[x].renderedText, letters[x].pos)

pygame.image.save(screen, "tab.png")



