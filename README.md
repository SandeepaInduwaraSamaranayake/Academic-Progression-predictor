# Academic-Progression-predictor
This is a python program to predict progression outcomes at the end of each academic year <br><br> 
Progression outcomes as defined by the University regulations(see the table).<br><br>
![progression_outcomes](https://user-images.githubusercontent.com/95087710/188074648-f6bae0e5-0160-4379-bbce-2debe3dfb9cd.PNG)<br><br>
## Part 1 - Main Version (Student & Staff versions)<br><br>
sd_coursework_part_1_(Base_program-Student_version).py ---------> for students<br>
sd_coursework_part_1_(Main_version-horizontal_histogram).py ----> for staff<br>
1) The program allows students to predict their progression outcome at the end of each academic year. The program prompt for the number of credits at pass,
   defer and fail and then display the appropriate progression outcome for an individual student (i.e., progress, trailing, module retriever or exclude).<br><br>
   
2) Validation<br><br>
-- The program display ‘Integer required’ if a credit input is the wrong data type.<br>
-- The program display ‘Out of range’ if credits entered are not in the range 0, 20, 40, 60, 80, 100 and 120.<br>
-- The program display ‘Total incorrect’ if the total of the pass, defer and fail credits is not 120.<br>
-- An example of the program running with user input (shown in bold):<br><br>

Please enter your credits at pass: <b>p</b><br>
Integer required<br>
Please enter your credits at pass: <b>140</b><br>
Out of range.<br>
Please enter your credits at pass: <b>100</b><br>
Please enter your credit at defer: <b>40</b><br>
Please enter your credit at fail: <b>20</b><br>
Total incorrect.<br>
Please enter your credits at pass: <b>100</b><br>
Please enter your credit at defer: <b>20</b><br>
Please enter your credit at fail: <b>0</b><br>
Progress (module trailer)<br><br>

3) Multiple Outcomes & Histogram<br><br>
-- The program loops to allow a staff member to predict progression outcomes for multiple students.<br>
-- The program prompts for credits at pass, defer and fail and display the appropriate progression for each individual student until the staff member user enters ‘q’ to quit. Optionally you can use an input of ‘y’ to continue.<br>
-- When ‘q’ is entered, the program produces a ‘histogram’ where each star represents a student who achieved a progress outcome in the category range: progress, trailing, module retriever and exclude. The histogram should relate to the data input entered by the staff member during the program run and work for any number of outcomes.<br>
-- Display the number of students for each progression category and the total number of students.<br>
-- Example of a program run and input (in bold). Note: program exit on ‘q’ to quit. ‘y’ to continue.<br><br>

Staff Version with Histogram<br>
 
Enter your total PASS credits: <b>120</b><br>
Enter your total DEFER credits: <b>0</b><br>
Enter your total FAIL credits: <b>0</b><br>
Progress<br>
Would you like to enter another set of data?<br>
Enter 'y' for yes or 'q' to quit and view results: <b>y</b><br>
Enter your total PASS credits: <b>100</b><br>
Enter your total DEFER credits: <b>0</b><br>
Enter your total FAIL credits: <b>20</b><br>
Progress (module trailer)<br>
Would you like to enter another set of data?<br>
Enter 'y' for yes or 'q' to quit and view results: <b>y</b><br>
Enter your total PASS credits: <b>80</b><br>
Enter your total DEFER credits: <b>20</b><br>
Enter your total FAIL credits: <b>20</b><br>
Module retriever<br>
Would you like to enter another set of data?<br>
Enter 'y' for yes or 'q' to quit and view results: <b>y</b><br>
Enter your total PASS credits: <b>60</b><br> 
Enter your total DEFER credits: <b>0</b><br>
Enter your total FAIL credits: <b>60</b><br>
Module retriever<br>
Would you like to enter another set of data?<br>
Enter 'y' for yes or 'q' to quit and view results: <b>y</b><br>
Enter your total PASS credits: <b>40</b><br> 
Enter your total DEFER credits: <b>0</b><br>
Enter your total FAIL credits: <b>80</b><br>
Exclude<br>
Would you like to enter another set of data?<br>
Enter 'y' for yes or 'q' to quit and view results: <b>q</b><br>
---------------------------------------------------------------<br>
Horizontal Histogram<br>
Progress 1 : *<br>
Trailer 1 : *<br>
Retriever 2 : **<br>
Excluded 1 : *<br>
5 outcomes in total.<br>
----------------------------------------------------------------<br><br>

## Part 2 - Vertical Histogram (extension) ( sd_coursework_part_2_(vertical_histogram).py )<br><br>
-- Extend version of part 1 program to add a vertical histogram (stars in a category should go downwards), e.g.;<br><br>
![histogram](https://user-images.githubusercontent.com/95087710/188083308-dec44233-a50a-43fb-b189-5af8f8e8d1fe.PNG)<br><br>
## Part 3 - List/Tuple/Directory (extension) ( sd_coursework_part_3_(extend_with_list).py )<br><br>
-- Extended solution, so that the program uses Python to save the input progression data to a list, tuple or directory. Then access the stored data from the list, tuple, directory and print the data in the following format below.<br><br>
 
Output: The following should display after the histogram(s)<br><br>
Progress - 120, 0, 0<br>
Progress (module trailer) - 100, 0, 20<br> 
Module retriever - 80, 20, 20<br>
Module retriever - 60, 0, 60<br>
Exclude – 40, 0, 80<br><br>

## Part 4 - Text File (extension) ( sd_coursework_part_4_(extend_with_list_text_file).py )<br><br>
-- This script will save input progression data to a text file. Later in the program, access the stored data and 
print out as shown below. Example output (with data from text file):<br><br>

Progress - 120, 0, 0<br>
Progress (module trailer) - 100, 0, 20<br> 
Module retriever - 80, 20, 20<br>
Module retriever - 60, 0, 60<br>
Exclude – 40, 0, 80<br>

