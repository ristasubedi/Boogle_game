class Boggle:
    def __init__(self, grid, dictionary):
        """Constructor to initialize the grid and dictionary"""
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = set()  # Using a set to avoid duplicates
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

    def isValidWord(self, word):
        """Check if a word is valid (exists in the dictionary and is at least 3 letters long)"""
        return word in self.dictionary and len(word) >= 3

    def findAllWords(self):
        """Find all words in the grid using DFS"""
        for row in range(self.rows):
            for col in range(self.cols):
                self.dfs(row, col, "")

    def dfs(self, row, col, current_word):
        """Depth-first search to explore all possible word formations"""
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols:
            return
        if self.visited[row][col]:
            return

        # Append current grid letter to the word
        current_word += self.grid[row][col]

        if not any(word.startswith(current_word) for word in self.dictionary):
            return

        if self.isValidWord(current_word):
            self.solutions.add(current_word)

        # Mark the current cell as visited
        self.visited[row][col] = True

        # Explore all 8 adjacent cells (including diagonals)
        for r, c in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            self.dfs(row + r, col + c, current_word)

        # Unmark the cell as visited after backtracking
        self.visited[row][col] = False

    def getSolution(self):
        """Getter to return the found valid words"""
        self.findAllWords()
        return list(self.solutions)


def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    print("Grid:")
    for row in grid:
        print(row)
    print("\nDictionary:", dictionary)

    mygame = Boggle(grid, dictionary)
    print("\nSolutions found:", mygame.getSolution())

if __name__ == "__main__":
    main()