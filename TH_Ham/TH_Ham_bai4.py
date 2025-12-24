# Viết hàm chuyển đổi nhiệt độ từ Celsius sang Fahrenheit
# T (° F) = T (° C) × 9/5 + 32
def do_C(x):
    do_F = (x * 9/5) + 32
    return do_F

x = -50
a = do_C(x)
print(f"{x} độ C = {a} độ F")
    

