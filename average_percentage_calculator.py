#percentage and average calculator.
n=int(input('enter number of subjects you have'))
sum=0
for i in range(1,n+1):
	subject=input('enter subject name')
	mark=int(input(f'enter {subject}  mark :'))
	sum+=mark
def avg():
	avg=sum/n
	print('your average marks is :',avg)
def percentage():
	total=int(input('please enter the total marks for which the exam is conducted :'))
	percentage=(sum/total)*100
	print('percentage you scored is :',percentage)	
choice=input('do you want to calaculate average or percetage of your mark ?(average/percentage)')
if choice.lower()=='average':
		avg()
elif choice.lower()=='percentage':
		percentage()
else:
		print('please check your spelling and try again' )		