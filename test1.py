# 定義計算 1 加到 N 的函式
def calculate_sum(n):
    """計算 1+2+...+N 的總和"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# 原有的 square 函式（依您的需求保留或修改）
def square(y):
    print(f"目前數值：{y} 與下一個數：{y+1}") 

# 主程式邏輯
try:
    x = int(input("請輸入一個正整數："))

    if x <= 0:
        print(f"您輸入的值 {x} 小於等於 0，請輸入正整數。")
    else:
        print(f"您輸入的值 {x} 大於 0")
        
        # 執行原本的迴圈測試
        print("--- 執行 square 函式測試 ---")
        for i in range(1, x + 1): # 這裡建議 range 到 x 即可，或依需求調整
            square(i)
        
        # 呼叫連加函式並顯示結果
        result = calculate_sum(x)
        print("--- 連加結果 ---")
        print(f"1 加到 {x} 的總和為：{result}")

except ValueError:
    print("錯誤：請輸入有效的整數數字。")

print("\npython 程式測試結束")
def sum_to_n(n):
    """計算從 1 加到 n 的總和"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def square(y):
    """您原本要求的測試函式"""
    print(f"{y}  {y+1}")