import pygame
import time
import sys
from SolverBruteForce.BruteForce import BruteForce
from VisuelBruteForce.Element import Element
pygame.init()

class Screen(BruteForce,Element):
    def __init__(self):
        BruteForce.__init__(self)
        Element.__init__(self)
        
        self.grid_start_x = 360
        self.grid_start_y = 130
        self.grid_end_x = 805
        self.grid_end_y = 570
        self.grid_width = self.grid_end_x - self.grid_start_x
        self.grid_height = self.grid_end_y - self.grid_start_y
        self.clock = pygame.time.Clock()
        self.grid = self.load_sudoku_grid("input/1.txt")
        self.research = False
        self.font = pygame.font.SysFont("Themundayfreeversion-Regular.ttf", 40)
        pygame.display.set_caption("Sudoku")
        
        
    def display_rect(self):
        self.Window.fill(self.white_1)
        self.rect_full_not_centered(self.white_2,340,20,480,570,10)
        self.rect_full_not_centered(self.white,360,130,445,445,10)
        self.rect_border(self.white_3, 340,20,480,570, 2, 10)
        self.rect_border(self.black, 358,129,447,449, 7, 10)
        self.button_solver = self.button_hover("Button solver", 80, 310, 180, 60, self.white_3, self.white_3, self.white_3, self.white_3, "    SOLVER", "Themundayfreeversion-Regular.ttf", self.white,33, 0, 10)

            
    def display_text(self):
        self.text_not_align("Themundayfreeversion-Regular.ttf", 50, "SUDOKU", self.black, 80, 100)
        self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "SOLVER", self.black, 530, 80)
        self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "BRUTE FORCE", self.black, 500, 40)
        
    def load_sudoku_grid(self, filename):
        grid = []
        with open(filename, 'r') as file:
            for line in file:
                row = line.strip()
                grid.append(row)
        return grid

    def display_line(self):
        cell_size = self.grid_width // 9
        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.Window, (0, 0, 0), (self.grid_start_x + i * cell_size, self.grid_start_y), 
                             (self.grid_start_x + i * cell_size, self.grid_end_y), thickness)
            pygame.draw.line(self.Window, (0, 0, 0), (self.grid_start_x, self.grid_start_y + i * cell_size), 
                             (self.grid_end_x, self.grid_start_y + i * cell_size), thickness)

    def display_number(self):
        cell_size = self.grid_width // 9
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != '_':
                    number = self.font.render(self.grid[i][j], True, (0, 0, 0))
                    self.Window.blit(number, (self.grid_start_x + j * cell_size + (cell_size // 2 - number.get_width() // 2),
                                               self.grid_start_y + i * cell_size + (cell_size // 2 - number.get_height() // 2)))

    def display_result(self):
        if self.result==True and self.research == False:
            self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "Sodoku Finish", self.black, 70, 500)
        elif self.research == True:
            self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "In progress...", self.black, 70, 500)
        elif self.elapsed_time== 0:
            self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "Sudoku empty", self.black, 70, 500)
            
    def display_time(self, time):
        self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "Time :", self.black, 70, 400)

        if self.start_time != 0:
            time_str = "{:.6f}".format(time)
            self.text_not_align("Themundayfreeversion-Regular.ttf", 30, time_str[:6], self.black, 80, 440)
        else:
            self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "0", self.black, 80, 440)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_solver.collidepoint(event.pos):
                        self.research = True
            
            self.display_rect()
            self.display_line()
            self.display_text()
            self.display_number()
            self.display_result()
            print(self.elapsed_time)
            self.display_time(self.elapsed_time)
            

            if self.result == True:
                self.research = False
                
            if self.research:
                self.begin("input/1.txt")
                self.grid = self.load_sudoku_grid("SudokuBruteForce.txt")
                self.display_number()

            pygame.display.flip()

        pygame.quit()
        sys.exit()



# interface = Screen()
# interface.run()
