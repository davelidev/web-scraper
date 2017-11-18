def compute_final (marks):
    '''(str) ->float
    extracts the marks and the corresponding weight from a string and computes the final mark.
    >>> compute_final ("[100, 5], [80, 10], [70 , 5], [60 , 30], [70, 20], [0, 10], [60, 20]")
    60.5
    >>> compute_final("[90, 5], [100, 10], [50 , 5], [60 , 30], [70, 20], [50, 10], [70, 20]")
    68.0
    '''
    # remove [] from the string
    marks = marks.replace('[', "")
    marks = marks.replace(']', "")
    #convert the string into a list 
    marks_list = marks.split(sep = ',')
    #compute the final mark
    final = 0
    for index in range (0, len(marks_list), 2):
        final += float(marks_list[index])* float(marks_list[index+1]) /100
    return final

def print_to_file (info, output_file_handle):
    '''(list, io.TextIOWrapper) -> None
    creates a transcaript by writing stuent information into a file. 
    >>> print_to_file (['100', ' John', ' CSCA08', ' Introduction to Computer Science I', 60.5], file_handle)
    StudentName: John    Student No: 100
    ------------------------------------------------------
    CSCCA08     Introduction to Computer Science I    60.5
    ------------------------------------------------------
    average = 60.5
    '''
    # write the title
    output_file_handle.write("StudentName: " + info[1] + "\t" + "Student No: " + info[0]+"\n")
    # draw a line
    tab_len = 4
    line_length = len(info[2]) + len(info[3]) +len(str(info[4])) + 2*tab_len 
    output_file_handle.write("-" * line_length +"\n")    
    # write student info
    output_file_handle.write(info[2] + "\t" + info[3]+"\t" + str(info[4])+ "\n")    
    # draw a line
    output_file_handle.write("-" * line_length+"\n")    
    # write the average
    output_file_handle.write("Average = " + str(info[4])+"\n\n\n")
    
    
    

if (__name__ == "__main__"):
    # open a file for reading and one for writing
    input_file_handle = open("grades_0.txt", "r")
    output_file_handle = open("transcripts_0.txt", "w") 
    # read a line at a time from Grades.txt file
    for line in input_file_handle:
        #generate a transcript for each student
        student_info = line.split()   
        # compute the final mark
        final = compute_final(student_info[4])
        student_info [4] = final
        # write to the file
        print_to_file(student_info, output_file_handle)
    
    # close both files
    input_file_handle.close()
    output_file_handle.close()
    
    
   
    