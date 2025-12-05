class Dial():
    def __init__(self):
        self.current_number = 50
    
    def rotate(self, dir, num_steps):
        if dir == "L":
            self.current_number = (self.current_number - num_steps) % 100
        else:
            self.current_number = (self.current_number + num_steps) % 100

    def apply_moves(self, moves):
        num_zeros = 0
        for dir, num_steps in moves:
            self.rotate(dir, num_steps)
            if self.current_number == 0:
                num_zeros+=1
        
        return num_zeros

def parse_input(filename):
    with open(filename, "r") as infile:
        raw_lines = [ line.strip() for line in infile.readlines()]

    if raw_lines:
        move_list = [(r[0], int(r[1:])) for r in raw_lines]

    return move_list



if __name__ == "__main__":
    dial = Dial()
    moves = parse_input("./input.txt")
    password = dial.apply_moves(moves)
    print(f"The password is: {password}")