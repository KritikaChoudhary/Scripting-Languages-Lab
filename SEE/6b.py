class revers:
    coun=0
    def __init__(self,sent):
        self.sent=sent
    def vowels(self):
        v="AaEeIiOoUu"
        for j in v:
            for i in self.sent:
                if i==j:
                    self.coun+=1
    def rev(self):
        li=self.sent.split()
        li.reverse()
        return " ".join(li)

s=[revers(input("Enter a sentence:")) for i in range(3)]
for i in s:
    print(i.rev())
    i.vowels()
for i in sorted(s,key=lambda x:x.coun,reverse=True):
    print(i.rev(),":",i.coun)
      
              
        
    


