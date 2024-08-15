# 단어 정렬 # 1181번
test_num = int(input())
sentence = []
for _ in range(test_num):
    temp = input()
    sentence.append(temp)
sentence = list(set(sentence))
sorted_sentence = sorted(sentence, key=lambda x : (len(x), x))

for __ in sorted_sentence:
    print(__)