# Your task is to write a program which allows teachers to create a multiple choice
# test in a class called Testpaper and to be also able to assign a minimum pass mark.
# The testpaper's subject should also be included. The attributes are in the following order:
# 1. subject
# 2. markscheme
# 3. pass_mark
# Example:
#
# paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
# paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
# paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
#
# student1 = Student()
# student2 = Student()
# student1.tests_taken ➞ "No tests taken"
# student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
# student1.tests_taken ➞ {"Maths" : "Passed! (80%)"}
#
# student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
# student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
# student2.tests_taken ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}


class TestPaper:
    def __init__(self, subject, mark_scheme=list, pass_mark=str):
        self.subject = subject
        self.mark_scheme = mark_scheme
        self.pass_mark = pass_mark


class Student:
    tests_taken = 'No tests taken'

    def take_test(self, paper, answers):
        correct_answer = 0
        for answer in answers:
            for reply in paper.mark_scheme:
                if answer == reply:
                    correct_answer += 1
        percent = int(round((correct_answer / len(paper.mark_scheme) * 100), 0))
        if percent >= int(paper.pass_mark[:2]):
            result = f'Passed! ({percent}%)'
        else:
            result = f'Failed! ({percent}%)'
        if isinstance(self.tests_taken, str):
            self.tests_taken = {}
        self.tests_taken.update({paper.subject: result})
