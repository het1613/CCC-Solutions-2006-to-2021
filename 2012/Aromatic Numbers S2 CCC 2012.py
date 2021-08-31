aromatic_seq=input()

roman='IVXLCDM'
base=[1,5,10,50,100,500,1000]

previous_roman=9999999999
total_sum=0

for pos in range(0,len(aromatic_seq)-1,2):
    arabic=int(aromatic_seq[pos])
    current_roman=base[roman.index(aromatic_seq[pos+1])]
    current_pair_total=(arabic)*(current_roman)

    total_sum+=current_pair_total

    if (current_roman>previous_roman):
        total_sum-=(2*previous_pair_total)

    previous_roman=current_roman
    previous_pair_total=current_pair_total

print(total_sum)
        
