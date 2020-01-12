class HousePark:
    lastname="박"
    def __init__(self,name):
        self.fullname=self.lastname+name
    def travel(self,where):
        print("%s %s여행을 가다"%(self.fullname,where))
pey=HousePark("응용")
pey.travel("부산")

class HouseKim(HousePark):
    lastname="김"
    def travel(self,where,day): #오버라이딩
        print("%s %s여행을 %d일가네"%(self.fullname,where,day))
    def love(self,other):
        print("%s %s와 사랑에 빠졌네"%(self.fullname,other.fullname))
    def __add__(self, other):
        print("%s %s와 결혼했네"%(self.fullname,other.fullname))


pey2=HouseKim("가루")
pey2.travel("전주",2)

pey2.love(pey)
pey2+pey
