from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        num_pre = defaultdict(list)
        for num, pre in prerequisites:
            num_pre[num].append(pre)   # CHANGE: keep all prereqs

        explored_num = set()  # courses fully processed (acyclic)
        visiting = set()      # courses on current DFS path (cycle detection)

        def chain(num: int) -> bool:
            if num in explored_num:
                return True
            if num in visiting:
                return False  # found a cycle

            visiting.add(num)
            for pre in num_pre[num]:          # CHANGE: explore all prereqs
                if not chain(pre):
                    return False
            visiting.remove(num)

            explored_num.add(num)
            return True

        for num in range(numCourses):
            if not chain(num):
                return False
        return True

        


        