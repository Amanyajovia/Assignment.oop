#OOP's(Object Oriented Programming)
#An object is also an instance,it is found in a class
#Here we create objects that do not exist and we give them classes,objects
#Modeling-Trying to identify classes and attributes in each class
#The things that we want the class to do are the methods

#Examples
#1.Creating classes 
#Classes names always start with a capital letter and it's always singular.
#Syntax class Name:
# Cohort class:
    # name
    # description
    # start_date
    # end_date
    # total_number_of_students
    # All the objects are strings.
    
#Within the cohort class:
#Add a constructor for the cohort class.hint read about constructors

# class Cohort:
#     def __init__(self, name, description, start_date, end_date, total_number_of_students):
#         # Initializing the attributes of the cohort
#         self.name = name
#         self.description = description
#         self.start_date = start_date
#         self.end_date = end_date
#         self.total_number_of_students = total_number_of_students

#     def __str__(self):
    
#         print(f"Cohort Name: {self.name}\nDescription: {self.description}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}\nTotal Students: {self.total_number_of_students}")

# # Example of cohort details
# cohort4 = Cohort(
#     name=" Cohort4 class 2024",
#     description="A commited class",
#     start_date="2024-01-01",
#     end_date="2025-06-01",
#     total_number_of_students="60"
#     )
# print(cohort4)


#Add a method(function to the class that prints the cohort name and the total number of student

# class Cohort:
#     def __init__(self, name, description, start_date, end_date, total_number_of_students):
#         self.name = name
#         self.description = description
#         self.start_date = start_date
#         self.end_date = end_date
#         self.total_number_of_students = total_number_of_students

    
#     def print_cohort_info(self):
#         print(f"Cohort Name: {self.name}")
#         print(f"Total Number of Students: {self.total_number_of_students}")

# # For Example
# cohort4 = Cohort("Python course unit", "A logical course unit ", "2024-01-01", "2024-06-30", "60")
# cohort4.print_cohort_info()

#Create a new instance(object) of the cohort class.hint newCohort = Cohort()

# Create a new cohort with name and start date:
class Cohort:
  def __init__(self, name, description, start_date, end_date, total_number_of_students):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.total_number_of_students = total_number_of_students



newCohort = Cohort(
    name="Cohort5",
    description="An intelligent class focusing on exploring new ideas.",
    start_date="2025-01-15",
    end_date="2026-04-15",
    total_number_of_students="80"
)

#  Accessing  the attributes of the new cohort:
print(f"Cohort Name: {newCohort.name}")
print(f"Description: {newCohort.description}")
print(f"Start Date: {newCohort.start_date}")
print(f"End Date: {newCohort.end_date}")
print(f"Total Students: {newCohort.total_number_of_students}")

