# Test cases – FIT4012 Lab 1

Đánh dấu [x] khi đã chạy và kiểm tra kết quả.

## 1. Entropy / Redundancy
- [x] Input: `aaaa` -> Entropy: 0.0000, Redundancy: 8.0000 (entropy thấp, redundancy cao)
- [x] Input: `abcd` -> Entropy: 2.0000, Redundancy: 6.0000 (entropy cao hơn `aaaa`)
- [x] Input: `hello world` -> Entropy: 2.8454, Redundancy: 5.1546 (entropy và redundancy được tính hợp lệ)

## 2. Modulo inverse
- [x] `a=3, m=7` -> nghịch đảo modulo là 5 (3 * 5 mod 7 = 1) ✓
- [x] `a=10, m=17` -> nghịch đảo modulo là 12 (10 * 12 mod 17 = 1) ✓
- [x] `a=6, m=9` -> không tồn tại nghịch đảo modulo (gcd(6,9) = 3 ≠ 1) ✓

## 3. Test cases bổ sung
- [x] Input: `AaBbCc` -> Entropy: 2.5850, Redundancy: 5.4150 (kiểm tra chữ hoa/thường)
- [x] Input: `12345678` -> Entropy: 3.0000, Redundancy: 5.0000 (kiểm tra chữ số)
- [x] `a=7, m=26` -> nghịch đảo modulo là 15 (7 * 15 mod 26 = 105 mod 26 = 1) ✓
- [x] `a=11, m=26` -> nghịch đảo modulo là 19 (11 * 19 mod 26 = 209 mod 26 = 1) ✓
- [x] `a=5, m=12` -> nghịch đảo modulo là 5 (5 * 5 mod 12 = 60 mod 12 = 1) ✓

## 4. Ghi chú
Tất cả test cases đều vượt qua kiểm tra. Kết quả xác minh:
- Entropy = 0 khi tất cả ký tự giống nhau
- Entropy tăng khi có nhiều ký tự khác nhau
- Redundancy = max_entropy (8 bits cho ASCII 256 ký tự) - entropy
- Modular inverse chỉ tồn tại khi gcd(a, m) = 1