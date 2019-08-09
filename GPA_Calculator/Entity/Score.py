import numpy as np


class Type:
    PublicRequired = 1
    MajorRequired = 2
    PublicElective = 3
    MajorElective = 4


class Score:  # 单科成绩
    def __init__(self, name, type, credit, score, year, semester):
        self._name = name
        self._type = type
        self._credit = credit
        self._score = score
        self._year = year
        self._semester = semester
        if score > 100.0:
            print("error score is no more than 100")
        elif score >= 90.0:
            self._gpa = 4.0
        elif score >= 85.0:
            self._gpa = 3.7
        elif score >= 82.0:
            self._gpa = 3.3
        elif score >= 78.0:
            self._gpa = 3.0
        elif score >= 75.0:
            self._gpa = 2.7
        elif score >= 72.0:
            self._gpa = 2.3
        elif score >= 68.0:
            self._gpa = 2.0
        elif score >= 64.0:
            self._gpa = 1.5
        elif score >= 60.0:
            self._gpa = 1.0
        elif score >= 0.0:
            self._gpa = 0
        else:
            print("error,score is no less than 0")

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_credit(self):
        return self._credit

    def get_score(self):
        return self._score

    def get_gpa(self):
        return self._gpa

    def get_year(self):
        return self._year

    def get_semester(self):
        return self._semester


class ReportCard:  # 成绩单
    def __init__(self):
        self._score_list = list()
        self._total_S = 0.0  # 绩点乘学分的总和
        self._total_RS = 0.0  # 保研的科目的绩点乘学分总和
        self._total_credit = 0.0  # 总学分
        self._total_re_credit = 0.0  # 保研科目总学分
        pass

    def add_score(self, score):
        self._score_list.append(score)
        if score.get_type() == Type.MajorRequired or score.get_type() == Type.MajorElective or score.get_type() == Type.PublicRequired:
            self._total_re_credit += score.get_credit()
            self._total_RS += score.get_credit()*score.get_gpa()
        self._total_credit += score.get_credit()
        self._total_S += score.get_credit()*score.get_gpa()

    def _calculate_total_gpa(self):
        return self._total_S/self._total_credit

    def print_total_gpa(self):
        gpa = self._calculate_total_gpa()
        print("总GPA为:",gpa)

    def _calculate_recommendation_gpa(self):
        return self._total_RS/self._total_re_credit

    def print_recommendation_gpa(self):
        rec_gpa = self._calculate_recommendation_gpa()
        print("保研GPA为:", rec_gpa)

    # 返回l1 l2 l3 l4,其中l1为公必list，l2为公选list,l3为专必list,l4为专选list
    def get_classfied_scores(self):
        l1 = list()
        l2 = list()
        l3 = list()
        l4 = list()
        for score in self._score_list:
            if score.get_type() == Type.PublicRequired:
                l1.append(score)
            elif score.get_type() == Type.PublicElective:
                l2.append(score)
            elif score.get_type() == Type.MajorRequired:
                l3.append(score)
            else:
                l4.append(score)
        return l1,l2,l3,l4
    # 打印全部成绩
    def print_all_scores(self):
        print("下面是全部成绩:",end='\n')
        for score in self._score_list:
            print("课名:", score.get_name(), "学分", score.get_credit(), "得分:", score.get_score(), "GPA:", score.get_gpa())
        print("共%s门"%len(self._score_list))

    # 打印公共必修成绩情况
    def print_PublicRequired(self):
        list,_,_,_ = self.get_classfied_scores()
        print("下面是公共必修成绩情况:",end='\n')
        for score in list:
            print("课名:", score.get_name(), "学分" ,score.get_credit(),"得分:", score.get_score(),"GPA:",score.get_gpa())

    # 打印公共选修成绩情况
    def print_PublicElective(self):
        _, list, _, _ = self.get_classfied_scores()
        print("下面是公共选修成绩情况:", end='\n')
        for score in list:
            print("课名:", score.get_name(), "学分", score.get_credit(), "得分:", score.get_score(), "GPA:", score.get_gpa())

    # 打印专业必修成绩情况
    def print_MajorRequired(self):
        _, _, list, _ = self.get_classfied_scores()
        print("下面是专业必修成绩情况:", end='\n')
        for score in list:
            print("课名:", score.get_name(), "学分", score.get_credit(), "得分:", score.get_score(), "GPA:", score.get_gpa())

    # 打印专业选修成绩情况
    def print_MajorElective(self):
        _, _, _, list = self.get_classfied_scores()
        print("下面是专业选修成绩情况:", end='\n')
        for score in list:
            print("课名:", score.get_name(), "学分", score.get_credit(), "得分:", score.get_score(), "GPA:", score.get_gpa())

    # 打印score的list
    def print_list(self,list):
        for score in list:
            print("课名:", score.get_name(), "学分:", score.get_credit(), "得分:", score.get_score(), "GPA:", score.get_gpa(),"学年:",score.get_year())

    # grade 为年级数，如大一学年则为1，以此类推
    def calculate_best_choice_for_grade(self, your_grade,year):
        # 返回值:l1为某一学年所有必修 l2为某一学年的专选 l3 为某一学年的公选
        def get_required_and_diff_elective():
            l1,l2,l3,l4 = self.get_classfied_scores()
            # self.print_list(l4)
            required = list()
            majorElec = list()
            publicElec = list()
            try:
                if year > 4 or year < 1:
                    raise Exception
                for score in l1:
                    if score.get_year() == your_grade + year -1:
                        required.append(score)
                for score in l2:
                    if score.get_year() == your_grade + year -1:
                        publicElec.append(score)
                for score in l3:
                    if score.get_year() == your_grade + year -1:
                        required.append(score)
                for score in l4:
                    if score.get_year() == your_grade + year -1:
                        majorElec.append(score)
            except Exception:
                print("year必须是1 2 3 4中的一个")
            return required,majorElec,publicElec

        # aim01中前面是major的0-1变量，0表示不纳入B1，1表示纳入B1
        # choice:1表示计入B1，-1表示计入B2，0表示B1，B2均不计入
        def get_score(required,major,public,aim01):
            def get_ordered_index(total_scores):
                ndarray_list = np.argsort(total_scores)
                list = ndarray_list.tolist()
                list.reverse()
                none_0_list = [a for a in list if total_scores[a] > 0]
                return none_0_list
            times = 0.002
            r_credit = [score.get_credit() for score in required]
            r_score = [score.get_score() for score in required]
            m_credit = [score.get_credit() for score in major]
            m_score = [score.get_score() for score in major]
            p_credit = [score.get_credit() for score in public]
            p_score = [score.get_score() for score in public]
            r_s_plus_c = sum(np.array(r_credit)*np.array(r_score))
            r_c = sum(r_credit)
            #F22 = (sum(np.array(m_score)*np.array(m_credit)*np.array(aim_m_01))+sum(np.array(p_score)*np.array(p_credit)*np.array(aim_p_01)))*times
            # B2
            choice = aim01 + [0 for _ in p_score] # 初始化choice
            total_01 = [(1-aim) for aim in aim01] + [1 for _ in p_score]
            m_p_score = m_score+p_score
            m_p_credit = m_credit+p_credit
            total_scores = np.array(m_p_score)*np.array(m_p_credit)*np.array(total_01)
            orderd_index = get_ordered_index(total_scores)
            B2_0 = 0
            MOST_B2 = 8
            if len(orderd_index) <= MOST_B2:
                for index in orderd_index:
                    choice[index] = -1
                    B2_0 += total_scores[index]
            else:
                for i in range(0,MOST_B2): # 0-7
                    index = orderd_index[i]
                    choice[index] = -1
                    B2_0 += total_scores[index]
            B2 = B2_0*times
            # 求专选分子m_up
            m_up_list = np.array(m_score)*np.array(m_credit)*np.array(aim01)
            m_up = sum(m_up_list)
            # 求专选分母m_down
            m_down_list = np.array(m_credit)*np.array(aim01)
            m_down = sum(m_down_list)
            # 分子
            B1_up = r_s_plus_c + m_up
            # 分母
            B1_down = r_c + m_down
            B1 = B1_up/B1_down
            F2 = B1+B2
            return F2,choice

        # length:专选和公选课程的总数
        # 返回值:从00000000到11111111的list，list中的每个值是0和1组成的list，1表示计入公选
        def get_choice_lists(length):
            choice_lists = list()
            for i in range(0,2**length):
                bin_str = bin(i).replace("0b","")
                fixed_len_bin_str = "0"*(length - len(bin_str))+bin_str
                temp_list = list()
                for c in fixed_len_bin_str:
                    temp_list.append(int(c))
                choice_lists.append(temp_list)
            return choice_lists


        MOST_MajorElective_to_B1 = 4
        required_list,majorElec_list,publicElec_list = get_required_and_diff_elective()
        # self.print_list(majorElec_list)
        major_len = len(majorElec_list)
        choice_lists = get_choice_lists(major_len) # majorlen
        name_list = [score.get_name() for score in majorElec_list]+[score.get_name() for score in publicElec_list]
        solution_list = SolutionList(name_list)
        for choice_list in choice_lists:
            if sum(choice_list) <= MOST_MajorElective_to_B1:
                score,choice = get_score(required_list,majorElec_list,publicElec_list,choice_list)
                solution = Solution(choice,score)
                solution_list.add_solution(solution)
        return solution_list

    def print_best_choice(self,your_grade,year):
        solution_list = self.calculate_best_choice_for_grade(your_grade,year)
        name_list = solution_list.get_name_list()
        best_solution = solution_list.get_best_solution()
        best_choice = best_solution.get_choice_list()
        best_F2 = best_solution.get_score()
        print("方案如下:")
        length = len(name_list)
        for i in range(0,length):
            if best_choice[i] == 1:
                print(name_list[i],"计入B1")
            elif best_choice[i] == 0:
                print(name_list[i], "不计入B1和B2")
            elif best_choice[i] == -1:
                print(name_list[i], "计入B2")
        print("最佳F2:",best_F2)



class Solution:
    # choice_list:专选、公选的0-1取值list, score:当前0-1取值下的F2成绩
    def __init__(self,choice_list,score):
        self._choice_list = choice_list
        self._score = score

    def get_score(self):
        return self._score

    def get_choice_list(self):
        return self._choice_list


class SolutionList:
    # name_list:专选、公选的课程名列表、专选在前
    #
    #
    def __init__(self,name_list):
        self._name_list = name_list
        self._solution_list = list()
        self._best_solution = None

    def add_solution(self,solution):
        if self._best_solution is None:
            self._best_solution = solution
        elif self._best_solution.get_score() < solution.get_score():
            self._best_solution = solution
        self._solution_list.append(solution)

    def get_best_solution(self):
        return self._best_solution

    def get_name_list(self):
        return self._name_list






    '''    错误理解规则的情况下写的函数，但我觉得用数字二进制的枚举思路不错
    def calculate_best_choice_for_grade(self, your_grade,year):
        # 返回值:l1为某一学年所有必修 l2为某一学年的专选 l3 为某一学年的公选
        def get_required_and_diff_elective():
            l1,l2,l3,l4 = self.get_classfied_scores()
            # self.print_list(l4)
            required = list()
            majorElec = list()
            publicElec = list()
            try:
                if year > 4 or year < 1:
                    raise Exception
                for score in l1:
                    if score.get_year() == your_grade + year -1:
                        required.append(score)
                for score in l2:
                    if score.get_year() == your_grade + year -1:
                        publicElec.append(score)
                for score in l3:
                    if score.get_year() == your_grade + year -1:
                        required.append(score)
                for score in l4:
                    if score.get_year() == your_grade + year -1:
                        majorElec.append(score)
            except Exception:
                print("year必须是1 2 3 4中的一个")
            return required,majorElec,publicElec

        # aim01中前面是major的0-1变量，后面是public的0-1变量
        def get_score(required,major,public,aim_m_01,aim_p_01):
            times = 0.002
            r_credit = [score.get_credit() for score in required]
            r_score = [score.get_score() for score in required]
            m_credit = [score.get_credit() for score in major]
            m_score = [score.get_score() for score in major]
            p_credit = [score.get_credit() for score in public]
            p_score = [score.get_score() for score in public]
            r_s_plus_c = sum(np.array(r_credit)*np.array(r_score))
            r_c = sum(r_credit)
            F22 = (sum(np.array(m_score)*np.array(m_credit)*np.array(aim_m_01))+sum(np.array(p_score)*np.array(p_credit)*np.array(aim_p_01)))*times
            # 求专选分子m_up
            m_r_aim_01 = [(1-aim) for aim in aim_m_01]
            m_up_list = np.array(m_score)*np.array(m_credit)*np.array(m_r_aim_01)
            m_up = sum(m_up_list)
            # 求专选分母m_down
            m_down_list = np.array(m_credit)*np.array(m_r_aim_01)
            m_down = sum(m_down_list)
            # 分子
            F21_up = r_s_plus_c + m_up
            # 分母
            F21_down = r_c + m_down
            F21 = F21_up/F21_down
            score = F21+F22
            return score

        # length:专选和公选课程的总数
        # 返回值:从00000000到11111111的list，list中的每个值是0和1组成的list，1表示计入公选
        def get_choice_lists(length):
            choice_lists = list()
            for i in range(0,2**length):
                bin_str = bin(i).replace("0b","")
                fixed_len_bin_str = "0"*(length - len(bin_str))+bin_str
                temp_list = list()
                for c in fixed_len_bin_str:
                    temp_list.append(int(c))
                choice_lists.append(temp_list)
            return choice_lists

        MOST_B2 = 8
        MOST_MajorElective_to_B2 = 4
        required_list,majorElec_list,publicElec_list = get_required_and_diff_elective()
        # self.print_list(majorElec_list)
        major_len = len(majorElec_list)
        public_len = len(publicElec_list)
        choice_lists = get_choice_lists(major_len+public_len)
        name_list = [score.get_name() for score in majorElec_list]+[score.get_name() for score in publicElec_list]

        solution_list = SolutionList(name_list)
        for choice_list in choice_lists:
            if sum(choice_list) <= MOST_B2:
                major01 = choice_list[:major_len]
                public01 = choice_list[major_len:]
                if sum(major01) <= MOST_MajorElective_to_B2:
                    score = get_score(required_list,majorElec_list,publicElec_list,major01,public01)
                    solution = Solution(choice_list,score)
                    solution_list.add_solution(solution)
        return solution_list
        
    def print_best_choice(self,your_grade,year):
        solution_list = self.calculate_best_choice_for_grade(your_grade,year)
        name_list = solution_list.get_name_list()
        best_solution = solution_list.get_best_solution()
        best_choice = best_solution.get_choice_list()
        best_F2 = best_solution.get_score()
        print("方案:(如果专选不计入公选则计入必修，如果公选不计入公选则不计算)")
        length = len(name_list)
        for i in range(0,length):
            if best_choice[i] == 1:
                print(name_list[i],"计入公选")
            elif best_choice[i] == 0:
                print(name_list[i], "不计入公选")
        print("最佳F2:",best_F2)
        
class Solution:
    # choice_list:专选、公选的0-1取值list, score:当前0-1取值下的F2成绩
    def __init__(self,choice_list,score):
        self._choice_list = choice_list
        self._score = score

    def get_score(self):
        return self._score

    def get_choice_list(self):
        return self._choice_list


class SolutionList:
    # name_list:专选、公选的课程名列表、专选在前
    #
    #
    def __init__(self,name_list):
        self._name_list = name_list
        self._solution_list = list()
        self._best_solution = None

    def add_solution(self,solution):
        if self._best_solution is None:
            self._best_solution = solution
        elif self._best_solution.get_score() < solution.get_score():
            self._best_solution = solution
        self._solution_list.append(solution)

    def get_best_solution(self):
        return self._best_solution

    def get_name_list(self):
        return self._name_list     
        '''
