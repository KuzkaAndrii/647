from MyWord import cut
class Iterator():
    def __init__(self, cs):
        self.iind=0
        self.find=0
        self.sind=0

        self.mil=list(cs.intset)
        self.mfl=list(cs.fltset)
        self.msl=list(cs.strset)

        self.ilen=len(self.mil)
        self.flen=len(self.mfl)
        self.slen=len(self.msl)

        self.mil=sorted(self.mil)
        self.mfl=sorted(self.mfl)
        self.mfl=self.mfl[::-1]
        self.msl=sorted(self.msl)
    def __next__(self):
        if self.iind<self.ilen:
            self.iind+=1
            return self.mil[self.iind-1]
        elif self.find<self.flen:
            self.find += 1
            return self.mfl[self.find-1]
        elif self.sind<self.slen:
            self.sind+=1
            return self.msl[self.sind-1]
        else:
            raise StopIteration
class CustomSet:
    def __init__(self, a):
        self.intset=set()
        self.fltset=set()
        self.strset=set()
        f=open(a, "rt")
        for i in f.readlines():
            try:
                el=int(str(*cut(i)))
                self.intset.add(el)
            except ValueError:
                try:
                    el=float(str(*cut(i)))
                    self.fltset.add(el)
                except ValueError:
                    el=str(*cut(i))
                    self.strset.add(el)
        f.close()
    def __iter__(self):
        return Iterator(self)


if __name__=="__main__":
    print("Hello, world")