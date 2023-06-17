class Solution:
    def isValid(self, s: str) -> bool:
        if not s or (len(s) % 2 != 0): 
            return False

        stack = []
        map = {')': '(', '}': '{', ']': '['}

        for c in s:
            print(stack)
            if c in map:
                if stack.pop() != map[c]: 
                    return False
            if c in map.values(): stack.append(c)
        
        return True
    