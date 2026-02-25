#Напиcaти функцію, яка повертає мінімальне ціле число К, яке дозволить Джекі з'їсти всі
#банани на складі протягом Н годин, поки повернеться охорона.
import math

def min_eating_speed(piles, H):
    left = 1
    right = max(piles)
    
    while left < right:
        mid = (left + right) // 2
        
        hours = 0
        for bananas in piles:
            hours += math.ceil(bananas / mid)
        
        if hours > H:
            left = mid + 1
        else:
            right = mid
            
    return left
