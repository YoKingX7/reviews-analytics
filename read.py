data = []
count = 0
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # 1000 的倍數
			print(len(data))
print("檔案讀取完了， 總共有", len(data), "筆資料") # 清單長度

sum_len = 0
for d in data:
	sum_len = sum_len + len(d) # sum_len += len(d)
	# print(sum_len) # 總共有多少個字
print("留言的平均長度為", sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print("一共有", len(new), "筆留言長度小於100")
print(new[0])

good = []
for d in data:
	if "good" in d:
		good.append(d)
print("一共有", len(good), "筆留言提到 good")
print(good[0])

