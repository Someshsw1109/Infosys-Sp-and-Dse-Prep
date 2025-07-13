# Codeforces Question - Two Buttons (Rating-1400)

''' Author - Somesh raj, Created on 12-07-2025 '''
 
# Greedy Approach
 
# Approach/Logic - we want to go from n to m like agar n = 6 hai aur m = 11 hai to hum 2 operations karke n ko m banana hai aur jis point pe n == m ho gaya wahan se break kar jaana hai
# If we think to hum isse reverse way me v bna sakte hain like ki agar m -- 11 hai to ye ekk odd number hai, operations me kya karna tha ki hume 1 ghatana tha to uski jagah hum 1 add kar denge 
# to humara m = 12 ho gaya after adding 1 to hum yahan pe ekk operation ko count kar lenge uske bdd m even number ho gaya aur operation me ekk aur step hai ki hume 2 se multiply karna tha to hum uska ulta karenge isme 
# multiply na karke hum divide karenge by 2 to 12 // 2 = 6 aur humara m == n mil gaya i mean hum m se n chale aaye aur number of operations only 2 lage to ye best ans hoga


def TwoButtons(n, m):
    count = 0
    while m > n:
        if m % 2 == 0:
            m = m // 2
            count += 1
        else:
            m += 1
            count += 1
    count += (n - m)  
    return count
 
n, m = map(int, input().split())
print(TwoButtons(n, m))
 
# @Copyright Somesh Raj