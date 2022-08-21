from collections import deque
def createAdjancyMatrix(arr):
    length = 1 + max( [x[0] for x in arr] + [x[1] for x in arr] )
    matrix = []
    for i in range(length):
        temp = [0] * length
        matrix.append(temp)
    
    for i in range(len(arr)):
        matrix[arr[i][0]][arr[i][1]] = 1
    return matrix

def bfs_traversal(matrix):
    length = len(matrix)
    vis = set()
    for i in range(length):
        if i in vis:
            continue
        vis.add(i)
        q = deque([i])
        while q:
            el = q.pop()
            print(el , end=' ')
            for i in range(length):
                if matrix[el][i] == 1 and i not in vis:
                    q.appendleft(i)
                    vis.add(i)
    print()

def dfs_traversal(matrix):
  length = len(matrix)
  vis = [0]*length;

  for i in range(length):
    if vis[i] == 1:
      continue
    vis[i] = 1
    stack = [i]
    while stack:
      el = stack.pop()
      print(el , end = " ")
      for i in range(length):
        if matrix[el][i] == 1 and vis[i] != 1:
          stack.append(i)
          vis[i] = 1
arr = [[0,1] , [1, 2] ,[1, 3] , [2 , 4] , [3, 4] , [5,7] ,[7,6]]
matrix = createAdjancyMatrix(arr)

for x in matrix:
  print(x)
print('BFS TRAVERSAL')
bfs_traversal(matrix)
print('DFS TRAVERSAL')
dfs_traversal(matrix)