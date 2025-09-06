class Reveal():
    max_red = 12
    max_green = 13
    max_blue = 14

    def __init__(self, ball_hash):
        self.red = int(ball_hash["red"])
        self.green = int(ball_hash["green"])
        self.blue = int(ball_hash["blue"])
    
    def __repr__(self):
        return f"{'valid' if self.valid() else 'INVALID' } - red: {self.red}, green: {self.green}, blue: {self.blue}"
    def valid(self):
        return self.red <= self.max_red and self.green <= self.max_green and self.blue <= self.max_blue

class Game():
    def __init__(self, id, reveals=[]):
        self.id = int(id)
        self.reveals = reveals

    def valid(self):
        return all([r.valid() for r in self.reveals])

    def minimum_set(self):
        num_r: int = max([r.red for r in self.reveals])
        num_g: int = max([r.green for r in self.reveals])
        num_b: int = max([r.blue for r in self.reveals])
        return (num_r, num_g, num_b)
    
    def power(self):
        power = 1
        for num in self.minimum_set():
            power *= num
        return power

game_list:[Game] = []


with open("02_data.txt", "r") as file:
    for line in file:
        game_split = line.split(":")
        game = game_split[0]
        id = game[game.find(" "):]
        reveals = game_split[1]
        reveals = reveals.split(";")
        reveal_list:[Reveal] = []

        for reveal in reveals:
            reveal = reveal.split(",")
            ball_hash = {"red": 0, "green": 0, "blue": 0}
        
            for ball in reveal:
                ball = ball.split(" ")
                count = ball[1]
                color = ball[2]
                color = color.replace("\n","")
                ball_hash[color] = count

            reveal = Reveal(ball_hash)
            reveal_list.append(reveal)

        game_list.append(Game(id, reveal_list))
        
solution = sum([g.id for g in game_list if g.valid()])

print("Solution to 2023 Day 2, Part 1:")
print(solution)


## Part 2

solution2: int = sum([g.power() for g in game_list])
print("Solution to 2023 Day 2, Part 2:")
print(solution2)



