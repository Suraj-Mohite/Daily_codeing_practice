# Q.1	Consider the following situation - In a building there can be N number of floors, to reach on a particular floor we just have stair case. if floor number is even then there would be 10*2+no of floor steps in stair case, if floor number is odd then there would 10*2+10+1 steps. Only floor number 6 is such a floor which has 22 steps. If building has 12 floor, write a program which would help you to find out how many steps would be required to reach any floor.

# Sample Input 1 :- 5                                 Sample Output 1 :- 139
# Sample Input 2 :- 10                               Sample Output 2 :- 281


# def numOfStepsToReach(num):
#     try:
#         if num>12:
#             return "Building has only 12 floor"
#         if num<0 or type(num)==bool:
#             raise("Invalid Input")

#         steps=0
#         for floor in range(1,num+1):
#             if floor==6:
#                 steps+=22
#             elif floor%2==0:
#                 steps+=10*2+floor
#             else:
#                 steps+=10*2+10+1
#         return steps
#     except:
#         return("Invalid Input")

# if __name__=='__main__':
    # Test Cases
    # print(numOfStepsToReach(5))
    # print(numOfStepsToReach(10))
    # print(numOfStepsToReach(0)) 
    # print(numOfStepsToReach(40)) #if input is Beyond size of Building
    # print(numOfStepsToReach(5.23)) #input is Float
    # print(numOfStepsToReach("String")) #input is String
    # print(numOfStepsToReach(True)) #input is Boolean
    # print(numOfStepsToReach(-56)) #if input is invalid (negative value)




# Q.2	Person A consume almost 1320 calories per day B eats almost 1550 Calories per day and C consume almost 1300 calories per day. Calories chart is as per follow -
# Food	Qty (in grams)	Calories
# Rice (Brown)	100	353.7
# Wheat flour	100	320.2
# Bengal gram, whole	100	287
# Cabbage,	100	21.5
# Peas, dry	100	303.2
# Rajma, red	100	299.2
# Red gram, dal	100	330.

# Note the condition
# 1. Each person takes atleast 3 item per day, it may be same for all 30 days e.g.

# Diet plan for A -

# Red gram Or Dal 300 gm per day Rajma Red 100 gm,
# Cabbage 100 gm.
# Its how he gets almost 1320 Calories and for him only, required grocery for 30 days will be - Red Gram – 9000 gm
# Rajma Red – 3000 gm Cabbage – 3000 gm

# Write down a program which accept days and tell you, Quantity of grocery required for A, B and C. System will ask Diet plan for A, B & C. Then will ask for days you want to calcualate and then will show the ouput like explained below

# Grocerry for A

# Red Gram – 9000 gm Rajma Red – 3000 gm Cabbage – 3000 gm


# Sample Input 1 :-   A
# 			        30                                 
# 		 	         Rice
# 			         Cabbage 
# 			         Red Gram Dal

# Sample Output 1 :- Grocerry for A 		
# 			            Rice – 6000gm   Cabbage – 6000gm   Red Gram Dal – 3000gm
# 	(As total calories are under 1320 calories/day for A [ totalCalories / 30 <= 1320 ] )


# personObj={
#     'A':1320,
#     'B':1550,
#     'C':1300
# }

# calPer100gm={
#     'Rice (Brown)':353.7,
#     'Wheat flour':320.2,
#     'Bengal gram whole'	:287,
#     'Cabbage'	:21.5,
#     'Peas, dry':303.2,
#     'Rajma, red':299,
#     'Red gram, dal':330
# }

# def perDayCal(person,days,*items):
#     person=person.upper()
#     cal=personObj[person]
#     perday={}
    
#     while True:
#         round=0
#         for item in items:
#             if calPer100gm[item]<=cal:
#                 perday[item]=perday.get(item,0)+100
#                 cal-=calPer100gm[item]
#             else:
#                 round+=1
#         if round==len(items):
#             break
    
#     # print(perday)
#     # print(cal)
#     for key in perday:
#         perday[key]*=days
#     return perday

# print(perDayCal('c',30,'Rice (Brown)','Wheat flour','Red gram, dal'))


class dietPlan:
    personObj={
        'A':1320,
        'B':1550,
        'C':1300
    }

    calPer100gm={
        'Rice (Brown)':353.7,
        'Wheat flour':320.2,
        'Bengal gram whole'	:287,
        'Cabbage'	:21.5,
        'Peas, dry':303.2,
        'Rajma, red':299,
        'Red gram, dal':330
    }
    def perDayCal(self,person,days,*items):
        try:
            person=person.upper()
            cal=self.personObj[person]
            perday={}
            
            while True:
                round=0
                for item in items:
                    if self.calPer100gm[item]<=cal:
                        perday[item]=perday.get(item,0)+100
                        cal-=self.calPer100gm[item]
                    else:
                        round+=1
                if round==len(items):
                    break
            
            for key in perday:
                perday[key]*=days
            return perday
        except:
            return "Invalid Input"


if __name__=="__main__":
    obj=dietPlan()
    print(obj.perDayCal('b',30,'Rice (Brown)','Wheat flour','Red gram, dal','Cabbage'))