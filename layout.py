def read_layout(filename="layout\maze.txt"):
    maze = [] #a list of (lists of location/letters)s
    with open(filename, "r") as file:
        for line in file:
            maze.append([])
            line = line.strip() #removing any heading and trailing white space "" "\s" "\t" "\n"
            for letter in line:
                 maze[-1].append(letter)
    return maze
# print the maze in a user-friendly way
def print_layout(maze, user_locantion=(None,None)):
    for i in range(len(maze)):
        row_list = maze[i]
        row_string = ""
        for j in range(len(row_list)):
            letter = row_list[j]
            if (i,j) == user_locantion:
                letter = "X"
            row_string += letter #row_string = row_string
        print(row_string)
















#    file = open(filename, "r")
    # assuming we did something
#    file.close() # it is very important to close the file to aovid doubluc conflict




# def do_something(x,y):
#    print(x)
#    print(y)
#    return
# do_something(x=1, y=2)
