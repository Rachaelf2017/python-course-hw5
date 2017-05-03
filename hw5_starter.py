# In this homework, we'll be using for-loops, lists and dictionaries to
# operate on a tabular dataset!

# This dataset is a modified version of a dataset available on the Chicago
# open data portal.
# https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj

# In this homework assignment description, we'll describe the functions your
# program will need, but it's up to you to check that each one is working
# as you go along.
import sys

# 0.  Write a function to read in the dataset and return it as a list of
#     strings.  Your function should not return any empty rows or the header row.
#     Your function's signature should be EXACTLY
#     def read_data(file_path):
#     i.e. your function definition should look EXACTLY like that.

def read_data(file_path):
    read_data = open(sys.argv[1])
    indata = read_data.read()
    rows_raw = indata.split('\n')[1:-1]
    return rows_raw

def make_dict(data_rows):
    index = []
    for row in data_rows:
        index.append(row.split(','))
    # print index
    landmark_lookup = {}
    for landmark in index:
        if len(landmark) == 2:
            landmark_lookup[landmark[0]] = landmark[1]
        else:
            sys.exit("%s is missing it's designation date" % (landmark[0]))
    return landmark_lookup

def try_lookup(term, district_dict):
    narrowed = []
    for key in district_dict:
        if term in key:
            narrowed.append(key)
        else:
            pass
    return narrowed



def prompt_and_search(district_dict):
    finding =[]
    finding = finding + try_lookup(raw_input("Landmark search term: "), make_dict(read_data(sys.argv[1])))
    if len(finding)>1:
        print "Which landmark?"
        for i in range(len(finding)):
            print  "%s" % finding[i]
        prompt_and_search(make_dict(read_data(sys.argv[1])))
    elif len(finding)==1:
        print "The %s district was officiallly landmarked on %s." % (finding[0],district_dict[finding[0]])
    else:
        print "None found. Try again"
        prompt_and_search(make_dict(read_data(sys.argv[1])))

    #
    # print "The %s district was officiallly landmarked on %s" % (term,district_dict[term])
    #


prompt_and_search(make_dict(read_data(sys.argv[1])))



# 1.  Write a function to read a list of strings into a dictionary.
#     Your function should check if each string has two parts, separated by
#     a comma.  If it doesn't, your program should exit immediately with a
#     helpful message.
#     Hint:  look up the sys.exit() function.
#     For each string that does have two parts separated by a comma, your
#     function should use the first part as the key and the second as the value.
#     Your function's signature should be EXACTLY
#     def make_dict(data_rows):
#     i.e. your function definition should look EXACTLY like that.


#  2.  Write a function that searches a dictionary's keys for a string search
#      term.  At first, write a function that returns a list of strings length 1
#      containing an element with a key that matches the search term exactly.
#      Your function's signature should be EXACTLY
#      def try_lookup(term, district_dict) :
#      i.e. your function definition should look EXACTLY like that.


# 3.  Now write a function to prompt the user for a search term, then
#     look it up in the dictionary.
#     Your function should take a dictionary
#     as an argument.  Your function should then prompt the user for a search
#     term and then call the function from (2) to find the matching key.
#     For now, you can assume your function always finds exactly one match.
#     After finding the match, your function should print out the date that
#     district became landmarked.
#     Your function's signature should be EXACTLY
#     def prompt_and_search(district_dict):
#     i.e. your function definition should look EXACTLY like that.
#     Your function's output should be formatted EXACLTY like this:
#     "The Oakdale Avenue district was officially landmarked on 03/29/2006."


#  4.  Now go back to your function from (2).  Update it so that it returns a
#      list of 0 or more strings.   Each string in the returned list should
#      represent a key from the dictionary, such that the term is part of that
#      key.  For example, if the term is 'Oak', your function should now return
#      ['Oakdale Avenue', 'Oakland'].

#  5.  Now go back to your function from (3).  Update it so that:
#      - if it finds exactly one match it prints out the match (as in (4)) and
#        then exits
#      - if it finds zero matches, it prompts the user for a new search term
#      - if it finds more then one matches, it shows the user the possible
#        matches, then prompts them again.
#      Note that your program should continue indefinately until a single
#      match is found.
#      Full credit on this part requires code that is clean and not repetitive.

#  6.  Include whatever additional code you need to run your program.  This
#      should include taking the path to the data file from the program
#      argument list.
