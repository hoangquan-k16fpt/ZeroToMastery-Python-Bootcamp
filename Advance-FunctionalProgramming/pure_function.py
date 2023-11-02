#Hàm thuần túy là một hàm mà không làm ảnh hưởng đến yếu tố bên ngoài (VD: không print) và bên trong nó sẽ chỉ thực hiện một chức năng nhất định
#Khi chạy 100 lần thì sẽ ra kết quả giống nhau cả 100 lần
def multiplyby2(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item*2)
    return new_lst

print(multiplyby2([1,2,3]))