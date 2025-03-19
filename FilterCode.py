import math
class filter(): #Class for the filter 
    def __init__(self, type=None, Lvalue = None, Cvalue = None, Rvalue = 0): #Class for the filter 
        if type == "HP" or type == "LP":
            self.type = type
        else:
            print("\n","Wrong input text","\n"), quit() #Prints an error if the input value is wrong and then quits

        if Lvalue > 0 and Cvalue > 0 and Rvalue > 0:
            self.Lvalue, self.Cvalue, self.Rvalue = Lvalue, Cvalue, Rvalue # Saves all the atributes is a objekt self
        else:
            print("\n","Input values must be positive","\n"), quit() #Prints an error if the input value is wrong and then quits

    def getResonansPoint(self): #This function calculates the resonans point for the filter and then prints it 
        resonansFreq = 1/(2*math.pi*math.sqrt(self.Lvalue*self.Cvalue)) 
        print("\n","The resonans freaquency is:", round(resonansFreq, 4) ,"Hz")
        return round(resonansFreq, 4)

    def getDampingFactor(self): # This function calculates the damping factor for the filter and then prints it 
        dampingFactor = self.Rvalue/2*math.sqrt(self.Cvalue/self.Lvalue)
        print("\n","The damping factor is:", round(dampingFactor, 4))
        return round(dampingFactor, 4)
    
    def getTransfer(self): # This gets the transfer function. The transfer function for high pass and low pass are differet 
        if self.type == "LP":
            transfer = "1 / (s^2*{} + s*{} + 1)".format(self.Lvalue * self.Cvalue, self.Rvalue * self.Cvalue) # Transfer funciton string
            print("\n", "The transfer function for LP is:", transfer)
        elif self.type == "HP":
            transfer = "(s^2*{}) / (s^2*{} + s*{} + 1)".format(self.Lvalue * self.Cvalue,self.Lvalue * self.Cvalue, self.Rvalue * self.Cvalue) 
            print("\n", "The transfer function for HP is:", transfer)
        return transfer
def main():
    # This is all the input for the class
    type = input("Choose wich type of filter. Write HP for high pass and LP for low pass: ")
    Lvalue = float(input("Write an inductior value: "))
    Cvalue = float(input("Write a capacitor value: "))
    Rvalue = float(input("Write a resistor value: "))
    myFilter = filter(type ,Lvalue, Cvalue, Rvalue) # Creats a object of the filter
    myFilter.getResonansPoint(), myFilter.getDampingFactor(), myFilter.getTransfer() # Runs all the funcions in the class
main()