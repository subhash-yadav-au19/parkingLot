import Vehicle
class ParkingLot:
    def __init__(self):
        self.capacity=0
        self.slotid=0
        self.numofoccupiedslots=0
#CREATE PARKING CAPACITY
    def createParkingLot(self,capacity):
        self.slots=[-1]*capacity
        self.capacity=capacity
        return self.capacity
#
    def getEmptySlot(self):
        for i in range(len(self.slots)):
            if self.slots[i]==-1:
                return i
#CREATE HERE CAR PARKING WITH REG_NO AND COLOR 
    def park(self,regno,color):
        if self.numofoccupiedslots < self.capacity:
            slotid=self.getEmptySlot()
            self.slots[slotid]=Vehicle.car(regno,color)
            self.slotid=self.slotid+1
            self.numofoccupiedslots=self.numofoccupiedslots+1
            return slotid+1
        else:
            return -1
#HERE WE REMOVE CAR TAKING SLOTS NUMBER
    def leave(self,slotid):
        if self.numofoccupiedslots > 0 and self.slots[slotid-1]!=-1:
            self.slots[slotid-1]=-1
            self.numofoccupiedslots=self.numofoccupiedslots-1
            return slotid
        else:
            return -1
#HERE WE CHECK PARKING CAR STATUS    
    def status(self):
        print("slot no.\tregistration no.\tcolour")
        for i in range(len(self.slots)):
            if self.slots[i]!=-1:
                print(str(i+1)+"\t\t"+str(self.slots[i].regno)+"\t\t"+str(self.slots[i].color))
            else:
                continue
#HERE WE CHECK REG_NO BY COLOR
    def Get_Reg_no_By_Color(self,color):
        regnos=[]
        for i in self.slots:
            if i ==-1:
                continue
            if i.color ==color:
                regnos.append(i.regno)
        return regnos
#HERE WE GET SLOTS NO BY CAR REG-NO.
    def Get_Slot_no_By_reg(self,regno):
        for i in range(len(self.slots)):
            if self.slots[i].regno == regno:
                r=i+1
                return r
            else:
                continue
        return -1
#HERE WE GET SLOTS NO BY  CAR COLOR      
    def Get_Slot_By_Color(self,color):
        slotnos=[]
        for i in range(len(self.slots)):
            if self.slots[i]==-1:
                continue
            if self.slots[i].color==color:
                a=str(i+1)
                slotnos.append(a)
        return slotnos
#HERE WE CREATE COMMAND TO OPERATE SUCH METHOD
    def command_handler(self,command):
        
        if command =="A":
            res=int(input("create slots\n"+">"))
            res=self.createParkingLot(res)
            print('Created a parking lot with '+str(res)+' slots')

        elif command =="P":
            reg_no=input("enter car plate no:\n"+">")
            color=input("enter car color no:\n"+">")
            res=self.park(reg_no,color)
            if res==-1:
                print("slot are full")
            else:
                print('Allocated slot number: '+str(res))
                   
        elif command =="E":
            leave_slotid=int(input("enter slot no:\n"+">"))
            status=self.leave(leave_slotid)
            if status==-1:
                print("slot are not present")
            else:
                print("slot"+str(status)+" is free")
          
                
        elif command =="S":
            self.status()


        elif command == "C":
            color=input("enter  car color\n"+">")
            regnos = self.Get_Reg_no_By_Color(color)
            print(','.join(regnos))
        

        elif command =="F":
            regnos=input("enter car reg_no\n"+">")
            slotnos = self.Get_Slot_no_By_reg(regnos)
            print(slotnos)
            
        elif command == "G":
            color=input("enter car color name\n"+">")
            slotno = self.Get_Slot_By_Color(color)
            if slotno == -1:
                print("Not found")
            else:
                print(','.join(slotno))

        elif command =="Q":
            exit(0)

def main():
    command=""
    while command != "Q":
        print("Please Select An Option:\n"
              "A - create_parking_lot\n"
              "P - PARK\n"
              "E - Leave\n"
              "S - status\n"
              "C - Get_Reg_no_By_Color\n"
              "F - Get_Slot_no_By_reg\n"            
              "G - Get_Slot_By_Color\n" 
              "Q - Quit")
        command=input(">")
        obj.command_handler(command)    
if __name__ == '__main__':
    obj=ParkingLot()
    main()