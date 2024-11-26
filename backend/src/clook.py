def clook(arm_position, lrequests, debug=False):
    """
    C-LOOK Disk Scheduling Algorithm

    Args:
        arm_position (int): Initial position of the arm
        lrequests (list<int>): List of disk requests
        debug (bool): Flag to enable debug output
    """
    distance = 0
    sequence = []
    requests = sorted(lrequests)  # Sort requests in ascending order

    # Split requests into left and right of the initial position
    left = [req for req in requests if req < arm_position]
    right = [req for req in requests if req > arm_position]

    # Determine the direction of the arm movement
    if len(left) >= len(right):
        direction = "up"
    else:
        direction = "down"

    # Move based on direction
    if direction == "up":
        # Move up first, then jump to the lowest request and continue
        sequence = right + left
    elif direction == "down":
        # Move down first, then jump to the highest request and continue
        sequence = left[::-1] + right[::-1]

    # Calculate total distance traveled
    current_pos = arm_position
    for req in sequence:
        distance += abs(req - current_pos)
        current_pos = req
        if debug:
            print("> ", current_pos, "seeked")

    average = distance / len(lrequests)
    return {
        "sequence": [arm_position] + sequence,
        "average": average,
        "distance": distance,
    }
# Example usage:
# print("C-LOOK:", clook(96, [125, 17, 23, 67, 90, 128, 189, 115, 97]))