result = []
def divider(a, b):
    if a < b:
        raise ValueError(f"Число a должно быть больше b")
    if b > 100:
        raise IndexError(f"чило b должно быть не больше 100")
    return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, 1: 15, 8 : 4}
try:
    for key in data:
        res = divider(key, data[key])
        result.append(res)
except:
    print(f"ошибка")

print(result)