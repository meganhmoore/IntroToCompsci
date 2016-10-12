neighbors=[[-1,0],[0,1],[1,0],[0,-1]]
def search (row, col):
	if maze[row][col]=='#' or maze[row][col]=='.':
		return False
	elif maze[row][col]=='E':
		return True
	maze[row][col]='.'
	for step in neighbors:
		

