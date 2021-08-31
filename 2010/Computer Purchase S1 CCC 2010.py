num_of_comp=int(input())

all_comp=[]

for current_comp in range(num_of_comp):
    comp=input().split()

    name=comp[0]
    performance=(2*int(comp[1]))+(3*int(comp[2]))+(int(comp[3]))

    all_comp.append([name,performance])

all_comp=sorted(all_comp)
all_comp=sorted(all_comp,key=lambda x:x[1],reverse=True)

print(all_comp[0][0])

if (len(all_comp)>1):
    print(all_comp[1][0])
