#viet chuong trinh tim tat ca cac so chia het cho 7 nhung
# khong phai là bội số của 5, nằm trong đoạn 2000 đến 3200
#các sô thu được sẽ in thành một chuỗi trên môt dòng cách nhau bằng dấu phẩy

# j=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         j.append(str(i))
# print (','.join(j))

# bài 2: tính giai thừa của một so cho trước

# import sys
# sys.setrecursionlimit(5000)
#
# x = int(input('nhap n : '))
#
# def fact(x) :
#     if x == 0 :
#         return 1
#     return x*fact(x-1)
#
# print(fact(x))

#bai 3 Với số nguyên n nhất định, hãy viết chương trình để tạo
# ra một dictionary chứa (i, i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n)
# sau đó in ra dictionary này.
# Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.
# x = int(input('nhap n : '))
# d = {}
# for i in range(1,x+1):
#     d[i] = i*i
# print(d)

# Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu
# phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.
#
# Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
#
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# values=input("Nhập vào các giá trị:")
# l=values.split(",",2)
# t=tuple(l)
# print (l)
# print (t)
