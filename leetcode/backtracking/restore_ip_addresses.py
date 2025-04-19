from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) not in range(4, 13):
            return []

        ips = []

        def backtrack(i: int, dots: int, cur_ip: str) -> None:
            if i == len(s) and dots == 4:
                ips.append(cur_ip[:-1])
                return

            if dots > 4:
                return

            for j in range(i, min(i + 3, len(s))):
                if self.valid_ip(s[i : j + 1]):
                    backtrack(j + 1, dots + 1, cur_ip + s[i : j + 1] + ".")

        backtrack(0, 0, "")
        return ips

    def valid_ip(self, s: str) -> bool:
        return int(s) < 256 and (len(s) == 1 or s[0] != "0")
