# Report 1 Page – FIT4012 Lab 1

## 1. Mục tiêu
Bài lab nhằm giúp sinh viên:
- Hiểu và chạy được chương trình tính entropy của một chuỗi ký tự.
- Cài đặt hàm tính độ dư thừa thông tin (redundancy) dựa trên entropy thực tế.
- Cài đặt hàm tìm nghịch đảo modulo bằng thuật toán Euclid mở rộng.
- Rèn luyện kỹ năng kiểm thử và báo cáo kết quả.

## 2. Cách làm
- Đọc hiểu chương trình entropy mẫu trong `entropy_redundancy.cpp`.
- Bổ sung hàm `calculate_redundancy()` tính độ dư thừa: redundancy = max_entropy - actual_entropy.
- Hoàn thiện hàm `mod_inverse()` sử dụng thuật toán Euclid mở rộng để tìm nghịch đảo modulo.
- Chạy thử trên nhiều test case và ghi nhận kết quả.

## 3. Kết quả chính
### 3.1 Entropy và redundancy
| Input | Entropy | Redundancy | Nhận xét |
|---|---:|---:|---|
| aaaa | 0.0000 | 8.0000 | Entropy = 0 vì tất cả ký tự giống nhau |
| abcd | 2.0000 | 6.0000 | Entropy cao hơn do 4 ký tự khác nhau phân bố đều |
| hello world | 2.8454 | 5.1546 | Entropy trung bình, có ký tự lặp (l, o, space) |
| AaBbCc | 2.5850 | 5.4150 | 6 ký tự khác nhau, entropy = log₂(6) ≈ 2.585 |
| 12345678 | 3.0000 | 5.0000 | 8 ký tự khác nhau, entropy = log₂(8) = 3.0 |

### 3.2 Modulo inverse
| a | m | Kết quả mong đợi | Kết quả chương trình | Kiểm tra |
|---:|---:|---|---|---|
| 3 | 7 | 5 | 5 ✓ | 3×5 mod 7 = 1 |
| 10 | 17 | 12 | 12 ✓ | 10×12 mod 17 = 1 |
| 6 | 9 | Không tồn tại | Không tồn tại ✓ | gcd(6,9) = 3 ≠ 1 |
| 7 | 26 | 15 | 15 ✓ | 7×15 mod 26 = 1 |
| 11 | 26 | 19 | 19 ✓ | 11×19 mod 26 = 1 |
| 5 | 12 | 5 | 5 ✓ | 5×5 mod 12 = 1 |

## 4. Kết luận
**Những điều học được:**
- **Entropy** là thước đo lượng thông tin trung bình. Công thức: H = -Σ p(x) × log₂(p(x)). Khi tất cả ký tự giống nhau, entropy = 0. Khi các ký tự phân bố đều, entropy đạt cực đại.
- **Redundancy** (độ dư thừa) = max_entropy - actual_entropy. Với ASCII (256 ký tự), max_entropy = log₂(256) = 8 bits.
- **Nghịch đảo modulo** của a mod m chỉ tồn tại khi gcd(a, m) = 1. Thuật toán Euclid mở rộng cho phép tìm x sao cho a×x + m×y = gcd(a, m) = 1, từ đó x mod m là nghịch đảo cần tìm.

**Khó khăn lớn nhất:** Hiểu rõ cách hoạt động của thuật toán Euclid mở rộng và cách áp dụng để tìm nghịch đảo modulo.

**Điều giúp hiểu rõ hơn:** Việc chạy thử nhiều test cases với các giá trị khác nhau giúp kiểm chứng tính đúng đắn của thuật toán và hiểu sâu hơn về mối quan hệ giữa entropy, redundancy và phân bố ký tự.