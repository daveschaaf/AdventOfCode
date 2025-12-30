## 2023 Day 4, Part 1
from collections import deque

class Scratchcard():
    """Creates a Scratchcard object which tracks the id, winning numbers, and lottery winning_numbers

    """
    def __init__(self, id, winning_numbers, lottery_numbers):
        """Initializes a new Scratchcard

        Args:
            id: int = unique numeric id 
            winning_numbers: [int] = selection of winning numbers assigned to the card
            lottery_numbers: [int] = selection of numbers to be compared to the winning numbers
        
        winning_numbers, lottery_numbers will be sorted automatically

        """
        self.id: int = id
        winning_numbers.sort()
        lottery_numbers.sort()
        self.winning_numbers: [int] = winning_numbers
        self.lottery_numbers: [int] = lottery_numbers

    def matches(self):
        """
        """
        i: int = 0 # index of winning_numbers
        j: int = 0 # index of lottery_numbers
        tally: int = 0 # count of matched numbers

        while i < len(self.winning_numbers) and j < len(self.lottery_numbers):
            n: int = self.winning_numbers[i]
            k: int = self.lottery_numbers[j]
            
            if n == k:
                tally += 1
                i += 1
                j += 1
            
            if n > k:
                j += 1
            
            if k > n:
                i += 1
        return tally 

    def points(self):
        tally: int = self.matches()    

        if tally > 0:
            return 2**(tally-1)
        else:
            return 0


def part1(cards):
    return sum([card.points() for card in cards])



def part2(scratchcards):
    library: dict = {}
    card_deq: deque = deque()
    card_counter: int = 0

    def increment_counter(card, deq = card_deq, counter = card_counter):
        deq.append(card)
        counter += 1

    for card in scratchcards:
        library[card.id] = card
        increment_counter(card)
        # card_deq.append(card)
        # card_counter += 1

    while len(card_deq) > 0:
        card: Scratchcard = card_deq.popleft()
        start_id: int = card.id + 1

        for i in range(start_id, start_id + card.matches()):
            increment_counter(library[i])
            card_deq.append(library[i])
            card_counter += 1
    
    return card_counter


    

    

if __name__ == "__main__": 
    scratchcards: [Scratchcard] = []

    with open("04_data.txt", "r") as file:
        for line in file:
            # Card   1: 91 73 74 57 24 99 31 70 60  8 | 89 70 43 24 62 30 91 87 60 57 90  2 27  3 31 25 39 83 64 73 99  8 74 37 49
            line = line.replace("\n", "")

            colon_split: [str] = line.split(":")
            id: int = int(colon_split[0].split(" ")[-1])
            lottery: [str] = colon_split[1].split("|")

            winning: [int] = [int(s) for s in lottery[0].split(" ") if len(s)]

            numbers: [int] = [int(n) for n in lottery[1].split(" ") if len(n)]

            s = Scratchcard(id, winning, numbers)
            scratchcards.append(s)

    solution1 = part1(scratchcards)
    print("Solution to 2023 Day 4, Part 1:")
    print(solution1)
    # 20855

    solution2 = part2(scratchcards)
    print("Solution to 2023, Day 4, Part 2:")
    print(solution2)
    # 5489600


