import pandas as pd
from Entity.Score import Score,Type,ReportCard
import numpy as np

def read_excel(stu_name):
    file_name = "../Excels/"+stu_name+"_grade.xlsx"
    fd = pd.read_excel(file_name,sheet_name="Sheet1")
    data = fd.values
    rp_card = ReportCard()
    #print(data)
    for course in data:
        course_name = course[0]
        course_type = course[1]
        course_credit = course[4]
        course_year = course[8]
        course_semester = course[9]
        course_grade = course[10]
        if course_type == "公共必修":
            # string Type float int int int
            score = Score(course_name,Type.PublicRequired,course_credit,course_grade,course_year,course_semester)
        elif course_type == "公共选修":
            score = Score(course_name, Type.PublicElective, course_credit, course_grade, course_year, course_semester)
        elif course_type == "专业必修":
            score = Score(course_name, Type.MajorRequired, course_credit, course_grade, course_year, course_semester)
        else: # 专业选修
            score = Score(course_name, Type.MajorElective, course_credit, course_grade, course_year, course_semester)
        rp_card.add_score(score)
    return rp_card

rp_card = read_excel("zx")
# rp_card = read_excel("slh")
# rp_card = read_excel("xjy")

rp_card.print_best_choice(2017,2)

# rp_card.print_total_gpa()
# rp_card.print_recommendation_gpa()

# rp_card.print_MajorElective()

