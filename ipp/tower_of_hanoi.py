R'''
When monks of a certain temple accomplish this feat with 64 gold disks on 3 diamond needles, it will be the end of the world.
Unfortunately if we run our algorithm with input 64, it won't be over until then...
'''

def hanoi(n : int, left = False):
    if n <= 0: return

    hanoi(n - 1, not left)

    if left:
        print(n, 'left')
    else:
        print(n, 'right')

    hanoi(n - 1, not left)


hanoi(5)
