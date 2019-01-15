import time

class MainGame():

    level_file_name = "NEATLevel400.csv"
    width_of_level  = 400
    height_of_level = 10

    width_of_frame  = 10
    height_of_frame = 10
    player_x_position = 0        
    player_y_position = 0

    PLAYER_TILE = "2"
    FLOOR_TILE = "1"
    AIR_TILE = "0"
    
        
    def __init__(self):
        print("Game starting")

        level = self.read_file()

        print(len(level))

        for i in range(0, len(level) - 1):
            if level[i][0] == self.FLOOR_TILE:
                self.player_y_position = self.height_of_level + i

        print(level[0])
                

        while self.player_x_position != self.width_of_level - 10:
            time.sleep(0.1)
            self.clear_console()
            self.print_screen(level)
            self.player_x_position += 1


    def read_file(self):
        level = open(self.level_file_name, 'r')
        full_level = level.readlines()
        full_level[0] = full_level[0][3:]               # The first 3 chars read in seem to be garbage, I'm not sure yet if it's corrupted data
                                                        # or just a misread header. I think it's a header from the CSV file though

        expanded_level = [[0] * self.width_of_level] * (3 * self.height_of_level)       # Adds in the extra blank space above and below the level
        for count, line in enumerate(full_level):
            line.strip("\n")
            line = line.split(",")
            expanded_level[self.height_of_level + count] = line

        print(len(expanded_level))
        expanded_level = [*zip(*expanded_level)]                # Transposes the level matrix to follow (x,y) conventions
        print(len(expanded_level))
            
        return expanded_level

    def print_screen(self, level):
        for row in range(self.player_x_position, self.player_x_position + self.width_of_frame):
            for column in range(self.player_y_position - (int) (self.height_of_frame / 2),
                                self.player_y_position + (int) (self.height_of_frame / 2) ):
                print(level[column][row], end="")
            print()

    def clear_console(self):
        print("\n" * 20)
    



game = MainGame()
        
