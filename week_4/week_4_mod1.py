def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a)!=type(b):
        print("자료형이 다릅니다")
        return
    else:
        return a+b

if __name__=="__main__":
    print(safe_sum('a',1))
    print(safe_sum(1,4))
    print(safe_sum(10,10.4))