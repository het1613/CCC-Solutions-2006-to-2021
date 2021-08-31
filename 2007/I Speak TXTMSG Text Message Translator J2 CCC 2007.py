text=input('Enter phrase: ')

shortform=['CU',':-)',':-(',';-)',':-P','TA','CCC','CUZ','TY','YW','TTYL']
longform=['see you','I’m happy','I’m unhappy','wink','stick out my tongue','totally awesome','Canadian Computing Competition','because','thank-you','you’re welcome','talk to you later']

new_text=text

if text in shortform:
    index=shortform.index(text)
    new_text=longform[index]
    
print(new_text)


