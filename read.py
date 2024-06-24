data = []
count = 0 
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # 1000 的倍數
			print(len(data))

print(len(data)) # 清單長度

# print(data) # 清單
print(data[0]) # 第一筆
print("----------")
print(data[1]) # 第二筆


