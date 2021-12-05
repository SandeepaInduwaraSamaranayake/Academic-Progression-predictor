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

def check_valid_total(total):                                                   # this function will check whether total=120, takes one parameter-total.
    if(total==120):                                                             # if pass+defer+fail is equal to 120 then
        progress_level = sort_progression_outcome(pass_cr,fail_cr)              # call sort_progression_outcome function to get the progression level,store it in progress_level.
        print(progress_level)                                                   # print the progress_level
    else:                                                                       # if total is not equal to 120 then
        print("Total incorrect")                                                # print total is incorrect
        main()                                                                  # takes user to the beginning of the program.


def sort_progression_outcome(Pass,Fail):
    pro_out_1="Progress"                                    # set pro_out_1 to "Progress"
    pro_out_2="Progress (module trailer)"                   # set pro_out_2 to "Progress (module trailer)"
    pro_out_3="Do not Progress – module retriever"          # set pro_out_3 to "Do not Progress – module retriever"
    pro_out_4="Exclude"                                     # set pro_out_4 to "Exclude"
    if(Pass==120):                                          # if pass=120 then
        return pro_out_1                                    # return "Progress" to where the function called.
    elif(Pass==100):                                        # if pass=100 then
        return pro_out_2                                    # return "Progress (module trailer)" to where the function called.
    elif(Fail>=80):                                         # if Fail value>=80 then
        return pro_out_4                                    # return "Exclude" to where the function called.
    else:                                                   # else it should be surely "Do not Progress – module retriever"
        return pro_out_3                                    # return "Do not Progress – module retriever" to where the function called.

def main():                                                       # create a main function to handle main tasks in the program.
    global pass_cr,defer_cr,fail_cr                               # make those vaiables in global scope because we want to access this variables in check_valid_total function.
    pass_cr=input_valid_number("pass")                            # call the input_valid_number function with argument"pass" and store the returned value in pass_cr.
    defer_cr=input_valid_number("defer")                          # call the input_valid_number function with argument"defer" and store the returned value in defer_cr.
    fail_cr=input_valid_number("fail")                            # call the input_valid_number function with argument"fail" and store the returned value in fail_cr.

    total=pass_cr+defer_cr+fail_cr                                # calculate the total of what user entered.
    check_valid_total(total)                                      # call the check_valid_total function with the argument total(previous line we calculated it)

main()                                                            # call the main function(This is the starting point of this program)









