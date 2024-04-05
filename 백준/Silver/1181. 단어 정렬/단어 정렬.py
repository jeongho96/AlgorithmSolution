N = int(input())

word_list = {input() for _ in range(N)}

word_list = list(word_list)

word_list.sort(key=lambda x: (len(x), x))

print(*word_list, sep='\n')
