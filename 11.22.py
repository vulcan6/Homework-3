# Erick Jimenez
# PSID: 1463639
# Zylab 11.22

palabra = input()
palabra = palabra.split(" ")
freq = {}

for each in palabra:
    if each in freq:
        freq[each] = freq[each] + 1
    else:
        freq[each] = 1
for each in palabra:
    print(each, freq[each])
