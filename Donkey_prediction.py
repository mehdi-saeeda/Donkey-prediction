n, m = input().split()
n = int(n)
m = int(m)
responses = {}

for i in range(n):
    line = input().split()
    first_word = line[0]
    second_word = line[1]
    responses[first_word] = second_word

questions = input().split()

result = []
for j in questions:
    if j in responses:
        result.append(responses[j] + " kachal!")
    else:
        result.append("kachal!")

print(" ".join(result))
