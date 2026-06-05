"""
- Vì sao Chi nhánh 1 hiển thị đúng là 83 học viên.
=> Vì biến total được set là 0 
- Vì sao Chi nhánh 2 đúng là 60 nhưng hệ thống lại hiển thị 143 học viên
=> Vì từ vòng lặp thứ 2 đã bị cộng dồn cả học sinh viên chi nhánh cũ
- Vì sao Chi nhánh 3 đúng là 97 nhưng hệ thống lại hiển thị 240 học viên
=> Vì đã bị cộng dồn học viên của cả 2 chi nhanh trước đó
"""

branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của một chi nhánh: "))

for branch in range(1, branch_count + 1):

    total_students = 0
    print(f"\nChi nhánh {branch}")
    
    for classroom in range(1, class_count + 1):
        student_count = int(input(f"Nhập số học viên lớp {classroom}: "))
        total_students += student_count

    print(f"Chi nhánh {branch}: {total_students} học viên")