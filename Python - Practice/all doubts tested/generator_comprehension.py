def hi(nums):
    """
    Check if any number in the given list is divisible by 7.

    Args:
        nums (list): A list of numbers.

    Returns:
        bool: True if any number is divisible by 7, False otherwise.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False


def hii(nums) -> int:
    """
    Returns the first number in the given list that is divisible by 7.

    Args:
        nums (list): A list of numbers.

    Returns:
        int or None: The first number in the list that is divisible by 7, or None if no such number exists.
    """
    return next(num for num in nums if num % 7 == 0)
