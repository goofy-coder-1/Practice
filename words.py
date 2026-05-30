def user_Input():
    while True:
        try:
            sentence = input("Enter your sentence: ")
            return sentence
        except ValueError:
            print("Oops! You input something wrong")


user_sentence = user_Input()
block = user_sentence.split()
sentence_box = []
initial_letter = input("What's the initial letter?: ")

def sentence_logic(word_list, target_letter):
    for word in word_list:
        if word[0] == target_letter.upper() or word[0] == target_letter.lower():
            sentence_box.append(word)
            
    output = ', '.join(sentence_box)
    
    print(f"Words starting with '{target_letter}': {output}")

# Call the function with both required inputs
sentence_logic(block, initial_letter)