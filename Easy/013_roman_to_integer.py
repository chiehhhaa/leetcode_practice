def romanToInt(s: str):
    # 先定義兩個字典，分別對應單一和雙字母的羅馬數字及其對應的整數值
    one_roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    two_roman = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    # 初始化 sum 變數來存儲最終結果，i 變數用來控制字串的索引
    sum = 0
    i = 0
    
    # 使用 while 迴圈來遍歷整個字串
    while i < len(s):
        # 判斷 i 是否小於字串長度減一，如果是則繼續執行
        if(i < len(s) - 1 and s[i] + s[i+1] in two_roman):
            # 如果 s[i] 及 s[i+1] 的組合在 two_roman 中
            # 則將對應的數值加到 sum 中
            sum += two_roman[s[i] + s[i+1]]
            i += 2
        #  否則，將當前字符對應的數值加到 sum 中
        else:
            sum += one_roman[s[i]]
            i += 1
    return sum

print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
        