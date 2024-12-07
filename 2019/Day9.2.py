class intCodeComputer:
    def __init__(self,programCode,id =0, relBase=0,indx=0,emptySpace=1000,inptArr=[]):
        self.relativeBase =0
        self.memory = programCode.copy()
        for i in range(emptySpace):self.memory.append(0)
        self.index=indx
        self.inputArray=inptArr.copy()
        self.outputArray=[]
        self.id=id
        self.finished = False
    def compute(self):#computes until there's an input requiered

        while(True):

            if(self.index == 308):
                print(self.memory[311])
            #formatting OPCODE

            self.memory[self.index] = str(self.memory[self.index]).zfill(5)

            parameters = []
            parameterMode = self.memory[self.index][:3]
            OpCode = self.memory[self.index][-2:]

            self.memory[self.index]=int(self.memory[self.index])
            
            if (parameterMode[2] == "0"):parameters.append(int(self.memory[self.index + 1]))
            elif (parameterMode[2] == "1"):parameters.append(self.index + 1)
            else:parameters.append(int(self.memory[self.index + 1]) +self.relativeBase)
            
            if (parameterMode[1] == "0"):parameters.append(int(self.memory[self.index + 2]))
            elif (parameterMode[1] == "1"):parameters.append(self.index + 2)
            else:parameters.append(self.memory[self.index + 2] + self.relativeBase)
            
            if (parameterMode[0] == "0"):parameters.append(int(self.memory[self.index + 3]))
            elif (parameterMode[0] == "1"):parameters.append(self.index + 3)
            else:parameters.append(int(self.memory[self.index + 3]) + self.relativeBase)
            print("debug",parameterMode+OpCode,parameters,self.memory[self.index:self.index+4],self.index)
            if(OpCode=="01"):
                print(f"put at address {parameters[2]} the sum of what is at adresses {parameters[0]}:{self.memory[parameters[0]]} and {parameters[1]}:{self.memory[parameters[1]]}")
                self.memory[parameters[2]] = int(self.memory[parameters[0]]) + int(self.memory[parameters[1]])
                self.index +=4
            elif(OpCode=="02"):
                print(f"put at address {parameters[2]} the product of what is at adresses {parameters[0]}:{self.memory[parameters[0]]} and {parameters[1]}:{self.memory[parameters[1]]}")
                self.memory[parameters[2]] = int(self.memory[parameters[0]]) * int(self.memory[parameters[1]])
                self.index += 4
            elif(OpCode=="03"):
                if(len(self.inputArray)!=0):
                    self.memory[parameters[0]]=self.inputArray[0]
                    self.index+=2
                    self.inputArray.pop(0)
                    print(f"inputed to address {parameters[0]} the value:{self.memory[parameters[0]]}")
                else:
                    print("waiting input")
                    break
            elif(OpCode=="04"):
                print("output from int comp "+str(self.id)+ "  :" +str(self.memory[parameters[0]]))
                self.outputArray.append(self.memory[parameters[0]])
                self.index+=2
            elif(OpCode=="05"):
                if(self.memory[parameters[0]]!=0):
                    self.index = int(self.memory[parameters[1]])
                else:
                    self.index+=3
                print(f"jumped if not zero {self.memory[parameters[0]]} to {self.index}")
            elif(OpCode=="06"):
               # print("went here")
                if (self.memory[parameters[0]] == 0):
                    self.index = int(self.memory[parameters[1]])
                else:
                    self.index += 3
            elif(OpCode=="07"):
                if(int(self.memory[parameters[0]]) < int(self.memory[parameters[1]])):
                    self.memory[parameters[2]]=1
                else:
                    self.memory[parameters[2]]=0
                self.index+=4
                print(f"stored to address {parameters[2]} the inferiority test of:{self.memory[parameters[0]]} with {self.memory[parameters[1]]}")
            elif(OpCode=="08"):
                if (self.memory[parameters[0]] == self.memory[parameters[1]]):
                    self.memory[parameters[2]] = 1
                else:
                    self.memory[parameters[2]] = 0
                self.index += 4
            elif(OpCode=="09"):
                self.relativeBase += self.memory[parameters[0]]
                self.index+=2
                print(f"changed rb by {self.memory[parameters[0]]} from address {parameters[0]}")
            elif(OpCode=="99"):
                print(str(self.id)+ ". computer has finished")
                self.finished = True
                break

            #print(self.relativeBase)

data = open("d9.txt").read().split(",")
for i in range(len(data)):
    data[i]=int(data[i])

print(data)
comp1 = intCodeComputer(data,inptArr=[1])
comp1.compute()
