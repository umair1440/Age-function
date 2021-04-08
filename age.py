n1 = str(input("Enter the name of first person: "))
a1 = float(input("Enter the age of first person: "))
n2 = str(input("Enter the name of second person: "))
a2 = float(input("Enter the age of second person: "))
n3 = str(input("Enter the name of third person: "))
a3 = float(input("Enter the age of third person: "))
if a1 > a2 and a1 > a3:
	if a2 < a1 and a2 < a3:
		print(str(n1)+" is elder then "+ str(n2)+" & "+str(n3)+"\n"+n2+" is younger then "+str(n2)+" & "+str(n3))
	elif a3 < a1 and a3 < a2:	
		print(str(n1)+" is elder then "+ str(n2)+" & "+str(n3)+"\n"+n3+" is younger then "+str(n1)+" & "+str(n2))


																#  first one 
elif a2 > a3 and a2 > a1:
	if a1 < a3 and a1 < a2:
		print(str(n2)+" is elder then "+ str(n1)+" & "+str(n3)+"\n"+n1+" is younger then "+str(n2)+" & "+str(n3))
	elif a3 < a1 and a3 < a2:	
		print(str(n2)+" is elder then "+ str(n1)+" & "+str(n3)+"\n"+n3+" is younger then "+str(n1)+" & "+str(n2))


																# second one

elif a3 > a1 and a3 > a2:
	if a1 < a3 and a1 < a2:
		print(str(n3)+" is elder then "+ str(n1)+" & "+str(n2)+"\n"+n1+" is younger then "+str(n2)+" & "+str(n3))
	elif a2 < a1 and a2 < a3:	
		print(str(n3)+" is elder then "+ str(n1)+" & "+str(n2)+"\n"+n2+" is younger then "+str(n1)+" & "+str(n3))


																# third one


