import time

class MainGame():

    level_file_name = "NEATLevel400.csv"
    width_of_level  = 400
    height_of_level = 10

    width_of_frame  = 10
    height_of_frame = 10
    player_position = 0         # The x position of that player. y position will always be 'height_of_frame / 2'
        
    def __init__(self):
        print("Game starting")
        level = self.read_file()

        while self.player_position != self.width_of_level - 10:
            time.sleep(0.1)
            self.clear_console()
            self.print_screen(level)
            self.player_position += 1


    def read_file(self):
        level = open(self.level_file_name, 'r')
        full_level = level.readlines()
        full_level[0] = full_level[0][3:]               # The first 3 chars read in seem to be garbage, I'm not sure yet if it's corrupted data
                                                        # or just a misread header. I think it's a header from the CSV file though        
        for line in full_level:
            line.strip("\n")
            line = line.replace(",", "")
            

        return full_level

    def print_screen(self, level):
        for line in level:
            line = line.replace(",", "")
            print(line[self.player_position: self.player_position + self.width_of_frame])

    def clear_console(self):
        print("\n" * 20)
    



game = MainGame()
        
