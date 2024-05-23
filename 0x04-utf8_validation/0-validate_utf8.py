#!/usr/bin/python3
"""
a utf module
"""


def validUTF8(data):
    """summary
    Args:
            data (list[int]): a list of integers
    """
    expected_continuation_bytes = 0
    # Define bit patterns for UTF-8 encoding
    UTF8_BIT_1 = 1 << 7
    UTF8_BIT_2 = 1 << 6

    # Loop over each byte in the input data
    for byte in data:
        leading_one_mask = 1 << 7
        if expected_continuation_bytes == 0:
            while leading_one_mask & byte:
                expected_continuation_bytes += 1
                leading_one_mask = leading_one_mask >> 1
            if expected_continuation_bytes == 0:
                continue
            if expected_continuation_bytes == 1 or\
                    expected_continuation_bytes > 4:
                return False
        else:
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False
        expected_continuation_bytes -= 1
    if expected_continuation_bytes == 0:
        return True
    else:
        return False
