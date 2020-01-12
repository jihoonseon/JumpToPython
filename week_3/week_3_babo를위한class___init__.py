class Service:
    secret ="나는 포옹을 좋아해"
    def __init__(self,name):
        self.name=name
    def adder(self,a,b):
        print("%s님 %d+%d=%d입니다"%(self.name,a,b,a+b))
    def new_adder(self,*numbers):
        result=0
        lenofnumbers=len(numbers)
        i=0
        print("%s님 "% self.name,end='')
        for number in numbers:
            i+=1
            result+=number
            print("%d" % number,end='')
            if(i>=lenofnumbers):
                break
            print("+",end='')
        print("=%d입니다"%result,end='')


pey=Service("가고일")

print(pey.secret)
pey.adder(1,2)
pey.new_adder(1,2,3,4,5)
