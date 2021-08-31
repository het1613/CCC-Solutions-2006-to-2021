num_of_boxes=int(input('Enter number of boxes: '))

boxes=[]

for iteration in range(num_of_boxes):
    current_box=sorted([int(dimention) for dimention in input('Enter box dimentions: ').split()])

    current_box.append(current_box[0]*current_box[1]*current_box[2])
        
    boxes.append(current_box)

boxes=sorted(boxes, key=lambda x:x[3])


num_of_items=int(input('Enter number of items: '))

items=[]

for iteration in range(num_of_items):
    current_item=sorted([int(dimention) for dimention in input('Enter item dimentions: ').split()])
    
    items.append(current_item)

output=[]

print(boxes)
print(items)

for current_item in items:
    
    status='Item does not fit.'
    
    for current_box in boxes:
        
        if ((current_item[0]<=current_box[0]) and (current_item[1]<=current_box[1]) and (current_item[2]<=current_box[3])):
            status=str(current_box[3])
            break

    output.append(status)

print('\n'.join(output))

