#Boring Business
#Het Patel
#ICS4U0
#9/18/20

def error_checking(direction,length,current_x,current_y):

    message=''
    flag=True

    if (direction not in 'dulrq'):
        message='Invalid direction. Please only use u, d, r or l.\n'
        flag=False

    elif ((direction=='d') and ((current_y-length)<-200)):
        message='Invalid length. Length goes beyond 200 units down. Please try again.\n'
        flag=False

    elif ((direction=='u') and ((current_y+length)>=0)):
        message='Invalid length. Length goes above ground. Please try again.\n'
        flag=False

    elif ((direction=='l') and ((current_x-length)<-200)):
        message='Invalid length. Length goes beyond 200 units left. Please try again.\n'
        flag=False

    elif ((direction=='r') and ((current_x+length)>200)):
        message='Invalid length. Length goes beyond 200 units right. Please try again.\n'
        flag=False

    return message, flag


exsisting_boring_holes=[]

exsisting_boring_holes.append([0,-1])
exsisting_boring_holes.append([0,-2])
exsisting_boring_holes.append([0,-3])
exsisting_boring_holes.append([1,-3])#
exsisting_boring_holes.append([2,-3])
exsisting_boring_holes.append([3,-3])
exsisting_boring_holes.append([3,-4])#
exsisting_boring_holes.append([3,-5])
exsisting_boring_holes.append([4,-5])#
exsisting_boring_holes.append([5,-5])
exsisting_boring_holes.append([5,-4])#
exsisting_boring_holes.append([5,-3])
exsisting_boring_holes.append([6,-3])#
exsisting_boring_holes.append([7,-3])
exsisting_boring_holes.append([7,-4])#
exsisting_boring_holes.append([7,-5])
exsisting_boring_holes.append([7,-6])
exsisting_boring_holes.append([7,-7])
exsisting_boring_holes.append([6,-7])#
exsisting_boring_holes.append([5,-7])
exsisting_boring_holes.append([4,-7])
exsisting_boring_holes.append([3,-7])
exsisting_boring_holes.append([2,-7])
exsisting_boring_holes.append([1,-7])
exsisting_boring_holes.append([0,-7])
exsisting_boring_holes.append([-1,-7])
exsisting_boring_holes.append([-1,-6])#
exsisting_boring_holes.append([-1,-5])

current_x=-1
current_y=-5

all_output_messages=[]

status='safe'

while (status!='DANGER'):

    while True:
        user_input=input('Enter the direction (u, d, r or l) followed by the positive length: ').split()

        direction=user_input[0]
        length=int(user_input[1])

        message, flag = error_checking(direction,length,current_x,current_y)

        print(message)

        if (flag):
            break

    if (direction=='q'):
            break

    for current_pos in range(length):
        if (direction=='u'):
            current_y+=1

        elif (direction=='d'):
            current_y-=1

        elif (direction=='r'):
            current_x+=1

        elif (direction=='l'):
            current_x-=1

        if ([current_x,current_y] in exsisting_boring_holes):
            status='DANGER'
        else:
            exsisting_boring_holes.append([current_x,current_y])

    all_output_messages.append('{0} {1} {2}'.format(current_x,current_y,status))

print('\n'.join(all_output_messages))
