from collections import defaultdict
from typing import List, Optional


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """There are a total of `numCourses` courses you have to take, labeled
        from `0` to `numCourses - 1`. You are given an array `prerequisites`
        where `prerequisites[i] = [aᵢ, bᵢ]` indicates that you **must** take
        course `bᵢ` first if you want to take course `aᵢ`.

        - For example, the pair `[0, 1]`, indicates that to take course `0` you
        have to first take course `1`.

        Return `true` if you can finish all courses. Otherwise, return `false`.

        Args:
            numCourses (int): required courses
            prerequisites (List[List[int]]): courses that must be taken before
            other courses

        Returns:
            bool: `true` if you can finish all courses or `false` otherwise
        """

        # map of courses and their prerequisites
        prereq_graph = defaultdict(list)
        # list of courses being checked for path to completion
        track_found: List[Optional[bool]] = [None] * numCourses

        # Map each course to a list of its prerequisites.
        for course, prereq in prerequisites:
            prereq_graph[course].append(prereq)

        def is_track_found(course):
            """Determine if there is a path to completion for a course by
            recursively checking its prerequisites.

            Args:
                course (int): the course being checked

            Returns:
                bool: `True` if a path is found to completion, or `False`
                otherwise
            """

            # If the track-to-completion status for this course is not `None`, 
            # then this course has been processed and we can return its status.
            if track_found[course] != None:
                return track_found[course]

            # While processing, the course's track-to-completion status is 
            # `False`. If we encounter this course again during processing, we 
            # will know that there is not a path to completion because 
            # completing this course is required before this course can be taken.
            track_found[course] = False

            # Recursively check prerequisites of this course for a 
            # tack-to-completion.
            for prereq in prereq_graph[course]:
                if not is_track_found(prereq):
                    return False

            # If processing prerequisites does not return `False`, then this 
            # course has a path to completion. 
            track_found[course] = True
            return track_found[course]

        # Check each required course for a possible track to completing the
        # course given its prerequisites.
        for course in range(numCourses):
            if not is_track_found(course):
                return False

        # If each course has been checked, and no course was determined to be
        # impossible to take, then the required courses can be finished.
        return True


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        self.assertTrue(self.sol.canFinish(numCourses, prerequisites))

    def test_example2(self):
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        self.assertFalse(self.sol.canFinish(numCourses, prerequisites))

    def test_example3(self):
        numCourses = 5
        prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
        self.assertTrue(self.sol.canFinish(numCourses, prerequisites))

    def test_example4(self):
        numCourses = 6
        prerequisites = [[1, 0], [1, 2], [3, 1], [2, 3], [2, 4], [4, 5], [2, 5]]
        self.assertFalse(self.sol.canFinish(numCourses, prerequisites))

    def test_example5(self):
        numCourses = 6
        prerequisites = [[1, 0], [1, 2], [3, 1], [3, 2], [2, 4], [4, 5], [2, 5]]
        self.assertTrue(self.sol.canFinish(numCourses, prerequisites))


if __name__ == "__main__":
    unittest.main()
