words = input()
data = []
while words != '':
    if words not in data:
        data.append(words)
    words = input()
print(data)

for item in data:
    print(item)