from test1 import sum_to_n

try:
    # 讓使用者輸入 N
    num = int(input("請輸入一個正整數 N 以計算累加結果："))
    
    if num <= 0:
        print("請輸入大於 0 的正整數。")
    else:
        # 呼叫從 test1 匯入的函式
        result = sum_to_n(num)
        print(f"從 1 累加到 {num} 的結果為：{result}")

except ValueError:
    print("輸入錯誤！請輸入數字。")

print("--- 程式執行完畢 ---")