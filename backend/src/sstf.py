from heapq import *

def sstf(arm_position, lrequests, debug=False):
    """
    Shortest Seek Time First implementation

    Args:
        arm_position (int): Initial position of the arm
        lrequests (list<int>): List of disk requests
        debug (bool): Flag to enable debug output
    """
    distance = 0
    sequence = [arm_position]
    current_pos = arm_position
    requests = lrequests[:]

    while requests:
        # Find the request closest to the current position
        closest_request = min(requests, key=lambda x: abs(x - current_pos))
        distance += abs(closest_request - current_pos)
        current_pos = closest_request
        sequence.append(closest_request)
        requests.remove(closest_request)
        if debug:
            print("> ", current_pos, "seeked")

    average = distance / len(lrequests)
    return {
        "sequence": sequence,
        "average": average,
        "distance": distance,
    }

# Example usage:
# print(sstf(96, [125, 17, 23, 67, 90, 128, 189, 115, 97]))