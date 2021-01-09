# Предметы

class Subject:
    def __init__(self,subj_name,marks,lecturers):
        self.name = subj_name
        self.marks = marks
        self.lecturers = lecturers

    #def __init__(self):
        #self.name=0
        #self.marks=0
        #self.lecturers=0

        #def InputSubject():
            #s_name = input()
            #s_marks=input()
        #s_grade_sys = input.split()
           # s_lecturers=input()
           # return Subject(s_name,s_marks,s_lecturers)
        #self(s_name,s_marks,s_lecturers)
       # self=self.InputSubject()


class SubjectCycle(Subject):
    def __init__(self,cycle_name,marks,grad_sys,sub,lecturer_name=None):
        self.name=cycle_name
        self.marks=marks
        lecturers = []
        for subject in sub:
            for lector in subject.lecturers:
                lecturers.append(lector)
        if lecturer_name != None:
            lecturers.append(lecturer_name)
        self.lecturers=lecturers
        self.grade_sys= grad_sys
        self.subjects=sub

    def CountAvg(self):
        median=3
        average=1
        harmonic=2
        import statistics as s
        if self.grade_sys == average :
            return float(sum(self.marks)) / max(len(self.marks), 1)
        if self.grade_sys == harmonic:
            return  s.harmonic_mean(self.marks)
        if self.grade_sys == median:
            return s.median(self.marks)



def InputSubjects():
    print('Введите названия предметов')
    s_name=input().split()
    #print('введите код метода расчета средних ')
    #s_grade_sys=input().split()
    s_marks=[]
    s_lecturers=[]
    print('Введите оценки')
    for i in range(len(s_name)):
        s_marks.append(input().split())
    print('Введите имена лекторов')
    for i in range(len(s_name)):
        s_lecturers.append(input().split())
    subjcts=[]
    for i in range(len(s_name)):
        subjcts.append([])
    for i in range(len(s_name)):
        subjcts[i]=Subject(s_name[i],s_marks[i],s_lecturers[i])
    return subjcts

def InputCycleSubjects():

    print('Введите названия циклов предметов')
    s_name=input().split()
    print('Введите код метода расчета средних (1-среднее арифметическое, 2-среднее гармоническое, 3-среднее медианное')
    s_grade_sys=input().split()
    s_marks=[]
    s_lecturers=[]
    print('Введите оценки предметов циклов')
    for i in range(len(s_name)):
        s_marks.append(input().split())
    print('Введите имена лекторов предметов циклов (НЕ ОБЯЗАТЕЛЬНО)')
    for i in range(len(s_name)):
        s_lecturers.append(input().split())
    cycle_subjcts=[]
    for i in range(len(s_name)):
        cycle_subjcts.append([])
    for i in range(len(s_name)):
        print('Ввод предметов для цикла ' + s_name[i])
        sub = InputSubjects()
        cycle_subjcts[i]=SubjectCycle(s_name[i],s_marks[i],s_grade_sys[i],sub,s_lecturers[i])
    return cycle_subjcts

print(InputCycleSubjects())