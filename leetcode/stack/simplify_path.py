class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathSplit = path.split("/")
        for p in pathSplit:
            match p:
                case "" | ".":
                    continue
                case "..":
                    if stack:
                        stack.pop()
                case _:
                    stack.append(p)
        return "/" + "/".join(stack)
