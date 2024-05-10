confirm = int(input('Welcome to the BMI Calculator! Do you want to continue? (1 - yes, 0 - no): '))
if confirm==0:
    exit()
elif confirm==1:
    system = int(input('Which system do you want? (1 - kg-cm, 0 - lb-in: '))
    if system==1:
        weight = int(input('Put your weight (kg): '))
        height = int(input('Put your height (cm): '))
        value = (weight/(height**2))*10000
    elif system==0:
        weight = int(input('Put your weight (lb): '))
        height = int(input('Put your height (in): '))
        value = weight/(height**2)*703
    else:
        print('You put a wrong key!')
        exit()
    print('Your BMI is: ', int(value))
    
else:
    print('You put a wrong key!')
    exit()