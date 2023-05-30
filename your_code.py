




import sys 

def I_and_O(a,b):
    sys.stdin = open(a,"r")
    sys.stdout = open(b,'a')
    
def solution (s):
    d = s 
    print(d)
    
def window(arr, n , k ):
    i = 0 
    j = 0 
    cs = 0 
    mx = 0 
    s = 0 
    e = 0 
    while j < n :
        cs+=arr[j]
        if j-i+1 < k :
            j +=1 
        elif j-i+1 ==k :
            if mx <cs :
                mx = cs 
                s = i 
                e = j 
            cs-= arr[i]
            i+=1
            j+=1           
    print( "maximiun value is" , mx,"from index",s,"to",e)
    print(*arr[s:e+1])

def variable(arr , n , k ):
    i , j , c   =  0, 0 , 0 
    while j < n :
        c = c+arr[j]
        if c == k :
            m = max (m , j-i+1 )
            j +=1 
        elif c < k :
            j+=1
        elif c > k :
            while(c>k ):
                c -= arr[i]
                i +=1
            j+=1
                
    return m
            

def Non_repeating(l) :
    import collections
    d = collections.defaultdict(int)
    for i in l :
        d[i] += 1
    for i in l:
        if d[i] == 1 :
            return i


def minJumps(arr, n):
    if n ==0:
        return 1
    elif arr[0] == 0:
        return -1
    elif arr[0] and n==0:
        return -1
    maxreach = arr[0]
    steps = arr[0]
    jumps = 1    
    for i in range(1,n):
        if i == n-1:
                return jumps
        maxreach = max(maxreach, arr[i]+i)
        steps-=1
        if steps==0:
            jumps+=1
            steps = maxreach-i
        if maxreach <= i:
            return -1






def first_negative(arr,n,k):
    i , j = 0 , 0 
    l = []
    while j<n : 
        if arr[j] < 0 :
            l.append(arr[j])
        if j-i + 1 < k :
            j+=1
        if j-i+1 == k :
            if len(l) != 0 :
                print(l[0])
                l.remove(l[0])
            else:print(0)
            j+=1
            i+=1
            


def max_in_all ( a, n , k ):
    i ,  j = 0 , 0 
    r = []
    m = 0 
    while j < n :
        m = max(m,a[j])
        if j-i+1 < k :
            j+=1
        elif j-i+1  == k :
            r.append(m)
            i +=1 
            j +=1 
    return r

def max_of_subarrays(arr,N,K):
        from collections import deque
        #code here
        result = []
        dp = deque()
        for i in range(N):
        # Remove elements from the front that are not in the current subarray
            if dp and dp[0] <= i - K:
                dp.popleft()
        # Remove elements from the back that are smaller than the current element
            while dp and arr[dp[-1]] < arr[i]:
                dp.pop()
            dp.append(i)
        # Append the maximum element to the result for valid subarrays
            if i >= K - 1:
                result.append(arr[dp[0]])
        return result




# sum zero subarray  sum should be 0 or  any repeatation in prefix sum arrays 
def sum_zero(arr,n):
    d = {}
    sum = 0 
    for i in range(n):
        sum += arr[i]
        if sum in d.keys() or sum == 0 :
            return True
        d[sum] = True
    return False
        



def first_neg(arr , n ,k):
    from collections import deque 
    i ,j = 0 , 0 
    re = []
    dp = deque()    
    while j < n :
        if arr[j] <  0 :
            dp.append(j)
        if len(dp) > 0 and dp[0] < i :
            dp.popleft()
        if j-i+1 < k :
            j+=1
        elif j - i + 1 == k :
            if len(dp)> 0 :
                re.append(arr[dp[0]])
            else:
                re.append(0)
            i +=1 
            j+=1
    return re 





def activites(s,e):
    #{You are given n activities with their start and finish times.
    # Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. }
    c= []
    i = 0 
    # first should done always 
    c.append(i)
    for  j in range(1,len(s)):
        # after the 1st task  next should be greater  or equal than the previous ending time of task
        if s[j]>= e[i]:
            c.append(j)
            i = j     
    return c
    

def mini_product(a,n):
    if  n == 1 :
        return a[0]
    
    neg , pos , zer , prod = 0, 0 ,0 ,1
    min_pos = float("inf")
    max_neg = float("-inf")
    
    
    for i in range(n):
        if a[i]== 0 :
            zer+=1
            continue
        if a[i]< 0 :
            neg +=1 
            max_neg = max(max_neg,a[i])
        if a[i]> 0 :
            pos+=1
            min_pos = min(min_pos,a[i])
        prod *=a[i]   
          
    #for zeros     
    if zer == n or (neg == 0 and zer>0):
        return 0 
    #for positives
    if neg == 0 :
        return min_pos 
    #for odd negatives
    if neg % 2== 0 :
        return int(prod/max_neg)
    
    return prod











def factors(n):
    
    from math import sqrt
    s = int(sqrt(n))
    f = []
    
    
    for i in range(1,s):
        if n%i == 0 :
            f.append(i)
            if i * i != n :
                f.append(n//i)
            
    print(*f) 



def ap_free(arr, n ):
     # Read the number of test cases

  
      N = int(input())  # Read the size of the sequence
      sequence = list(map(int, input().split()))  # Read the sequence

      is_ap_free = True  # Assume the sequence is AP-Free

      for i in range(N - 2):
          for j in range(i + 1, N - 1):
              for k in range(j + 1, N):
                  if (sequence[j] - sequence[i]) == (sequence[k] - sequence[j]):
                      is_ap_free = False
                      break
              if not is_ap_free:
                  break
          if not is_ap_free:
              break

      if is_ap_free:
          print("YES")
      else:
          print("NO")


"""de = dict()
dict = dict()

l = [1,2,4,5,6,7,8]
h = ['q','e','r','t']

for i,j in zip(l,h):
    dict[i]=j 
     
for  i , j in enumerate(l,start = 100):
    de[i] =j
print(de)

print(dict)
keys = dict.keys()
values = dict.values()
items = dict.items()
print(keys)
print(values)
print(items)

"""



def palindrom():
    for _ in range(int(input())):
        n=int(input())
        
        x=input()
        d=dict()
        for i in x:
            if i in d:
                d[i]+=1
            else :
                d[i]=1
        c=0
        for i in d:
            if d[i]%2!=0:
                c+=1
        e = len(d)
        if e==1:
            if n%2==0:
                print(1)
            else :
                print(2)
        else :
            if n%2==0 :
                if c==0:
                    print(1)
                else :
                    print(0)
            else :
                if c==1:
                    print(1)
                else :
                    print(0)



cache = {}
def fab_series(n) :
    if n in cache :
        return cache[n]
    elif n < 0 :
        return 0 
    elif n == 1 : 
        return 1 
    else:
        cache[n] = fab_series(n-1)+fab_series(n-2)
        return cache[n]


