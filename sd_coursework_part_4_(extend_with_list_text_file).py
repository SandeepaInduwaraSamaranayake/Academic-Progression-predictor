#!/usr/bin/env python3
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID:20210302        Date: 2021/12/05
def input_valid_number(progression_level="pass"):                                          # create a function(input_valid_number) which accepts one parameter(default=pass)
    while True:                                                                            # create an infinite loop(Run forever untill return usr_respond to main() function)
        try:                                                                               # start a try block because we have to handle exceptions when user enter invalid values
            usr_respond=int(input(f"Please enter your credits at {progression_level} : ")) # get user input, convert it to int, store it in usr_respond
            if(usr_respond>=0 and usr_respond<=120 and (usr_respond%20)==0):               # check whether user's input is in the correct value range.
                return usr_respond                                                         # if user's entered value is in correct range then return the value to the main() function
            else:                                                                          # if user entered out of range value then
                print("Out of range")                                                      # print the message "out of range"
        except ValueError:                                                                 # if ValueError occured in the line which we take user's input then
            print("Integer required")                                                      # print "need an Integer"

progression_data=[]                                                             # related to part 3(use a list to save all progression data).Create an empty list.
filename="progression_data.txt"                                                 # filename is the actual file name of which we are going to store our progression data.
def insert_to_the_list(progress_level,pass_cr,defer_cr,fail_cr):                # Part 3 | extend the program with list.This function will save the progression data to a list.
    progression_data.append([progress_level,pass_cr,defer_cr,fail_cr])          # at the end of the progression_data list, append the data we get from user.so progression_data is a nested list.

def write_text_file():                                                          # this function will write all the progression data to a text file named progression_data_file.txt.
    progression_data_file=open(filename,"w")                                    # open the file in writing mode. progression_data_file is the fileobject we created.
    for data_set in progression_data:                                           # get elements(also lists) from progression_data one by one and store them in data_set.
        ready_to_write = f"{data_set[0]} - {data_set[1]},{data_set[2]},{data_set[3]}\n" # prepare a string to write as a line to the text file, which contains progression data.
        progression_data_file.write(ready_to_write)                             # write the prepared line(ready_to_write) to buffer.
    progression_data_file.flush()                                               # revert changes in buffer to text file.When only flush(), changes will revert to file.
    progression_data_file.close()                                               # close the file connection.
                                                                                # progression_data_file is a local fileobject.It's scope is write_text_file function.
                                                                                # out of this function we can use progression_data_file as fresh variable or object.

def read_text_file():                                                           # This function will read the progression_data.txt and print it's content.
    try:
        progression_data_file = open(filename,"r")                              # open the file in reading mode. progression_data_file is the fileobject we created.
        print(progression_data_file.read())                                     # print the content of progression_data.txt
        progression_data_file.close()                                           # close the file connection.
    except IOError:                                                             # progression_data_file is a local fileobject.It's scope is read_text_file function.
        print("Can't read",filename)                                            # out of this function we can use progression_data_file as fresh variable or object.

def check_valid_total(total):                                                   # this function will check whether total=120, takes one parameter-total.
    if(total==120):                                                             # if pass+defer+fail is equal to 120 then
        progress_level = sort_progression_outcome(pass_cr,fail_cr)              # call sort_progression_outcome function to get the progression level,store it in progress_level.
        print(progress_level)                                                   # print the progress_level
        insert_to_the_list(progress_level,pass_cr,defer_cr,fail_cr)             # all validations finished! call insert_to_the_list() function to save the input progression data to a list.
    else:                                                                       # if total is not equal to 120 then
        print("Total incorrect")                                                # print total is incorrect
        main()                                                                  # takes user to the beginning of the program.

def sort_progression_outcome(Pass,Fail):                    # create a function which accepts three parameters Pass,Defer and Fail.This will sort out the progression level.
    pro_out_1="Progress"                                    # set pro_out_1 to "Progress"
    pro_out_2="Progress (module trailer)"                   # set pro_out_2 to "Progress (module trailer)"
    pro_out_3="Module retriever"                            # set pro_out_3 to "Module retriever"
    pro_out_4="Exclude"                                     # set pro_out_4 to "Exclude"
    if(Pass==120):                                          # if pass=120 then
        add_progress()                                      # call add_progress() function to increment number of students for progress category by 1.
        return pro_out_1                                    # return "Progress" to where the function called.
    elif(Pass==100):                                        # if pass=100 then
        add_trailer()                                       # call add_trailer() function to increment number of students for progress(module trailer) category by 1.
        return pro_out_2                                    # return "Progress (module trailer)" to where the function called.
    elif(Fail>=80):                                         # if Fail value>=80 then
        add_Exclude()                                       # call add_Exclude() function to increment number of students for Exclude category by 1.
        return pro_out_4                                    # return "Exclude" to where the function called.
    else:                                                   # else it should be surely "Do not Progress – module retriever"
        add_retriever()                                     # call add_retriever() function to increment number of students for Do not Progress – module retriever category by 1.
        return pro_out_3                                    # return "Do not Progress – module retriever" to where the function called.

def main():                                                       # create a main function to handle main tasks in the program.
    global pass_cr,defer_cr,fail_cr                               # make those vaiables in global scope because we want to access this variables in check_valid_total function.
    pass_cr=input_valid_number("pass")                            # call the input_valid_number function with argument"pass" and store the returned value in pass_cr.
    defer_cr=input_valid_number("defer")                          # call the input_valid_number function with argument"defer" and store the returned value in defer_cr.
    fail_cr=input_valid_number("fail")                            # call the input_valid_number function with argument"fail" and store the returned value in fail_cr.

    total=pass_cr+defer_cr+fail_cr                                # calculate the total of what user entered.
    check_valid_total(total)                                      # call the check_valid_total function with the argument total(previous line we calculated it)

def add_progress():          # create a function to increment progress by 1.
    global progress          # We use global keyword to read and write progress global variable inside the add_progress() function.
    progress+=1              # Increment progress by 1.(Inside a function we can only ,access global variables,but can't modify global variables without global keyword.)
def add_trailer():           # create a function to increment trailer by 1.
    global trailer           # We use global keyword to read and write trailer global variable inside the add_trailer() function.
    trailer+=1               # Increment trailer by 1.(Inside a function we can only ,access global variables,but can't modify global variables without global keyword.)
def add_retriever():         # create a function to increment retriever by 1.
    global retriever         # We use global keyword to read and write retriever global variable inside the add_retriever() function.
    retriever+=1             # Increment retriever by 1.(Inside a function we can only ,access global variables,but can't modify global variables without global keyword.)
def add_Exclude():           # create a function to increment excluded by 1.
    global excluded          # We use global keyword to read and write excluded global variable inside the add_Exclude() function.
    excluded+=1              # Increment excluded by 1.(Inside a function we can only ,access global variables,but can't modify global variables without global keyword.)

def draw_histogram_horizontal():                                                                                  # crate a function to draw the horizontal histogram.
    print("________________________________________________________________________\nHorizontal Histogram\n ")    # print title
    print(f"Progress  {progress} : "+"*"*progress)                                                                # print progress category student's count.
    print(f"Trailer   {trailer} : "+"*"*trailer)                                                                  # print trailer  category student's count.
    print(f"Retriever {retriever} : "+"*"*retriever)                                                              # print retriever category student's count.
    print(f"Excluded  {excluded} : "+"*"*excluded)                                                                # print excluded category student's count.
    print(f"\n{sum([progress, trailer, retriever, excluded])} outcomes in total")                                 # print total no of students.

def draw_histogram_vertical():                                                                                   # crate a function to draw the vertical histogram.
    print("________________________________________________________________________\nVerticle Histogram(List extension with Text file )\n")    # print title
    titles=["Progress","Trailer","Retriever","Excluded"]                # store progress outcomes in a list named titles.
    data=[progress,trailer,retriever,excluded]                          # store progress outcome data in a list named data(no of students belong to each category)
    print(f"{titles[0]:<12}{titles[1]:<11}{titles[2]:<13}{titles[3]}")  # print head titles in the vertical histogram.

    def print_star(space):                                              # This print_star() function will print the stars when call this function.(a nested function)
        print(f"{'*':>{space}}",end='')                                 # And hold the cursor in same line

    def print_space(space):                                             # This print_space() function will print spaces when call this function.(a nested function)
        print(f"{' ':>{space}}",end='')                                 # And hold the cursor in the same line

    def stars():                                                        # This function will handle the number of spaces between two stars and finally call the print_star function(a nested function)
        indentation=[5,11,12,12]                                        # This is the list of no of spaces we are going to place between stars.
        for j in range(4):                                              # create a for loop to check which category this related to and decide indentation length according toit.
            if(i==j):                                                   # if catogery index(i) equals to j(0-3).
                print_star(indentation[j])                              # set the space value as parameter and call the print_star function.
    def space():                                                        # This function will handle the number of spaces between two spaces and finally call the print_star functio(a nested function)
        indentation=[5,11,12,12]                                        # This is the list of no of spaces we are going to place between spaces.
        for j in range(4):                                              # for loop to check which category this related to and decide indentation length according toit
            if(i==j):                                                   # if catogery index(i) equals to j(0-3).
                print_space(indentation[j])                             # set the space value as parameter and call the print_space function.

    for line in range(1,max(data)+1):                                   # This for loop will basically handle the process of printing line by line.
        for i in range(4):                                              # This for loop will handle the printing according to the categories like progress,trailer and so on.
            if(data[i]>=line):                                          # check if each category(progress,trailing...) value is greater than or equal to line number.
                stars()                                                 # if yes then call stars() function to print stars.
            else:                                                       # if category(progress,trailing...) value is less than to line number.
                space()                                                 # call space() function to print space.
        print("\n")                                                     # after printing stars & spaces for all four categories goto next line and next iteration will happen.
    print(f"\n{sum([progress,trailer,retriever,excluded])} outcomes in total\n________________________________________________________________________") # print total no of students.


progress=trailer=retriever=excluded=0                             # make progress,trailer,retriever,excluded variables with value 0 in global scope.

print("Staff version with Histogram\n")                           # print introduction.
while True:                                                       # infinite while loop to handle entire looping process.
    main()                                                        # call main function.
    usr_option=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")   # get user_option as his like,and store in usr_option.
    if(usr_option.lower()=="y"):                                  # check the lower case of user's input is equal to "y"
        print("")                                                 # if yes then print a blank line to seperate it from previous content,
        continue                                                  # and go to the beginning of the loop to continue normal procedure again.
    elif(usr_option.lower()=="q"):                                # check the lower case of user's input is equal to "q"
        draw_histogram_horizontal()                               # if yes then call draw_histogram_horizontal() function to draw the horizontal histogram.
        draw_histogram_vertical()                                 # call draw_histogram_vertical() function to draw the vertical histogram.
        break                                                     # break the loop and stop the program after drawing histogram.
    else:                                                         # if user inputs anything other than y or q.
        print("Not a valid option")                               # print not a valid option.
        break                                                     # break the while loop.

write_text_file()                                                 # call write_text_file() function to write the content.
read_text_file()                                                  # call read_text_file() function to read the text file and print the content.










