import math
import json
import numpy as np

"""
1. all elements of the list contain integers ranging from 1-9

2. the sum has to == 0 % 10

3. the number of 9s, 8s, 7s, 6s, and half of 5s has to be at most 85 
   (if there is an odd number of 5s, round up)

4. there needs to be more 1s than 9s

5. the sum <= 850

6. all the 1s and 2s added up has to be greater than 
   (1)number of 9s+(2)number of 8s

7. all the 1s and 2s and 3s added up has to be greater than 
   (1)number of 9s+(2)number of 8s+(3)number of 7s

8. all the 1s and 2s and 3s 4s added up has to be greater than 
   (1)number of 9s+(2)number of 8s+(3)number of 7s+(4)number of 6s
"""
                                        
                                        
def main():
    # x = high group count (digits 6-9 + ceil(5s/2))
    # H = count of digits 6-9
    # L = count of digits 1-4


    total_count = 0
    combinations = []

    
    for x in range(0, 85 + 1):
        n5_max = min(170 - x, 2 * (85 - x))
        
        for n5 in range(15, n5_max + 1):
            c5 = (n5 + 1) // 2
            
            H = x - c5
            if H < 0: continue
                
            L = 170 - n5 - H
            
            if L <= H: continue
                
            for n9 in range(12, H + 1):
                for n8 in range(12, H - n9 + 1):
                    for n7 in range(12, H - n9 - n8 + 1):
                        n6 = H - n9 - n8 - n7
                        if n6 < 0: continue
                            
                        a = n9 + 1
                        
                        b = n9 + n8 + 1
                        
                        c = n9 + n8 + n7 + 1
                        
                        T_hi = 9*n9 + 8*n8 + 7*n7 + 6*n6 + 5*n5
                        
                        r = (4*L + T_hi) % 10
                        
                        red = 4*L + T_hi - 850
                        
                        for n1 in range(max(a, 0), L + 1):
                            n2_min = max(b - n1, 15)
                            n2_max = L - n1 - 15
                            if n2_min > n2_max: continue
                            
                            for n2 in range(n2_min, n2_max + 1):
                                n3_min = max(c - n1 - n2, 15)
                                n3_max = L - n1 - n2 - 15
                                if n3_min > n3_max: continue
                                
                                base = 3*n1 + 2*n2
                                
                                n3_low = n3_min
                                if red > base:
                                    n3_low = max(n3_min, red - base)
                                if n3_low > n3_max: continue
                                
                                r_diff = (r - base) % 10
                                start = n3_low + (r_diff - (n3_low % 10)) % 10
                                if start < n3_low: start += 10
                                if start > n3_max: continue
                                
                                n3 = start
                                while n3 <= n3_max:

                                    n4 = L - n1 - n2 - n3
                                    
                                    if n1 >= 15 and n1 <= 30 and n2 >= 15 and n3 >= 15 and n4 >= 15 and n5 >= 15 and n6 >= 13 and n7 >= 12 and n8 >= 12 and n9 >= 12:
                                        combinations.append([n1, n2, n3, n4, n5, n6, n7, n8])
                                        total_count += 1
                                        
                                        print(total_count, "th combination:", [n1, n2, n3, n4, n5, n6, n7, n8])
                                    
                                    n3 += 10
                                    
    
    np_combination = np.array(combinations)
    np.savez('combination6.npz', data = np_combination)
    print(f"Total valid lists: {total_count}")


if __name__ == '__main__':
    main()

