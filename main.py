a = int(input("Число-1"))
b = int(input("Число-2"))
c = int(input("Число-3"))
choice = int(input("Вибiр"))
if choice == 1:
    print(max(a,b,c))
elif choice == 2:
    print(min(a,b,c))
elif choice == 3:
    print((a + b) / 2)
else:
    print("Невірний вибір")






