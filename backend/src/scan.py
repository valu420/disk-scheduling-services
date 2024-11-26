def scan(arm_position, lrequests, disk_size, debug=False):
    """
    SCAN (Elevator) Disk Scheduling Algorithm

    Args:
        arm_position (int): Initial position of the arm
        lrequests (list<int>): List of disk requests
        disk_size (int): Total size of the disk (last track)
        debug (bool): Flag to enable debug output
    """
    distance = 0
    sequence = []
    requests = sorted(lrequests)  # Sort requests in ascending order

    # Split requests into left and right of the initial position
    left = [req for req in requests if req < arm_position]
    right = [req for req in requests if req > arm_position]

    # Determine the direction of the arm movement
    if abs(disk_size-arm_position) <= arm_position and right:
        direction = "up"
    elif left:
        direction = "down"
    else :
        direction = "up"

    # Move to the edge of the disk
    if direction == "up":
        # Move up first, then to the left
        if not left:
            sequence = right
        else:
            sequence = right + [disk_size] + left[::-1]
    elif direction == "down":
        # Move down first, then to the right
        if not right:
            sequence = left[::-1]
        else:
            sequence = left[::-1] + [0] + right

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
# print(scan(96, [125, 17, 23, 67, 90, 128, 189, 115, 97], disk_size=200))