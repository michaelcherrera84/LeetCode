from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """There are a total of `numCourses` courses you have to take, labeled
        from `0` to `numCourses - 1`. You are given an array `prerequisites`
        where `prerequisites[i] = [aᵢ, bᵢ]` indicates that you must take course
        `bᵢ` first if you want to take course `aᵢ`.

        - For example, the pair `[0, 1]`, indicates that to take course `0` you
        have to first take course `1`.

        Return *the ordering of courses you should take to finish all courses.*
        If there are many valid answers, return **any** of them. If it is
        impossible to finish all courses, return **an empty array**.

        Args:
            numCourses (int): required courses
            prerequisites (List[List[int]]): prerequisites for each course

        Returns:
            List[int]: the order of courses to finish all courses
        """

        # map of courses to lists of prerequisites
        prereq_graph = defaultdict(list)
        # list of completability statuses for courses
        is_track: List[bool | None] = [None] * numCourses
        # a possible track for completing the required courses
        track = []

        # Map the courses to lists of their prerequisites.
        for course, prereq in prerequisites:
            prereq_graph[course].append(prereq)

        def find_track(course):
            """Determine if there is a possible track to completing each course
            and record the order.

            Args:
                course (int): the course being checked

            Returns:
                bool: `True` if the course has a tack to completion or `False`
                otherwise
            """

            # If the track status is not `None` then this course has been check
            # and we can return its status.
            if is_track[course] != None:
                return is_track[course]

            # The track status is set to `False` while searching for a
            # possible completion track. If this same course appears again before
            # a completion track is found, then this course cannot be completed
            # because this course must be completed before it can be taken.
            is_track[course] = False

            # Check the completability of the prerequisites for this course.
            for prereq in prereq_graph[course]:
                if not find_track(prereq):
                    return False

            # If none of the prerequisites for this course were found to be not
            # completeable, then this course has a track to completion.
            is_track[course] = True

            # This course can be completed as this point along the track.
            track.append(course)
            return is_track[course]

        # Check each course for completability and find the track to completion.
        for course in range(numCourses):
            # If any course cannot be completed, there is no track to completion.
            if not find_track(course):
                return []

        return track


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = [0, 1]
        actual = self.sol.findOrder(numCourses, prerequisites)
        self.assertEqual(expected, actual)

    def test_example2(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        expected = [0, 1, 2, 3]
        actual = self.sol.findOrder(numCourses, prerequisites)
        self.assertEqual(expected, actual)

    def test_example3(self):
        numCourses = 1
        prerequisites = []
        expected = [0]
        actual = self.sol.findOrder(numCourses, prerequisites)
        self.assertEqual(expected, actual)

    def test_example4(self):
        numCourses = 7
        prerequisites = [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]
        expected = [6, 5, 4, 2, 3, 0, 1]
        actual = self.sol.findOrder(numCourses, prerequisites)
        self.assertEqual(expected, actual)

    def test_example5(self):
        numCourses = 10
        prerequisites = [[5, 8], [3, 5], [1, 9], [4, 5], [0, 2], [7, 8], [4, 9]]
        expected = [2, 0, 9, 1, 8, 5, 3, 4, 6, 7]
        actual = self.sol.findOrder(numCourses, prerequisites)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
