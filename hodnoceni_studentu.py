from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores): # incilizace objektu
        self.scores = scores # definovani argumentu objektu

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        if 100 >= self.scores[index] >= 90:
            return 'A'
        elif 89 >= self.scores[index] >= 80:
            return 'B'
        elif 79 >= self.scores[index] >= 70:
            return 'C'
        elif 69 >= self.scores[index] >= 60:
            return 'D'
        elif 59 >= self.scores[index] >= 50:
            return 'E'
        else:
            return 'F'

    def find(self, points):
        index_to_find = []
        for i, score in enumerate(self.scores):
            if score == points:
                index_to_find.append(i)
        return index_to_find

    def get_sorted(self):
        scores = self.scores.copy()
        for j in range(len(scores) - 1):
            for i in range(len(scores) - j - 1):
                if scores[i] > scores[i + 1]:
                    scores[i], scores[i + 1] = scores[i + 1], scores[i]
        return scores

    def average(self):
        return sum(self.scores) / len(self.scores)

    def best(self):
        return max(self.scores)

    def worst(self):
        return min(self.scores)

    def pass_rate(self):
        passed = 0
        for score in self.scores:
            if score >= 50:
                passed += 1
        return passed / len(self.scores)

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    number_of_students = results.count()
    print(f"Test was written by {number_of_students} students.")
    for i, result in enumerate(results.scores):
        print(f"Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")
    print(f"Student {results.find(100)} got 100 points.")
    print(f"Results from the worst to the best: {results.get_sorted()}.")
    print(f"Average result was {results.average():.2f}")
    print(f"The best result was {results.best()}")
    print(f"The worst result was {results.worst()}")
    print(f"Fruitfulness was {results.pass_rate():.2f}")


    # random_results = StudentsGrades(random_numbers(30, 0, 100))
    # print(f"Random test was written by {random_results.count()} students.")
    # for i, result in enumerate(random_results.scores):
    #     print(f"Random student {i}: {random_results.get_by_index(i)} points - {random_results.get_grade(i)}")
    # print(f"Random student {random_results.find(100)} got 100 points.")
    # print(f"Random results from the worst to the best: {random_results.get_sorted()}.")


if __name__ == "__main__":
    main()
    # print(results.count())          # 9
    # print(results.get_by_index(2))  # 91
    # print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    # print(results.get_grade(2))  # A (91 bodů)
    # print(results.get_grade(6))  # A (100 bodů)
    # print(results.get_grade(7))  # F (38 bodů)
    # print(results.find(100))  # [6]
    # print(results.find(50))  # [4]
    # print(results.find(77))  # []
    # print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny
