def safe_pos(n, k):
    if n==1:
        return 1
    return ((safe_pos(n-1, k) + k - 1) % n )+1

print('safe postion:', safe_pos(10, 2))
print('safe position:', safe_pos(10, 3))
print('safe position:', safe_pos(5, 4))
