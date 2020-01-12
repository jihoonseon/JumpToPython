class Service:
    secret="영구는 배꼽이 두 개다"
    def setname(self,name):
        self.name=name
    def sum(self,a,b):
        c=a+b
        print("%s님 %d+%d=%d입니다"%(self.name,a,b,c))

pey=Service()

print(pey.secret)
print(pey.setname("가고일"))
print(pey.sum(1,1))
