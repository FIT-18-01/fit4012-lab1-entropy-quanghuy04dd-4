def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclid(a, b):
    """Returns (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    if b == 0:
        return a, 1, 0
    
    g, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return g, x, y

def mod_inverse(a, m):
    """Returns the modular inverse of a modulo m, or -1 if it doesn't exist"""
    if m <= 0:
        return -1
    
    g, x, y = extended_euclid(a, m)
    
    if g != 1:
        return -1
    
    inv = x % m
    return inv

def main():
    try:
        raw_input = input("Nhap a, m: ").strip()
        parts = raw_input.split()
        if len(parts) < 2:
            print("Vui long nhap 2 so nguyen, cach nhau boi khoang trang.")
            return
        a, m = map(int, parts[:2])
    except ValueError:
        print("Vui long nhap 2 so nguyen.")
        return
    
    if gcd(a, m) != 1:
        print(f"Khong ton tai nghich dao modulo vi gcd({a}, {m}) != 1.")
        return
    
    inv = mod_inverse(a, m)
    print(f"Nghich dao cua {a} mod {m} la: {inv}")
    print(f"Kiem tra: {a} * {inv} % {m} = {(a * inv) % m}")

if __name__ == "__main__":
    main()