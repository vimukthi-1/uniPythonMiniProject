class CabService:
    def __init__(self):
        self.vehicles = {
            "Cars":[
                    {
                     "Brand":"Toyota",
                     "Available": True,
                      "VehicleID": 1,
                     "MaxPassengers":4,
                     "Ac":False,

                     },
                    {
                     "Brand": "Mazda",
                     "Available": True,
                     "VehicleID": 2,
                     "MaxPassengers": 3,
                     "Ac": True,

                     }
                ],
            "Vans":[

                    {"VehicleID":1,
                     "Brand": "Zusuki",
                     "MaxPassengers": 6,
                     "Ac": True,
                     "Available": True}
                    ,
                     {"VehicleID":2,
                      "Brand": "Toyota",
                      "MaxPassengers": 8,
                      "Ac": False,
                      "Available": True
                    }

                ],
            "Threewheels":[
                {"VehicleID":1,
                 "Brand": "Bajaj",
                 "MaxPassengers": 3,

                 "Available": True},

                {"VehicleID":2,
                 "Brand": "Bajaj",
                 "MaxPassengers": 3,

                 "C": True}
                ],
            "Trucks":[
                    {   "VehicleID":1,
                        "Brand":"Mitsubishi",
                        "Size":7,
                        "Available": True

                    },
                    {   "VehicleID":2,
                        "Brand": "Toyota",
                        "Size": 12,
                        "Available": True

                    }
                ],
            "Lorries":[

                    {"VehicleID": 1,
                     "Brand": "Tata",
                     "Load": 2500,
                     "Available": True

                     },
                    {"VehicleID":2,
                     "Brand": "Toyota",
                     "Load": 3500,
                     "Available": True

                     }

            ]
        }

    def addVehicles(self,category):
        TempDictionary = {}
        TempDictionary["brand"] = input("Enter The Brand name: ")
        TempDictionary["Available"] = True
        if category == "c":
            key = "Cars"
            TempDictionary["MaxPassengers"] = int(input("Enter the Maximum Passenger :"))
            TempDictionary["Ac"] = input("Ac available (Y/N): ").lower() == "y"
        elif category == "v":
            key = "Vans"
            TempDictionary["MaxPassengers"] = int(input("Enter the Maximum Passenger :"))
            TempDictionary["Ac"] = input("Ac available (Y/N): ").lower() == "y"
        elif category == "th":
            key = "Threewheels"
            TempDictionary["VehicleID"] = len(self.vehicles["Threewheels"]) + 1
            TempDictionary["MaxPassengers"] = 3
        elif category == "t":
            key = "Trucks"
            TempDictionary["size"] = float(input("Enter the size of the Truck in Feets :"))
        elif category == "l":
            key = "Lorries"
            TempDictionary["Load"] = float(input("Enter the Maximum Load of the Lorry in kilograms:"))
        else:
            print("Invalid category")

        IDs = []
        for veh in self.vehicles[key]:
            IDs.append(veh["VehicleID"])

        TempDictionary["VehicleID"] = max(IDs) + 1
        self.vehicles[key].append(TempDictionary)
        print("\nYou have successfully added a Vehicle to the cab service")
        print(f"Your Vehicle ID is {max(IDs) + 1}")
        print("========================================================")

    def removeVehicle(self,category):
        VehicleID = int(input("Enter the Vehicle ID :"))
        if category == "c":
            key = "Cars"
        elif category == "v":
            key = "Vans"
        elif category == "th":
            key = "Threewheels"
        elif category == "t":
            key = "Trucks"
        elif category == "l":
            key = "Lorries"

        for index,veh in enumerate(self.vehicles[key]):
            if veh["VehicleID"] == VehicleID:
                self.vehicles[key].pop(index)
                print("You have successfully removed Vehicle")
                break
        else:
            print("Please Check your ID again")

        print("===================================================")
    def showVechicles(self,category):
        if category == "c":
            key = "Cars"
        elif category == "v":
            key = "Vans"
        elif category == "th":
            key = "Threewheels"
        elif category == "t":
            key = "Trucks"
        elif category == "l":
            key = "Lorries"
        else:
            print("Invalid category")

        AvVehicles =0
        totalVehicles = len(self.vehicles[key])
        for veh in self.vehicles[key]:
            if veh["Available"]:
                AvVehicles +=1

        print(f"\nTotal {key} : {len(self.vehicles[key])}")
        print(f"{AvVehicles} {key} Available for Hire\n")
        for veh in self.vehicles[key]:
            print(f"Vehicle ID : {veh['VehicleID']}")
            print(f"Brand      : {veh['Brand']}")
            if category == "t":
                print(f"Size   : {veh['Size']}")
            elif category == "l":
                print(f"Maximum Load : {veh['Load']}")
            else:
                print(f"Maximum Passengers : {veh['MaxPassengers']}")

            print(f"Availability for Hire : {'Available' if veh['Available'] else 'Hired'}")
            print()

    def hireVehicle(self,category):
        if category == "c":
            key = "Cars"
            passengers = int(input("Enter the no of Maximum Passengers : "))
            Ac = input("Do you need AC (Y/N) : ").lower() == 'y'

        elif category == "v":
            key = "Vans"
            passengers = int(input("Enter the no of Maximum Passengers : "))
            Ac = input("Do you need AC (Y/N) : ").lower() == 'y'
        elif category == "th":
            key = "Threewheels"
        elif category == "t":
            key = "Trucks"
            size = float(input("Enter the Size of the Truck in Feet : "))

        elif category == "l":
            key = "Lorries"
            Load = float(input("Enter the Maximum Load of the Lorry : "))
        else:
            print("Invalid category")

        available = False
        for veh in self.vehicles[key]:
            if veh["Available"]:
                if category == 't' and veh["Size"] == size:
                    print(f"\nVehicle ID  : {veh['VehicleID']}")
                    print(f"Brand : {veh['Brand']}")
                    print(f"Size : {veh['Size']}")
                    available = True
                    break
                elif category == 'l' and veh["Load"] == Load:
                    print(f"\nVehicle ID  : {veh['VehicleID']}")
                    print(f"Brand : {veh['Brand']}")
                    print(f"Maximum Load : {veh['Load']}")
                    available = True
                    break
                elif category == 'c' and veh["MaxPassengers"] == passengers and veh["Ac"] == Ac:
                    print(f"\nVehicle ID  : {veh['VehicleID']}")
                    print(f"Brand : {veh['Brand']}")
                    print(f"Maximum Passengers : {veh['MaxPassengers']}")
                    available = True
                    break
                elif category == 'v' and veh["MaxPassengers"] == passengers and veh["Ac"] == Ac:
                    print(f"\nVehicle ID  : {veh['VehicleID']}")
                    print(f"Brand : {veh['Brand']}")
                    print(f"Maximum Passengers : {veh['MaxPassengers']}")
                    available = True
                    break
                elif category == 'th':
                    print(f"\nVehicle ID  : {veh['VehicleID']}")
                    print(f"Brand : {veh['Brand']}")
                    print(f"Maximum Passengers : {veh['MaxPassengers']}")
                    available = True
                    break
        else:
            print(f"No Available {key} for your requirements")
        print()
        if available:
            hire  = input("Do you want to hire this Vehicle (Y/N) :").lower() == 'y'
            if hire:
                veh["Available"] = False
                print("You have successfully hired")
                print("You can release the Vehicle from the job using vehicle ID")

        print("====================================================")
    def hireCompleted(self,category):
        if category == "c":
            key = "Cars"
        elif category == "v":
            key = "Vans"
        elif category == "th":
            key = "Threewheels"
        elif category == "t":
            key = "Trucks"
        elif category == "l":
            key = "Lorries"
        else:
            print("Invalid category")

        ID = int(input("Enter the vehicle ID : "))

        for veh in self.vehicles[key]:
            if veh["VehicleID"] == ID and not veh["Available"]:
                print("You Have successfully Release the Vehicle from the job")
                veh["Available"] = True
                break
        else:
            print("The Vehicle that you are going to release, have not hired yet. Please Check the ID Again.  ")
        print("============================================================================================")

cabs = CabService()

while True:
    print("\nWelcome to the cab service")
    print("==========================================================\n")
    print("Available Options : Add Vehicle(1),Remove Vehicle(2),Hire Vehicle(3),Reassign vehicle(4),See Vehicles(5)")
    option = input("Please Enter the Option :")
    print()
    print("Available Vehicle category Cars(C),Vans(V),ThreeWheels(TH),Trucks(T),Lorries(L)")
    category = input("Please Enter the Vehicle Category :").lower()
    print()
    if option == "1":
        cabs.addVehicles(category)
    elif option == "2":
        cabs.removeVehicle(category)
    elif option == "3":
        cabs.hireVehicle(category)
    elif option == '4':
        cabs.hireCompleted(category)
    elif option == "5":
        cabs.showVechicles(category)
    else:
        print("Invalid Input")



