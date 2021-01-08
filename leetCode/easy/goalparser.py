#https://leetcode.com/problems/goal-parser-interpretation
class Solution:
    def interpret(self, command: str) -> str:
        cmd2 = "o".join(command.split("()"))
        new = "al".join(cmd2.split("(al)"))
        return new
