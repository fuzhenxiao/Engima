import copy
class wheel(object):
    def __init__(self,initpos='B'):
        self.input=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.output=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        pos=self.input.index(initpos)
        for i in range(0,26):
            self.output[i]=self.input[(i+pos+26)%26]
    def translate(self,input):
        #print(self.output[self.input.index(input)])
        return self.output[self.input.index(input)]
    def reverse_translate(self,input):
        return self.input[self.output.index(input)]
    def turn(self):
        oldoutput=copy.deepcopy(self.output)
        for i in range(0,26):
            self.output[i]=oldoutput[(i+1+26)%26]

'''class reflecter(object):
    def __init__(self,random_alphabet='TUVWXYZABCDEFGHIJKLMNOPQRS'):
        self.input=list('UTWVYXAZCBEDGFIHKJMLONQPSR')
        self.output=list(random_alphabet)
    def translate(self,input):

        return self.output[self.input.index(input)]
    '''
#这个真是绝了，上面那个对照表居然可以导致A的加密在Z和B之间震荡
class reflecter(object):
    def __init__(self,random_alphabet='TUVYZAKLNOHIJCBEFGMDPWXQRS'):
        self.output=list(random_alphabet)
        self.input=list(random_alphabet)
        for i in range(1,27):
            if i%2==0:
                self.input[i-2]=self.output[i-1]
                self.input[i - 1] = self.output[i - 2]
    def translate(self,input):

        return self.output[self.input.index(input)]

class engima(object):
    def __init__(self,initcode='EGN'):
        self.wheelnum=len(initcode)
        self.wheels = []
        self.clock=[]

        initcodelist=list(initcode)
        for i in range(0,self.wheelnum):
            self.wheels.append(wheel(initcodelist[i]))
            self.clock.append(1)

        self.reflectlayer = reflecter()

        #self.wheels.append(self.reflectlayer)
    def translate(self,txt=''):
        txt=list(txt)
        output=[]
        for i in range(0,len(txt)):
            self.clock[0]=self.clock[0]+1
            self.wheels[0].turn()
            for k in range(0,len(self.clock)):
                if self.clock[k]%26==0:
                    self.clock[k]=1
                    if k+1<len(self.clock):
                        self.clock[k+1]=self.clock[k+1]+1
                        self.wheels[k+1].turn()
                    else:
                        pass
            #print(self.clock)

            inpt=txt[i]
            #print(inpt)
            for j in self.wheels:
                #print(inpt)
                inpt=j.translate(inpt)

            inpt=self.reflectlayer.translate(inpt)
            #print(inpt)

            for j in range(len(self.wheels)-1,-1,-1):
                inpt=self.wheels[j].reverse_translate(inpt)
                #print(inpt)
            output.append(inpt)
            #print('NEXT')
        #print(output)
        return ''.join(output)


eng=engima()
print(eng.translate('ATTACKBERLININTWODAYS'))
eng=engima()
print(eng.translate('XSUDZLCXKKPGHKUPVCHFT'))











