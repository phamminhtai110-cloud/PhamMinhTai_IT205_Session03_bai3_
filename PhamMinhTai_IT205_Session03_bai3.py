print("=" * 60)
print("=== HỆ THỐNG KHỞI TẠO HỒ SƠ NHÂN SỰ - TechCorp ===")
print("=" * 60)

for i in range(1, 4):
    print(f"\n--- Nhập thông tin nhân viên thứ {i} ---")
    
    employee_id = input("Mã nhân viên (VD: NV001): ").strip()
    full_name = input("Họ và tên nhân viên: ").strip()
    department = input("Phòng ban công tác (VD: IT): ").strip()
    
    if employee_id == "" or full_name == "":
        print("\n[CẢNH BÁO] DỮ LIỆU TÊN HOẶC MÃ KHÔNG HỢP LỆ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
    else:
        print("\n" + "=" * 50)
        print("=== HỒ SƠ NHÂN SỰ ĐIỆN TỬ ===")
        print(f"Mã nhân viên: {employee_id}")
        print(f"Họ và tên: {full_name}")
        print(f"Phòng ban: {department}")
        print("=" * 50)
        print("✅ Đã tạo hồ sơ thành công!")

print("\n" + "=" * 60)
print("✅ Đã hoàn tất quá trình nhập liệu cho 3 nhân viên!")
print("=" * 60)