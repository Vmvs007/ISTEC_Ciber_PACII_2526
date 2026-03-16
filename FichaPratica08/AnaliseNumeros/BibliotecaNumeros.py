
def par(num):
    if num % 2 == 0:
        return True
    else:
        return False


def positivo(num):
    if num>=0:
        return True
    else:
        return False


def primo(num):

    for divisor in range(2, num):
        if num % divisor ==0:
            return False

    return True