#Het Patel
#J4 2011 Problem - Boring Business

def allowed_to_drill(point_x, point_y): #I defined a function called allowed_to_drill that takes the two parameters of where the drill is on the grid, and determines whether its safe to drill there
    if boring_hole[point_y] [point_x] == ['x']:      #I check if the position the drill is in has an 'x' on it, if it does its not safe therefore returning a false
        return False
    else:
        return True  #otherwise it returns a True so that the code in the loop will run

boring_hole = []
user_points_list = [] #I define two lists, boring_hole is a 2d 400 by 200 list laying out the entire map of where the drill could land and the other list will hold all the points the drill visits
drill_x = 198 #means -1
drill_y = 4 #means -5              #i have the starting point of the drill, converted to a list-index format

for y in range(200):
    boring_hole.append([])
                                   #I use these for loops to create the massive 2D LIST that will contain the entire map of where the drill could go
    for x in range(400):
        boring_hole[y].append([])
        
boring_hole[0][199].append("x")
boring_hole[1][199].append("x")
boring_hole[2][199].append("x")
boring_hole[2][200].append("x")
boring_hole[2][201].append("x")
boring_hole[2][202].append("x")
boring_hole[3][202].append("x")
boring_hole[4][202].append("x")
boring_hole[4][203].append("x")
boring_hole[4][204].append("x")
boring_hole[3][204].append("x")
boring_hole[2][204].append("x")
boring_hole[2][205].append("x")
boring_hole[2][206].append("x")         #This code is used to initalize all the points where the drill can't cross. The 'x' represnts the location of where the drill already was
boring_hole[3][206].append("x")
boring_hole[4][206].append("x")
boring_hole[5][206].append("x") 
boring_hole[6][206].append("x")
boring_hole[6][205].append("x")
boring_hole[6][204].append("x")
boring_hole[6][203].append("x")
boring_hole[6][202].append("x")
boring_hole[6][201].append("x")
boring_hole[6][200].append("x")
boring_hole[6][199].append("x")
boring_hole[6][198].append("x")
boring_hole[5][198].append("x")
boring_hole[4][198].append("x")

while True:   #I have a main while loop that will keep iterating as long as the drill doesn't cross itself or the user doesn't enter a 'q'

    user_input = (input("Enter the direction (u, d, r or l) followed by the positive length: ")).split()  #I get the input and split it by space
    print("")

    if len(user_input) != 2:
        print("Please follow the directions noted in the input statement.")  #I have error checks for if the user doesn't enter the right message
        print("")

    else:
            
        direction = user_input[0]    #I initalize many variables to store the direction of the drill, the length
        length = int(user_input[1])
        not_dangerous = True #a boolean value (a sentinel) for if the drill is allowed to cross the point the user inputted and the original points of where the drill is
        original_drillx = drill_x 
        original_drilly = drill_y #original points of the drill in each iteration
        
        if direction.lower() == "q":
            break       #if the user inputs a 'q' the code will break out the loop

        elif direction not in "rudl":
            print("Please enter a valid Direction.")
            print("")                          
                                            #More codes for error checks to help the user if they entered something wrong
        elif length <= 0:
            print("Please enter a positive Integer.")
            print("")
            
        else:

            if direction.lower() == "u": #code for the up direction

                if drill_y - length <= 0:
                    print("You can't go over the surface! Please Try Again.")             #error checking for if the drill goes over the surface
                    print("")
                else:                   
                    for point in range(length): #i have a loop to go through all the points the drill will cross in this direction

                        if allowed_to_drill(drill_x, drill_y - 1):  

                            drill_y -= 1 #if the drill doesn't cross any previous points it will decrease the y-value of the drill by 1 each time 

                            boring_hole[drill_y][drill_x].append("x") #then it will append an x to that location on the boring_hole 2d list to signify that the drill passed this point

                        else:
     
                            not_dangerous = False  #if the drill did pass through one of the points, it will set the boolean (sentinel) to False and break out the for loop
                            break

                    if not_dangerous:

                        user_points_list.append( str(original_drillx - 199) + " " + str((original_drilly - length + 1) * -1) + " Safe")  #if the drill didn't cross its past it will append the following to the user_points_list and stay in the loop

                    else:
                        user_points_list.append( str(original_drillx - 199) + " " + str((original_drilly - length + 1) * -1) + " DANGER!!!") #otherwise it will append the following to the user_points_list and break out the loop
                        break
                
            if direction.lower() == "d":

                if drill_y + length > 200:
                    print("Please stay below 200 units. ")    #I have an error check if the drill goes below 200 units
                    print("")
                else:
                        
                    for point in range(length):

                        if ( allowed_to_drill(drill_x, drill_y+1) ):
                            
                            drill_y += 1                                     #Does the same as the code for the 'up' direction but it does everything for the 'down' direction
                            boring_hole[drill_y][drill_x].append("x")

                        else:
                            not_dangerous = False
                            break

                    if not_dangerous:

                        user_points_list.append( str(original_drillx - 199) + " " + str((original_drilly + length + 1) * -1) + " Safe" ) #appends the following to the list and stays in the loop

                    else:
                        user_points_list.append( str(original_drillx - 199) + " " + str((original_drilly + length + 1) * -1) + " DANGER!!!" ) #appends the following and breaks out the loop
                        break
                    
            if direction.lower() == "r":

                if drill_x + length > 400:
                    print("Please don't go over 200 units. ")
                    print("")         #Error checking

                else:
                        
                    for point in range(length):

                        if ( allowed_to_drill(drill_x + 1, drill_y) ):
                                                                             #Does the same as the code for the 'up' direction but it does everything for the 'right' direction
                            drill_x += 1
                            boring_hole[drill_y][drill_x].append("x")

                        else:
                            not_dangerous = False   #breaks out the loop if the drill crosses its path
                            break

                    if not_dangerous:

                        user_points_list.append( str((original_drillx + length) - 199) + " " + str((original_drilly + 1) * -1) + " Safe" )   #appends the following to the list and stays in the loop

                    else:
                        user_points_list.append( str((original_drillx + length) - 199) + " " + str((original_drilly + 1) * -1) + " DANGER!!!" ) #appends the following and breaks out the loop
                        break
                    
            if direction.lower() == "l":

                if drill_x - length < -1:
                    print("please don't go over 200 units. ") #error checking so that the code doesn't go over 200 units
                    print("")

                else:
                        
                    for point in range(length):

                        if ( allowed_to_drill(drill_x - 1, drill_y) ):
                             
                            drill_x -= 1                           #Does the same as the code for the 'up' direction but it does everything for the 'left' direction
                            boring_hole[drill_y][drill_x].append("x")

                        else:
                            not_dangerous = False #breaks out the loop if the drill crosses its path
                            break

                    if not_dangerous:

                        user_points_list.append( str((original_drillx - length) - 199) + " " + str((original_drilly + 1) * -1) + " Safe" ) #appends the following to the list and stays in the loop

                    else:
                        user_points_list.append( str((original_drillx - length) - 199) + " " + str((original_drilly + 1) * -1) + " DANGER!!!" ) #appends the following and breaks out the loop
                        break



for coordinate in user_points_list:
    print(coordinate) #prints all the points the drill landed at, followed by if its safe or dangerous

