class HousePark:
    lastname="박"
    def __init__(self,name):
        self.fullname=self.lastname+name
    def travel(self,where):
        print("%s %s로 여행을 가네"%(self.fullname,where))

class HouseKim(HousePark):
    lastname="김"
    def travel(self,where,day):
        print("%s %s로 %d일 여행을 가네"%(self.fullname,where,day))
    def __add__(self, other):
        print("%s %s와 사랑에 빠지네"%(self.fullname,other.fullname))
    def __sub__(self, other):
        print("%s %s와 이혼하네" % (self.fullname, other.fullname))

pey=HousePark("응용")
juliet=HouseKim("줄리엣")
pey.travel("부산")
juliet.travel("부산",3)
juliet+pey
juliet-pey

