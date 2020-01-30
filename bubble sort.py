import pygame
import numpy


class Sort:
    def __init__(self):
        pygame.init()
        # main window
        self.height = 400
        self.width = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Bubble sort visualization')
        # line parameters
        self.x = 0
        self.y = self.height
        self.thickness = 4
        self.gap = 1
        self.nextLineXPosition = self.thickness + self.gap
        self.COLOR = (1, 100, 100)  # RGB
        # Line heights are stored in this list.
        # Random numbers from 0 to height of the window
        self.array = [numpy.random.randint(0, self.height) for number in range(self.width//self.nextLineXPosition)]

    def swap(self, index):
        # Bubble sort swap function
        # takes index as a parameter
        # swaps index element with index+1 element
        self.array[index], self.array[index + 1] = self.array[index + 1], self.array[index]

    def run(self):
        # This method is ..
        running = True  # while loop condition
        i = 0  # bubble sort "for loop iterators"
        j = 0
        while running:
            # application loop
            self.x = 0
            self.screen.fill((0, 0, 0))  # paint the screen in black

            # Quit event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Bubble sort. Works the same
            # as two for loop version.
            firstNumber = self.array[j]
            secondNumber = self.array[j+1]
            if firstNumber < secondNumber:
                self.swap(j)

            if i < len(self.array):
                j += 1
                if j >= (len(self.array)-i-1):
                    j = 0
                    i += 1

            # Drawing
            for line in range(self.width//self.nextLineXPosition):
                if line == j and i < len(self.array):  # only the j-th line will be yellow
                    pygame.draw.line(self.screen, (200, 200, 0), (self.x, self.y),
                                     (self.x, self.array[line]), self.thickness)
                else:
                    pygame.draw.line(self.screen, self.COLOR, (self.x, self.y),
                                     (self.x, self.array[line]), self.thickness)
                self.x += self.nextLineXPosition
            pygame.display.flip()
            # 850 FPS limit
            # clock = pygame.time.Clock()
            # clock.tick(850)


app = Sort()
app.run()