# https://leetcode.com/problems/01-matrix/
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 四个方向的移动
        m = len(mat)
        n = len(mat[0])
        visited = [[0] * n for i in range(m)] # 注意这里的写法！！[[0]*n]*m是错的，创建了m个同样指向的对象
        res = [[0] * n for i in range(m)]
        q = []
        
        # 初始化，如果已经是0了，拿距离就是0，标记为visited
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited[i][j] = 1
                    q.append([i,j])
        
        cost = 0
        # 从0开始遍历
        # 对每层而言，如果reach到1了，当前cost就是0到1的长度
        while q:
            size = len(q)
            for k in range(size):
                cur = q.pop(0)
                i = cur[0]
                j = cur[1]
                if mat[i][j] == 1:
                    res[i][j] = cost
                #判断下一层的点，没越界且没访问过，加入到q中
                for d in dirs:
                    x = i + d[0]
                    y = j + d[1]
                    if (x >= 0) and (x < m) and (y >= 0) and (y < n) and (visited[x][y] == 0):
                        q.append([x, y])
                        visited[x][y] = 1
            
            cost += 1
        
        return res
            
        
