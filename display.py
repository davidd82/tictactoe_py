#display.py

class Display:
    def __init__(self, size_):
        self.size = size_

    def print_board(self, state):
        # Adds column coordinates at the top
        print(" ", end = '')
        for i in range(self.size):
            print("  " + str(i) + "   ", end = '')
        
        print("\n")

        # This for loop will build the first n-1 rows because the last row will not have "_____" at the bottom
        # The last row is a special case/row
        # One iteration of the for loop equates to one row being printed
        for i in range((self.size - 1)):
            # Top part of the row being printed
            print("      |", end = '')
            for j in range((self.size - 2)):
                print("     |", end = '')
        
            print("     ", end = '')
            print("\n")

            # Middle part of the row being printed
            # The for loop will need to decide wether to print an X or an O
            # Also prints row coordinates
            if ((state)[i][0] == 0): 
                print(str(i) + "     |", end = '')
            elif ((state)[i][0] == 1):
                print(str(i) + "  X  |", end = '')
            elif ((state)[i][0] == 2):
                print(str(i) + "  O  |", end = '')
            

            for j in range((self.size - 2)):
                if ((state)[i][j + 1] == 0):
                    print("     |", end = '')
                elif((state)[i][j + 1] == 1):
                    print("  X  |", end = '')
                elif((state)[i][j + 1] == 2):
                    print("  O  |", end = '')

            if ((state)[i][self.size - 1] == 0):
                print("     ", end = '')
                print("\n")
            elif ((state)[i][self.size - 1] == 1):
                print("  X  ", end = '')
                print("\n")
            elif ((state)[i][self.size - 1] == 2):
                print("  O  ", end = '')
                print("\n")
            
            # Bottom part of the row being printed
            print(" _____+", end = '')
            for j  in range((self.size - 2)):
                print("_____+", end = '')
            print("_____", end = '')
            print("\n")
        
        # The final row will need to be printed outside of the for loop because the bottom has no "_____"
        # Top part of the row being printed
        print("      |", end = '')
        for i in range((self.size - 2)):
            print("     |", end = '')
        print("     ", end = '')
        print("\n")

        # Middle part of the row being printed
        # The for loop will need to decide wether to print an X or an O
        if ((state)[self.size - 1][0] == 0):
            print(str(self.size - 1) + "     |", end = '')
        elif ((state)[self.size - 1][0] == 1):
            print(str(self.size - 1) + "  X  |", end = '')
        elif ((state)[self.size - 1][0] == 2):
            print(str(self.size - 1) + "  O  |", end = '')

        for i in range((self.size - 2)):
            if ((state)[self.size - 1][i + 1] == 0):
                print("     |", end = '')
            elif((state)[self.size - 1][i + 1] == 1):
                print("  X  |", end = '')
            elif ((state)[self.size - 1][i + 1] == 2):
                print("  O  |", end = '')

        if ((state)[self.size - 1][self.size - 1] == 0):
            print("     ", end = '')
            print("\n")
        elif ((state)[self.size - 1][self.size - 1] == 1):
            print("  X  ", end = '')
            print("\n")
        elif ((state)[self.size - 1][self.size - 1] == 2):
            print("  O  ", end = '')
            print("\n")
        
        # Bottom part of the row being printed
        print(" ", end = '')
        for i in range((self.size - 1)):
            print("     +", end = '')
        
        print("     ", end = '')
        print("\n")
        
    