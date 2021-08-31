num_of_letters=int(input())

letters=[]
binary=[]

for current_letter in range(num_of_letters):
    seq=input().split()

    letters.append(seq[0])
    binary.append(seq[1])

binary_seq=input()

print(letters)
print(binary)
text=''

pos1=0

while (pos1<len(binary_seq)):

    pos2=0
    while True:
        if (binary_seq[pos1:].startswith(binary[pos2])):
            break
        pos2+=1

    text+=letters[pos2]

    pos1+=len(binary[pos2])

print(text)
