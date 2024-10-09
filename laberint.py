from collections import deque
import math

def print_field(field, path=None):...

def bfs(field, s, t):
    n = len(field)
    m = len(field[0])
    INF = 10 ** 9
    delta = [(0, -1), (0, 1), (1, 0), (-1, 0)] # даємо змогу ходити типу наліво, направо і тд
    d = [[INF] * m for _ in range(n)]
    p = [[None] * m for _ in range(n)]

    
    used = [[False] * m for _ in range(n)]
    queue = deque()
    

    d[s[0]][s[1]] = 0
    used[s[0]][s[1]] = True
    queue.append(s)
    while len(queue) != 0:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 < nx < n and 0 < ny < m and not used[nx][ny] and  field[nx][ny] != '#':
                d[nx][ny] = d[x][y] + 1
                p[nx][ny] = (x, y)# ми вказуємо що типу ми прийшли з х у
                used[nx][ny] = True
                queue.append((nx, ny))
    print(d[t[0]][t[1]])
    cur = t
    path = []
    while cur is not None:
        path.append(cur)
        cur = p[cur[0]][cur[1]]
    path.reverse()
    print_field(field, path[1:-1])# ми у кінці сказали щоб рух починався трішки далі від точки С і заканчувався трішки далі від точкти Т



if __name__ == '__main__':
    fin = open('test1.txt', 'r') # ми звідси беремо шлях
    field = fin.readlines()
    n = len(field)
    m = len(field[0]) - 1
    s = None
    t = None
    for i in range(n):
        field[i] = field[i].strip()
        if field[i].find('S') != -1: # це та нижче це точки від яких починається та закінчується шлях
            s = (i, field[i].find('S'))
        if field[i].find('T') != -1:
            t = (i, field[i].find('T'))



print_field(field)
print(s, t)
bfs(field, s, t)