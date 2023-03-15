def merge_the_tools(s, k):
    n = len(s)
    num_subs = n // k
    
    for i in range(num_subs):
        sub = s[i*k:(i+1)*k]
        sub_unique = ''.join(set(sub))
        print(sub_unique)

s = input()
k = int(input())
merge_the_tools(s, k)
