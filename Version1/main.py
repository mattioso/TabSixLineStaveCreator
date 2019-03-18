
#Import the used modules
import sys, pygame

#Initalise pygame
pygame.init()

#Create the screens dimensions, and set the variable screen to a display created by those dimensions
size = width, height = 2480, 3508
screen = pygame.display.set_mode(size)

#Set a colour to the pure white colour
colour = (255, 255, 255)

#Initalise a list to hold the lines positions
lines = []
#Initalise a list to hold letter classes
letters = []
#Create a list that holds the letters the lines will be labeled with
exampleLetters = ['e', 'B', 'G', 'D', 'A', 'E']
#Initalise an imported font to draw the letters
font = pygame.font.Font('raleway\Raleway-Black.ttf', 35)

#Create a class to hold the variables needed to draw the letters
class Letters (object):

    #The creator class, run automatically when the Letters class is created, takes x and y as parameters
    def __init__(self, x, y):

        #Set self.pos to a position where it is in line with the drawn line it is labeling
        self.pos = (15, (40 * y) + (x * 350) + (50 - int(35 / 2)))
        #Set self.rendered text to the rendered object of the example letters
        self.renderedText =  font.render(exampleLetters[y], 1, (0, 0, 0))

#This is how many line groups are going to be drawn
for x in range(9):
    #This is how many lines will be drawn per group
    for y in range(6):
        #Appends the position of the line to be drawn to the lines list
        lines.append([50, (40 * y) + (x * 350) + 50, width - 50, (40 * y) + (x * 350) + 50])
        #Appends a letter class to the letters list with the appropriate parameters
        letters.append(Letters(x, y))

#This only needs running once, so no while loop is needed
#Fill the created screen with pure white
screen.fill(colour)

#Run through every line
for x in range(len(lines)):
    #Draw the line on the screen
    pygame.draw.line(screen, (0, 0, 0), (lines[x][0], lines[x][1]), (lines[x][2], lines[x][3]), 3)
    #Draw the text on the screen
    screen.blit(letters[x].renderedText, letters[x].pos)

#Save the screen to a pdf of the name tab
pygame.image.save(screen, "tab.png")



