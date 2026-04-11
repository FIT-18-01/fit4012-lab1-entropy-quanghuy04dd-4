#include <iostream>

using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int extended_euclid(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }

    int x1 = 0, y1 = 0;
    int g = extended_euclid(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int mod_inverse(int a, int m) {
    if (m <= 0) {
        return -1;
    }

    int x = 0, y = 0;
    int g = extended_euclid(a, m, x, y);
    if (g != 1) {
        return -1;
    }

    int inv = x % m;
    if (inv < 0) {
        inv += m;
    }
    return inv;
}

int main() {
    int a = 0, m = 0;
    cout << "Nhap a, m: ";
    cin >> a >> m;

    if (gcd(a, m) != 1) {
        cout << "Khong ton tai nghich dao modulo vi gcd(a, m) != 1.\n";
        return 0;
    }

    int inv = mod_inverse(a, m);
    cout << "Nghich dao cua " << a << " mod " << m << " la: " << inv << '\n';
    cout << "Kiem tra: " << a << " * " << inv << " % " << m
         << " = " << (1LL * a * inv % m) << '\n';
    return 0;
}
