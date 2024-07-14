def isPalindrome(x: int):
        # 判斷 x 是否為負數，如果為負數就不會是回文數字
        if x < 0:
            return False
        # 把 x 反轉並指定給 reversed_number
        tmp = x
        reversed_number = 0
        while tmp:
            # 這邊先取 tmp 10的餘數（取 x 的尾數）加給 reversed_number
            # 為了確保 x 尾數都會在 reversed_number 的尾數，所以要先把 reversed_number 乘以 10
            reversed_number = reversed_number * 10 + tmp % 10
            # 每執行玩上面的內容後，要把 tmp 改成除以 10 的絕對值，並繼續執行 while 迴圈的判斷
            tmp = tmp // 10 
            # 最後去比較 反轉後的數字 是否有等於 x -> True or False
        return x == reversed_number

print(isPalindrome(x = 121))
print(isPalindrome(x = -121))
print(isPalindrome(x = 10))