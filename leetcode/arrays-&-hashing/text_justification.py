from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            # Line complete
            if length + len(line) + len(words[i]) > maxWidth:
                extraSpace = maxWidth - length
                spaces = extraSpace // max(1, len(line) - 1)
                remSpaces = extraSpace % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if remSpaces:
                        line[j] += " "
                        remSpaces -= 1

                res.append("".join(line))
                line, length = [], 0  # Reset line and length

            line.append(words[i])
            length += len(words[i])
            i += 1

        # Handle the last line
        lastLine = " ".join(line)
        remSpaces = maxWidth - len(lastLine)
        res.append(lastLine + " " * remSpaces)
        return res
