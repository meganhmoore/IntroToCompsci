import os
import time

maze1 = [
		['#','#',' ','#',' ','E'],
		[' ',' ',' ',' ','#',' '],
		[' ',' ','#',' ',' ',' '],
		[' ',' ',' ','#',' ',' '],
		[' ','#',' ','#','#','#'],
		['S','#',' ',' ',' ',' ']
		]

maze2 = [
		['S','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' '],
		[' ','#',' ','#',' ','#',' ','#','#','#',' ','#',' ','#',' ','#','#'],
		[' ','#',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' '],
		[' ','#',' ','#',' ','#',' ','#',' ','#','#','#','#','#','#','#',' '],
		[' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ',' ',' ',' ',' '],
		[' ','#','#','#',' ','#',' ','#',' ','#',' ',' ',' ','#','#','#',' '],
		[' ',' ',' ',' ',' ','#',' ','#',' ','#',' ','#',' ',' ',' ','#',' '],
		['#','#',' ','#',' ','#',' ','#',' ','#',' ','#','#','#','#','#',' '],
		[' ',' ',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ','#',' '],
		['#','#','#','#',' ','#','#','#','#','#','#','#','#','#',' ','#','#'],
		[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		['#','#','#','#','#','#','#','#','#','#','#','#','#','#',' ','#','#'],
		[' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		['#','#',' ',' ',' ','#',' ','#','#',' ','#','#','#','#',' ','#',' '],
		[' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' '],
		[' ','#',' ','#',' ','#','#','#','#','#','#','#',' ','#',' ','#','E']
		]

maze3 = [
		['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','S','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
		['#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#'],
		['#',' ','#',' ','#',' ','#','#','#','#','#',' ','#',' ','#','#','#',' ','#',' ','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#'],
		['#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#'],
		['#',' ','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#','#','#','#','#',' ','#',' ','#','#','#','#','#',' ','#',' ','#',' ','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' ','#','#','#',' ','#','#','#',' ','#'],
		['#',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#'],
		['#',' ','#','#','#',' ','#','#','#','#','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#','#','#',' ','#'],
		['#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#'],
		['#',' ','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#','#','#','#','#','#','#','#','#',' ','#','#','#','#','#',' ','#',' ','#',' ','#',' ','#',' ','#','#','#','#','#','#','#',' ','#',' ','#','#','#'],
		['#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#'],
		['#','#','#',' ','#','#','#','#','#','#','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#',' ','#'],
		['#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#'],
		['#',' ','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#',' ','#'],
		['#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#'],
		['#','#','#',' ','#','#','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#','#','#',' ','#',' ','#','#','#',' ','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#',' ','#','#','#','#','#'],
		['#',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ','#'],
		['#',' ','#','#','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#','#','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#','#','#','#','#',' ','#',' ','#'],
		['#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#'],
		['#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#'],
		['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#'],
		['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','E','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
		]

def printMaze(maze):
	numRows=len(maze)
	numCols=len(maze[0])
	os.system('clear')
	for row in range(numRows):
		for col in range(numCols):
			print (maze[row][col], end = ' ')
		print()
	time.sleep(0.1)

printMaze(maze3)

neighbors=[[-1,0],[0,1],[1,0],[0,-1]]

def search (maze, row, col):
	if maze[row][col]=='#' or maze[row][col]=='.':
		return False
	elif maze[row][col]=='E':
		return True
	#if it returns True then we have an empty space tile which we can set to a '.'
	maze[row][col]='.'
	printMaze(maze)

	for step in neighbors:
		if 0<=(row+step[0])<len(maze) and 0<=(col+step[1])<len(maze[0]):
			if search(maze, row+step[0],col+step[1]):
				return True
	maze[row][col]=' '
	return False
if search(maze3,0,41):
	printMaze(maze3)




