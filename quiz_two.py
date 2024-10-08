#Data Storage and Printings
#Name of Groupmates

Mem_1 = "Adrian Cedric Calindas"
Mem_2 = "Chryson M. Valdez "
Mem_3 = "Sharmaine N. Gasatan "



#AGE of the members in Vanilla
Age_1 = "20"
Age_2 = "20"
Age_3 = "19"

conAge1 = int(Age_1)
conAge2 = int(Age_2)
conAge3 =int(Age_3)

Allowance_1 = float(500.0)
Allowance_2 = float(1000.0)
Allowance_3 = float(500.0)


#Name of the Team
TeamName = "Vanilla"

print(TeamName, Mem_1 , "his age is " , Age_1, "allowance per week is " , Allowance_1)
print (TeamName, Mem_2 , "his age is " , Age_2, "allowance per weeek is " , Allowance_2)
print(TeamName, Mem_3, "her age is " , Age_2, "allowance per week  " , Allowance_3)

namelen1 = len(Mem_1)
namelen2 = len(Mem_2)
namelen3 = len(Mem_3)

print("Member 1 consists of", namelen1 , "characters")
print("Member 2 consists of", namelen2 , "characters")
print("Member 3 consists of", namelen3 , "characters")

result1 =(conAge1 + conAge2 + conAge3)
print(result1)
result2 =(conAge1 - conAge2 - conAge3)
print(result2)

prod1=(conAge1 * Allowance_1 )
prod2=(conAge2 * Allowance_2)
prod3=(conAge3 * Allowance_3)

print(prod1)
print(prod2)
print(prod3)


# COmparison of the length
 
lengthname1=(namelen1 - namelen2)
lengthname2=(namelen2 - namelen3)

print(lengthname1)
print(lengthname2)
 



