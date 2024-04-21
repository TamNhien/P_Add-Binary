def add_binary(a, b):
    result = " "
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
        total = carry + (int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0)
        result = str(total % 2) + result
        carry = total // 2
        i, j = i - 1, j - 1
        
    return result

# Nhập 2 chuỗi nhị phân từ người dùng
a = input("Nhaaph chuồi nhị phân a: ")
b = input("Nhaaph chuồi nhị phân b: ")

# Gọi hàm add_binary để tính tổng của hai chuỗi nhị phân
result = add_binary(a, b)

print("Tổng của 2 chuỗi nhị phân: ", result)