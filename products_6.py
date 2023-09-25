#Refactor 程式重構

import os #operating system 作業系統

# 純粹讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續, 跳過 7, 8 行, 進入下一個迴圈
			name, price = line.strip().split(',') #strip 先切掉換行符號跟前後空格, split 再用逗號切割
			products.append([name, price])
	return products	

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入商品價格：')
		price = int(price)
		products.append([name, price])
	print(products)
	return products #因為有 append, products 

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1]) # 只是很簡單的印出東西, 沒有改變, 就不用回傳

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f: # w 是 write 寫入模式 # 可以存成 txt or csv
		f.write('商品,價格\n') # 會亂碼因為編碼的問題, 要加上 encoding = 'utf-8' 此編碼可以讀也可以寫各種符號跟語言
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') # 4個字串加起來變成大字串, 丟回給f檔案做write

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #作業系統裡面的path模組, 檢查檔案在不在
		print('找到檔案了！')
		products = read_file(filename)
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()

