# Công cụ sinh test case tự động cho API bằng Rule-based và AI hỗ trợ

## Giới thiệu
Dự án xây dựng hệ thống tự động sinh test case từ API JSON, áp dụng Rule-based Testing kết hợp AI hỗ trợ nhằm tăng độ bao phủ kiểm thử và giảm thao tác thiết kế test case thủ công.

## Chức năng chính

✔ Tự động suy luận rule từ API schema

✔ Sinh test case:
- Valid Case
- Invalid Case
- Boundary Case
- Dependency Case
- AI Edge Case

✔ Mock API thực thi kiểm thử

✔ Phân tích Coverage

✔ Xuất báo cáo Excel tự động

---

## Công nghệ sử dụng

- Python
- JSON
- Rule Engine
- Mock API
- Coverage Analysis
- AI/LLM
- Pandas
- Excel Export

---

## Kiến trúc hệ thống

```text
API JSON
 ↓
Rule Inference
 ↓
Test Case Generator
 ↓
AI Generator
 ↓
Mock API
 ↓
Coverage Analyzer
 ↓
Excel Report
```

---

## Hướng dẫn chạy

Clone project:

```bash
git clone https://github.com/NgoTranKhanhPhuong/KLTN.git
```

Cài thư viện:

```bash
pip install pandas openpyxl
```

Chạy:

```bash
python app.py
```

---

## Kết quả thực nghiệm

- Tổng test case: 29
- Coverage: 100%
- Hỗ trợ Boundary Testing
- Hỗ trợ Dependency Testing
- AI-assisted Testing

---

## Tác giả

**Ngô Trần Khánh Phương**  
Fresher QA Tester | API Testing | Test Automation | AI-assisted Testing

GitHub:
https://github.com/NgoTranKhanhPhuong/KLTN
