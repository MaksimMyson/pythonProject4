a = int(input("Число-1"))
b = int(input("Число-2"))
c = int(input("Число-3"))
print("1.  Вивести максимум\n2. Вивести мiнiмум\n3. Середне арефметичне")
choice = int(input("Ваш вибiр:"))
if choice == 1:
    print(max(a, b, c))
elif choice == 2:
    print(min(a, b, c))
elif choice == 3:
    print((a + b + c) / 3)
else:
    print("Невірний вибір")






