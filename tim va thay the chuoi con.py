for i in range(t):
    s = input()
    s2 = input()
    dem = 0
    while s.find(s2) != -1:  # Tìm đến khi không còn chuỗi con
        s = s.replace(s2, '', 1)  # Thay thế chuỗi con s2 bằng chuỗi rỗng, nhưng chỉ thực hiện thay thế một lần mỗi vòng lặp (do tham số 1 ở cuối).
        dem += 1

    print(dem)
