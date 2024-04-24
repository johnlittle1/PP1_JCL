## import library
import streamlit as st

def main():
    st.title("Grade Calculator")

    ## function to get syllabus information from the user
    def get_syllabus_info():
        num_assignments = st.number_input('How many assignments do you have?', min_value=1, step=1)
        assignments = []
        for i in range(num_assignments):
            assignment_name = st.text_input(f'Enter the name of assignment {i + 1}:')
            weight = st.number_input(f'Enter the weight for assignment {i + 1} as a decimal:')
            assignments.append({'assignment': assignment_name, 'weight': weight})
        final_weight = st.number_input('What percent of your grade is the final exam worth?')
        desired_grade = st.number_input('What is your desired grade in this class (decimal)?')
        return assignments, final_weight, desired_grade

    ## function to allow user to enter grades for assignments
    def enter_grades(assignments):
        for assignment in assignments:
            grade = st.number_input(f"Enter the grade for {assignment['assignment']}.")
            if grade:
                assignment['grade'] = grade

    ## function to calculate current grade
    def calc_current_grade(assignments):
        weighted_grade = 0
        total_weight = 0
        for assignment in assignments:
            if 'grade' in assignment:
                weighted_grade += assignment['grade'] * assignment['weight']
                total_weight += assignment['weight']
        current_grade = weighted_grade / total_weight if total_weight != 0 else 0
        return current_grade

    ## function to calculate required final grade
    def final_grade_needed(final_weight, desired_grade, current_grade):
        required_grade = (desired_grade - (1 - final_weight) * current_grade) / final_weight
        return required_grade
	

    ## function calls and calculation results
    assignments, final_weight, desired_grade = get_syllabus_info()
    enter_grades(assignments)

    current_grade = calc_current_grade(assignments)
    st.write(f"Your current grade in this class is {round(current_grade*100,2)}%.")

    required_grade = final_grade_needed(final_weight, desired_grade, current_grade)
    st.write(f"You will need to get {round(required_grade*100,2)}% on the final to achieve your goal.")

if __name__ == "__main__":
    main()
