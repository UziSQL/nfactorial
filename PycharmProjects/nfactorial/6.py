a = input()

if len(a) > 1:
    a = a[-1] + a[1:-1] + a[0]

print(a)