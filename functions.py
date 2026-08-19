# writing functions...

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def count_vowels(s):
    """Return the number of vowels in string s."""
    count = 0
    for ch in s:
        if ch in "aeiou":
            count += 1
    return count

def apply_to_list(f, xs):
    t_xs = []
    """Return a list with xs transformed by f."""
    for item in xs:
        t_xs.append(f(item))
    return t_xs