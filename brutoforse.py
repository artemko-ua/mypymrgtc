Zeichen = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?', '\\', '|', '`', '~', "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" 
] 

def start():
    input("Enter to start")

def generate_combinations(stellen):
    if stellen <= 0:
        return

    def generate_recursively(combination, depth):
        if depth == 0:
            print(combination)
            return

        for char in Zeichen:
            generate_recursively(combination + char, depth - 1)

    for char in Zeichen:
        generate_recursively(char, stellen - 1)

start()
generate_combinations(1)
generate_combinations(2)
generate_combinations(3)
generate_combinations(4)
generate_combinations(5)