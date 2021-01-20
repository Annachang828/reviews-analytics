data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完畢, 總共有', len(data), '筆評論')

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