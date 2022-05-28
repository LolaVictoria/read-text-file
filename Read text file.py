# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    with open(filename) as f:
        content = f.read()
    
    return content


def count_words():
    text = read_file_content("story.txt")

    # converting text into a list of words
    words = text.split()

    dictionary = {}

    #Looping through words
    for word in words:
        #Checking how many times a word appears in dictionary
        if(word in dictionary):
            #Incrementing the number of times a word exist by 1
            dictionary[word] += 1

        else:
            dictionary[word] = 1


    return dictionary
    

print(count_words())