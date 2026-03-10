def square(y):
  print(f"{y} 的三次方為 {y**3}") 

x = int(input("請輸入一個正整數："))
if (x<=0):
	print(f"您輸入的值{x},小於等於0")
else:
	print(f"您輸入的值{x},大於等於0")
	for i in range(1,x+1):
		#print(i,end=";")
		square(i)

print("python程式測試")