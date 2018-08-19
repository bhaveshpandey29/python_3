print("Welcome to the search and replace system".center(100,"*"))
user_para = str(input("Please enter the paragraph: "))
search_res = []
replaced_wrd = {}
print("Thank you.Please choose the operations/options given below:\n")
while True:
    user_input = int(input("1.Print Paragraph\n2.Search\n3.Replace\n4.Recent searchs\n5.Recent replaced words\n6.Exit\n"))
    if user_input == 1:
        print(user_para)
    elif user_input == 2:
        search_input = str(input("Please enter the word you wish to search:"))
        if user_para.find(search_input) == -1:
            print("Sorry the word is not found")
        else:
            print(f"The word {search_input} is found at posotion {user_para.find(search_input)+1}")
            search_res.append(search_input)            
    elif user_input == 3:
        replace_input_one = str(input("Please enter the word you wish to replace:"))
        replace_input_two = str(input(f"Please enter the word you wish to replace with {replace_input_one}:"))        
        if user_para.find(replace_input_one) == -1:
            print("Sorry the word is not found")
        else:
            user_para = user_para.replace(replace_input_one,replace_input_two)
            print(f"The word {replace_input_two} is now added to the paragraph at location {user_para.find(replace_input_two)+1}")
            replaced_wrd[replace_input_one]=replace_input_two
    elif user_input == 4:
        print("Here are the recent searches:")
        print(search_res[::-1]) #printing backward
    elif user_input == 5:
        print("Here are the words which are replaced:")
        print(replaced_wrd)
    elif user_input == 6:
        print("Thank you for using our services. GoodBye!")
        break