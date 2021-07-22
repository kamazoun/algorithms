R'''
Write a program that takes the head of a singly linked list and returns null if there does not exist a
cycle, and the node at the start of the cycle, if a cycle is present. (You do not know the length of the
list in advance.)
'''



def cyclicity(head):
    R'''
    The main idea here is that, runner and current would have to meet (not in O(n), of course) before that point runner.next.next and current.next would both point to the same node. This proves that a cycle exists.
    If any of the node points to None, then a cycle does not exist.
    Make sure to use `is` instead of `==` for checks
    '''

    def cycle(n, length):
        while length > 0:
            n = n.next
            length -= 1

        return n
            

    def find_cycle_len(element):
        start, l = element, 0
        while True:
            l += 1
            start = start.next
            if start is element:
                return l
            
    current = head
    runner = head.next

    while current.next:
        if (runner.next.next is current.next) and (runner.next is not current): # There is a cycle
            cycle_length = find_cycle_len(current.next)

            ## We are going to find the first element with the following technique:
            ## From head, we will try node after node to jump `cycle_length`, if we return to the same node, this was the first node of the cycle
            s = head
            while True:
                if s is cycle(s, cycle_length):
                    return s # This is the beginning of the cycle
                else:
                    s = s.next

        
        if runner.next.next and current.next:
            runner = runner.next.next
            current = current.next
            
        else:
            return None
            


def has_cycle (head):
    R'''
    This is the authors way to find the cycle and beginning node without calculating the length of the cycle
    I think it doesn't work because if at the beginning of the if slow != fast they will never meet as they advance at the same speed
    '''
fast = slow = head
while fast and fast.next and fast.next.next:
slow , fast = slow.next , fast.next.next
if slow is fast: # There is a cycle.
# Tries to find the start of the cycle.
slow = head
# Both pointers advance at the same time.
while slow is not fast:
slow , fast = slow.next , fast.next
return slow # slow is the start of cycle.
return None # No cycle.
