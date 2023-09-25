import os #operating system 作業系統

# 讀取檔案, 確認有檔案後讀取檔案
products = []
if os.path.isfile('products.csv'): #作業系統裡面的path模組
	print('yeah! 找到檔案了!')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續, 跳過 7, 8 行, 進入下一個迴圈
			name, price = line.strip().split(',') #strip 先切掉換行符號跟前後空格, split 再用逗號切割
			products.append([name, price])
	print(products)
else:
	print('找不到檔案...')

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	p = []
	p.append(name)
	p.append(price) # 可以直接寫成 p = [name, price]
	products.append(p) # 甚至可以直接寫成 products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f: # w 是 write 寫入模式 # 可以存成 txt or csv
	f.write('商品,價格\n') # 會亂碼因為編碼的問題, 要加上 encoding = 'utf-8' 此編碼可以讀也可以寫各種符號跟語言
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # 4個字串加起來變成大字串, 丟回給f檔案做write