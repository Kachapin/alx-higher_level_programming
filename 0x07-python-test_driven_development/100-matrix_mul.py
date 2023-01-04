#!/usr/bin/python3
"""Define module to multiply matrices"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices m_a and m_b and return the result.
    
    Parameters:
    - m_a: a list of lists representing a matrix.
    - m_b: a list of lists representing a matrix.
    
    Returns:
    - A list of lists representing the product of m_a and m_b.
    
    Raises:
    - TypeError: if m_a or m_b is not a list, or if m_a or m_b is not a list of lists.
    - ValueError: if m_a or m_b is empty, or if incompatible.
    - TypeError: if m_a or m_b contains elements that are not integers or floats.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize result matrix with zeros
    rows = len(m_a)
    cols = len(m_b[0])

    mat = [[0 for _ in range(cols)] for _ in range(rows)]

    # iterating rows of m_a
    for i in range(len(m_a)):
        # iterating columns of m_b
        for j in range(len(m_b[0])):
            # iterating rows of m_b
            for k in range(len(m_b)):
                mat[i][j] += m_a[i][k] * m_b[k][j]
    return mat
    