# 640. Solve the Equation

# Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

# If there is no solution for the equation, return "No solution".

# If there are infinite solutions for the equation, return "Infinite solutions".

# If there is exactly one solution for the equation, we ensure that the value of x is an integer.

# Example 1:
# Input: "x+5-3+x=6+x-2"
# Output: "x=2"

# Example 2:
# Input: "x=x"
# Output: "Infinite solutions"

# Example 3:
# Input: "2x=x"
# Output: "x=0"

# Example 4:
# Input: "2x+3x-6x=x+2"
# Output: "x=-1"

# Example 5:
# Input: "x=x+2"
# Output: "No solution"

# 分解方程成为ax+b=0的形式
# 注意处理带x的特殊情况

class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        leftSeg,rightSeg = self.segString(left), self.segString(right)
        coeffX = coeff = 0

        (coeffX, coeff) += self.toNum(leftSeg)
        (coeffX, coeff) -= self.toNum(rightSeg)

        if coeffX is 0:
            if coeff is 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return 'x=' + str(-coeff / coeffX)

    def segString(self, s):
        ret , start=  [], 0
        for i in range(1, len(s)):
            if s[i] == '+' or s [i] == '-':
                ret.append(s[start:i])
                start = i
        ret.append(s[start:])
        return ret

    def toNum(self, stringList):
        coeffX = coeff = 0
        for i in range(len(stringList)):
            if stringList[i][-1] == 'x' :
                if len(stringList[i]) == 1 or (len(stringList[i]) == 2 and stringList[i][0] == '+'):
                    coeffX += 1
                elif len(stringList[i]) == 2 and stringList[i][0] == '-':
                    coeffX -= 1
                else:
                    coeffX += int(stringList[i][:-1])
            else:
                coeff += int(stringList[i])
        return (coeffX, coeff)