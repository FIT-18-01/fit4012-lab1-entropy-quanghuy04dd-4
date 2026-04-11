# Run Log – FIT4012 Lab 1

## Entropy / Redundancy
- [x] Đã chạy với input `aaaa`
  - Kết quả: Entropy = 0.0000, Redundancy = 8.0000
- [x] Đã chạy với input `abcd`
  - Kết quả: Entropy = 2.0000, Redundancy = 6.0000
- [x] Đã chạy với input `hello world`
  - Kết quả: Entropy = 2.8454, Redundancy = 5.1546

## Modulo inverse
- [x] Đã chạy với `3 7`
  - Kết quả: Nghịch đảo = 5, Kiểm tra: 3 * 5 mod 7 = 1 ✓
- [x] Đã chạy với `10 17`
  - Kết quả: Nghịch đảo = 12, Kiểm tra: 10 * 12 mod 17 = 1 ✓
- [x] Đã chạy với `6 9`
  - Kết quả: Không tồn tại nghịch đảo (gcd(6, 9) = 3 ≠ 1) ✓

## Test cases bổ sung
- [x] Input: `AaBbCc` -> Entropy = 2.5850, Redundancy = 5.4150
- [x] Input: `12345678` -> Entropy = 3.0000, Redundancy = 5.0000
- [x] `a=7, m=26` -> Nghịch đảo = 15, Kiểm tra: 7 * 15 mod 26 = 1 ✓
- [x] `a=11, m=26` -> Nghịch đảo = 19, Kiểm tra: 11 * 19 mod 26 = 1 ✓
- [x] `a=5, m=12` -> Nghịch đảo = 5, Kiểm tra: 5 * 5 mod 12 = 1 ✓

## Điều em học được từ bài lab
1. **Entropy** đo lượng thông tin trung bình của một chuỗi ký tự. Khi tất cả ký tự giống nhau, entropy = 0. Khi các ký tự phân bố đều, entropy đạt cực đại.
2. **Redundancy** (độ dư thừa) = max_entropy - actual_entropy. Với bảng chữ cái 256 ký tự (ASCII), max_entropy = 8 bits.
3. **Nghịch đảo modulo** chỉ tồn tại khi gcd(a, m) = 1. Thuật toán Euclid mở rộng cho phép tìm nghịch đảo một cách hiệu quả.
4. Việc kiểm thử với nhiều test cases giúp xác minh tính đúng đắn của thuật toán và hiểu rõ hơn về hành vi của chương trình.