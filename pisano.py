def pisano_sequence(N,n):
    '''
    finds the first n terms of the pisano sequence modulo N
    Arguments:
        N = integer, terms of the fibbonacci sequence are reduced to modulo N
        n = integer, length of sequence generated
    Returns:
        a list of the first n terms
    '''
    if N <= 0 or n <= 0:
        return False
    else:
        first_num = 0
        second_num = 1
        temp_num = 1
        i = 1
        output = []
        while i <= n:
            modulo = first_num % N
            output.append(modulo)
            first_num, second_num = second_num, temp_num
            temp_num = first_num + second_num
            i += 1
    return(output)


def pisano_period(N):
    """
    calculate the corresponding pissano period to a given number
    Arguments:
        n = integer, the number we take the pisano sequence modulo of
    Returns:
        the pisano period for a given number n
    """
    if N <= 0:
        return False
    if isinstance(N, int) == False:
        return False
    num_1 = 0
    num_2 = 1
    period = 0
    while True:
        num_1, num_2 = num_2, (num_1 + num_2) % N
        period += 1
        if num_1 == 0 and num_2 == 1:
            return period


print(pisano_sequence(3, 20))
print(pisano_period(3))