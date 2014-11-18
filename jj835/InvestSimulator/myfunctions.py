import re

def get_positions(positions):
    """Get integer (or list of integer) representation of user-supplied 'positions'.
    Args:
        -- positions: user-supplied string, which is an integer (or a list of integers).
    Returns:
        -- int_positions: an integer (or a list of integers)."""
    positions = positions.strip()
    list_positions = re.split(r'[\[\(,\)\]]',positions)
    int_positions = [int(tmp) for tmp in list_positions[1:-1]]
    return int_positions

