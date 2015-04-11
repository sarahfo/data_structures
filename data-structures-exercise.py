#Data-Structures Exercise
#I am going to try to write this without looking at the exercise first

# We want to determine the unique houses from Hackbright cohorts.
# First, we will define the function.
def unique_houses(cohort_data):

    house = set([]) # hey, we're making house into a set! But it's empty right now.

    cohort_data = open(cohort_data)  # refers to the file with the data

    for line in cohort_data:
    # Each line has "first_name | last_name | house | advisor | cohort"
    # We want to split this and get the houses in a set.
       line = line.rstrip()  #remove that blank space at the end of the line
       data = line.split("|") # we want to call each row 'student' and split each column by |
       house.add(data[2])
    print house

unique_houses('cohort_data.txt')
