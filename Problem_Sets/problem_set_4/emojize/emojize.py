import emoji

request = input("Input: ")


split_request = request.split(" ")

for word in split_request:
    if ":" in word:
        print(emoji.emojize(word,language = 'alias'),end = " ")
    
    else:
        print(word, end = " ")
