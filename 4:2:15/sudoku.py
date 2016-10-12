import os
import time

board = [
				[1,0,0,0,0,7,0,9,0], 
				[0,3,0,0,2,0,0,0,8], 
				[0,0,9,6,0,0,5,0,0],
				[0,0,5,3,0,0,9,0,0], 
				[0,1,0,0,8,0,0,0,2], 
				[6,0,0,0,0,4,0,0,0],
				[3,0,0,0,0,0,0,1,0], 
				[0,4,0,0,0,0,0,0,7], 
				[0,0,7,0,0,0,3,0,0]
				]

def printSudoku():
	os.system('clear')
	for row in range(len(board)):
		for col in range(len(board[0])):
			print (board[row][col], end=' ')
			if (col+1)%3 == 0:
				print ('|', end=' ')
		if (row+1)%3 == 0:
			print ('\n','-'*22, sep='')
		else:
			print()
	time.sleep(0.1)


printSudoku()

def getNext(row,col):
	if col<8:
		return row, col+1
	else:
		return row+1, 0

def solveSudoku(row,col):
	if board[row][col]!=0:
		solveSudoku(getNext(row,col))
	for number in range (1,10):
		if validChoice(number,row,col):
			board[row][col]=number
			if solveSudoku(getNext(row,col)):
				return True
	board[row][col]=0
	return False


def validChoice(number, row,col):
	if number in board[row]:
		return False

	for r in range(9):
		if board[r][col]==number:
			return False
			
	Br=3*(row//3)
	Bc=3*(col//3)

	for r in range(Br, Br+3):
		for c in range(Bc,Bc+3):
			if board[r][c]==number:
				return False
	return True

	solveSudoku(0,0)

