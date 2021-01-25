data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000000 == 0:
            print(len(data))
print('檔案讀取完畢, 總共有', len(data), '筆評論')

print(data[0])


sum_len = 0
for d in data:
    sum_len += len(d)
print('留言平均長度為', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '超過100個字母')
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('有', len(good), '筆含有good的留言')
print(good[0])

good = [1 for d in data if 'good' in d]
print(good)

bad = ['bad' in d for d in data]
print(bad)

bad = []
for d in data:
        bad.append('bad' in d)
print(bad)


# 文字記數+ 查字典
wc = {} # word_count
for d in data:
    words = d.split()
    for word in words: # 巢狀迴圈(迴圈裡還有迴圈)
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增新的key進wc字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))

while True:
    word = input('請問你想查什麼字?')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為:', wc[word])
    else:
        print('沒有出現過哦')

print('感謝使用本查詢功能')
