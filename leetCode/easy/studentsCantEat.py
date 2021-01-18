class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 0 circular, 1 square
        # queue of students
        # stack of sandwiches
        
        while students:
                student = students[0]
                sandwich = sandwiches[0]
                
                if sandwich == 0 and 0 not in students or sandwich == 1 and 1 not in students:
                    return len(students)
                
                if student == sandwich:
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    # student goes to back of queue
                    popVal = students.pop(0)
                    students.append(popVal)
                    
        return len(students)
