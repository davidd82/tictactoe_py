#display.py

class Display:
    def __init__(self, size_):
        self.size = size_

    def print_board(self, state):
        # Adds column coordinates at the top
        print(" ")
        for i in self.size:
            print("  " + i + "   ")
        
        print("\n")

        # This for loop will build the first n-1 rows because the last row will not have "_____" at the bottom
        # The last row is a special case/row
        # One iteration of the for loop equates to one row being printed
        for i in (self.size - 1):
            # Top part of the row being printed
            print("      |")
            for j in (self.size - 2):
                print("     |")
        
            print("     ")
            print("\n")

            # Middle part of the row being printed
            # The for loop will need to decide wether to print an X or an O
            # Also prints row coordinates
            if ((state)[i][0] == 0): 
                print(i + "     |")
            elif ((state)[i][0] == 1):
                print(i + "  X  |")
            elif ((state)[i][0] == 2):
                print(i + "  O  |")
            

            for j in (self.size - 2):
                if ((state)[i][j + 1] == 0):
                    print("     |")
                elif((state)[i][j + 1] == 1):
                    print("  X  |")
                elif((state)[i][j + 1] == 2):
                    print("  O  |")

            if ((state)[i][self.size - 1] == 0):
                print("     ")
                print("\n")
            elif ((state)[i][self.size - 1] == 1):
                print("  X  ")
                print("\n")
            elif ((state)[i][self.size - 1] == 2):
                print("  O  ")
                print("/n")
            
            # Bottom part of the row being printed
            print(" _____+")
            for j  in (self.size - 2):
                print("_____+")
            print("_____")
            print("/n")
        
        # The final row will need to be printed outside of the for loop because the bottom has no "_____"
        # Top part of the row being printed
        print("      |")
        for i in (self.size - 2):
            print("     |")
        print("     ")
        print("/n")

        # Middle part of the row being printed
        # The for loop will need to decide wether to print an X or an O
        if ((state)[self.size - 1][0] == 0):
            print(self.size - 1 + "     |")
        elif ((state)[self.size - 1][0] == 1):
            print(self.size - 1 + "  X  |")
        elif ((state)[self.size - 1][0] == 2):
            print(self.size - 1 + "  O  |")

        for i in (self.size - 2):
            if ((state)[self.size - 1][i + 1] == 0):
                print("     |")
            elif((state)[self.size - 1][i + 1] == 1):
                print("  X  |")
            elif ((state)[self.size - 1][i + 1] == 2):
                print("  O  |")

        if ((state)[self.size - 1][self.size - 1] == 0):
            print("     ")
            print("/n")
        elif ((state)[self.size - 1][self.size - 1] == 1):
            print("  X  ")
            print("/n")
        elif ((state)[self.size - 1][self.size - 1] == 2):
            print("  O  ")
            print("/n")
        
        # Bottom part of the row being printed
        print(" ")
        for i in (self.size - 1):
            print("     +")
        
        print("     ")
        print("/n")
        
    