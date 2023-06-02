"""
Example for imput:

10
################## ##
#k################ ##
# ##               ##
# ## ################
# ## ################
# ## #########      #
#              #### #
#    ######### #### #
#              #### #
################### #

"""

number_of_rows = int(input())
maze = []

for number_of_rows in range(number_of_rows):
    maze_row = []
    row = str(input())
    for i in row:
        maze_row.append(i)
    maze.append(maze_row)
    del maze_row

Kate_X = None
Kate_Y = None
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "k":
            Kate_Y = j
            Kate_X = i
count = 0
maze[Kate_X][Kate_Y] = str(count)
second_count = 0
cnt = 0
while True:
    count_space = 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == " ":
                count_space += 1
    if count_space == 0:
        break

    second_count = cnt
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == str(count):
                if i < len(maze) - 1:
                    if maze[i + 1][j] == " ":
                        maze[i + 1][j] = str(count + 1)
                if i > 0:
                    if maze[i - 1][j] == " ":
                        maze[i - 1][j] = str(count + 1)
                if j < len(maze[i]) - 1:
                    if maze[i][j + 1] == " ":
                        maze[i][j + 1] = str(count + 1)
                if j > 0:
                    if maze[i][j - 1] == " ":
                        maze[i][j - 1] = str(count + 1)
                cnt += 1
    count += 1
    if second_count == cnt:
        break
    print()
    for i in range(len(maze)):
        print()
        for j in range(len(maze[i])):
            try:
                if int(maze[i][j]) > 9:
                    print(maze[i][j], end=" ")
                else:
                    print(" " + maze[i][j], end=" ")
            except ValueError:
                if maze[i][j] == " ":
                    print(maze[i][j], end="  ")
                else:
                    print(maze[i][j], end="##")


# region Smallest amount of moves code
# current = 0
# result = -1
# for i in range(len(maze)):
#     for j in range(len(maze[i])):
#         if maze[i][j] == " ":
#             maze[i][j] = "#"
# for i in range(len(maze[0])):
#     if maze[0][i] != "#":
#         current = int(maze[0][i])
#         result = current
# for i in range(len(maze[len(maze)-1])):
#     if maze[len(maze) - 1][i] != "#":
#         current = int(maze[len(maze) - 1][i])
#         result = current
# for i in range(len(maze)):
#     if maze[i][0] != "#":
#         current = int(maze[i][0])
#         result = current
# for i in range(len(maze)):
#     if maze[i][len(maze[i]) - 1] != "#":
#         current = int(maze[i][len(maze[i]) - 1])
#         result = current
#
# for i in range(len(maze[0])):
#     if maze[0][i] != "#":
#         current = int(maze[0][i])
#         if result < current:
#             result = current
# for i in range(len(maze[len(maze)-1])):
#     if maze[len(maze) - 1][i] != "#":
#         current = int(maze[len(maze) - 1][i])
#         if result < current:
#             result = current
# for i in range(len(maze)):
#     if maze[i][0] != "#":
#         current = int(maze[i][0])
#         if result < current:
#             result = current
# for i in range(len(maze)):
#     if maze[i][len(maze[i]) - 1] != "#":
#         current = int(maze[i][len(maze[i]) - 1])
#         if result < current:
#             result = current
# if result == -1:
#     print("Kate cannot get out")
#     exit()
# result += 1
# print("Kate got out in " + str(result) + " moves")
# endregion
