R'''
Implement the "paint fill" function that one might see on many image editing programs. That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color, fill in the surrounding area until the color changes from the original color.
'''
import collections

def authors_adjacent(x, y):
    R'''
    Author considered the case on top, right, left and bottom of the current pixel. It is smart because from there we can reach the `lateral` cases too, but we would need to change our implementation.
    '''
    return [
    (x - 1, y),
    (x, y - 1), (x, y + 1),
    (x + 1, y)
    ]

# My implementations. I previously hadn't considered shallow/deep copy effects on my code. I needed to init visited double array properly, otherwise when I was updating an index such as visited[a][b] all indexes like visited[x][b] where updated.


def adjacent(x, y):
    # Helper function
    return [
    (x - 1, y - 1),(x - 1, y),(x - 1, y + 1),
    (x, y - 1), (x, y + 1),
    (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
    ]


def recursively(screen: list, point: tuple, new_color: str, visited = None, origin_point_color = None):
    x, y = point
    if x < 0 or y < 0 or x >= len(screen) or y >= len(screen[0]):
        return

    if None == visited:
        visited = [[] * len(screen[0])] * len(screen)
        # Because of shallow copy cannot create 2-dimension array with *
        for i in range(len(screen)):
            v = [False]*len(screen[i])
            visited[i] = v

    if not origin_point_color:
        origin_point_color = screen[x][y]

    for pixel in adjacent(x, y):
        xp, yp = pixel
        if xp < 0 or yp < 0 or xp >= len(screen) or yp >= len(screen[0]):
            continue

        if (not visited[xp][yp]) and (screen[xp][yp] == origin_point_color):
            screen[xp][yp] = new_color
            recursively(screen, pixel, new_color, visited, origin_point_color)
        visited[xp][yp] = True



def iterative_bfs(screen: list, point: tuple, new_color: str, visited = None):
    R'''
    Implementing a breadth first search to color all adjacent pixels. The advantage of this method is that we search broad first before searching deep. So we'll actually check all the neighbors of the current pixel
    '''
    x, y = point
    origin_pixel_color = screen[x][y]
    screen[x][y] = new_color # Sets first point color to new_color

    q = collections.deque()
    q.append(point)

    if None == visited:
        visited = [[] * len(screen[0])] * len(screen)
        # Because of shallow copy cannot create 2-dimension array with *
        for i in range(len(screen)):
            v = [False]*len(screen[i])
            visited[i] = v

        visited[x][y] = True # Sets first point visited to True


    while q:
        pixel = q.popleft()
        x, y = pixel
        for p in adjacent(x, y):
            xp, yp = p
            if xp < 0 or yp < 0 or xp >= len(screen) or yp >= len(screen[0]):
                continue

            if (not visited[xp][yp]) and (screen[xp][yp] == origin_pixel_color):
                screen[xp][yp] = new_color
                q.append(p)
            visited[xp][yp] = True


screen = [['1', '1', '0'],
          ['1', '0', '1'],
          ['1', '0', '1'],
          ['0', '1', '1']]

#recursivel(screen, (2, 1), 'blue')
iterative_bfs(screen, (2, 1), 'blue')
print(screen)
