import collections

Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

def find_max_simultaneous_event(events):
    R'''
    Author's O(nlogn) and O(n)
    '''
    endpoints = [Endpoint(event.start, True) for event in events] + [Endpoint(event.finish, False) for event in events]

    # We put start times before end times in sort
    endpoints.sort(key = lambda e: (e.time, not e.is_start))

    max_num = current = 0
    for e in endpoints:
        if e.is_start:
            current += 1
            max_num = max(current, max_num)
        else:
            current -= 1

    return max_num
