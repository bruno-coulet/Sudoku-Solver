class Grid:
    def __init__(self):
        pass

    def read_file(self,file_name):
        with open(file_name, 'r') as f:
            data = f.read()
        return self.convert_into_grid(data)

    def convert_into_grid(self, text):
        # Initiate a 9x9 grid filled with zeros
        grid = [[0]*9 for _ in range(9)]
        # Iterates every line of the string
        for i, ligne in enumerate(text.split('\n')):
            #  Iterates every element of the line.
            for j, number in enumerate(ligne):
                if number.isdigit():
                    # assigns the number to the current position in the grid
                    grid[i][j] = int(number)
        return grid

    def display_grid(self,file_name):
        self.grid = self.read_file(file_name)
        print()
        #  Iterates the lines of the grid (from 0 to 8 included) -> Horizontal separation
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            #  Iterates the colunns of the grid (from 0 to 8 included) -> Vertical separation
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
            #     # display the numbera t the position (i, j) in the grid.
            #     print(self.grid[i][j], end=" ")
            # # skips to next line
                if self.grid[i][j] == "_":
                    print("\033[94m" + self.grid[i][j] + "\033[0m", end=" ")
                else:
                    print(self.grid[i][j], end=" ")

            print()
        print()


