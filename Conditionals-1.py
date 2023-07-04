# Commission calculation
# Find the commission amount on the basis of sales amount as per the following conditions.

# Comission : 

# Sales amount(rs)			
# 0-1000	  		5%     	
# 1001-2000			10%   	
# >2000				12%   

sales = int(input("Enter the sales amount : "))

if sales < 1000 :
    com = sales*5/100
    print("The commition is : ",com)
elif sales > 1000 & sales < 2000 :
    com = sales*10/100
    print("The commition is : ",com)
else :
    com = sales*12/100
    print("The commiton is : ",com)
    
