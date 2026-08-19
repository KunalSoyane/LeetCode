class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        rows = {}

        # Store reserved seats for each affected row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        # Every completely empty row can fit 2 groups
        answer = (n - len(rows)) * 2

        for seats in rows.values():
            # Check seats 2,3,4,5
            left = all(seat not in seats for seat in [2, 3, 4, 5])

            # Check seats 4,5,6,7
            middle = all(seat not in seats for seat in [4, 5, 6, 7])

            # Check seats 6,7,8,9
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left and right:
                # Can fit both groups
                answer += 2
            elif left or middle or right:
                # Can fit one group
                answer += 1

        return answer