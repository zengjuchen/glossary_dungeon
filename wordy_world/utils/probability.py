def gaussian_distribution(summit, distance, step):
    """
        return a number list obey gaussian distribution 
    """
    left_end = summit - distance
    right_end = summit + distance
    if summit < 0  or left_end < 0 or right_end < 0:
        raise ValueError("value range can't below zero.")

    if summit ** distance 

