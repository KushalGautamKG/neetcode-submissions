from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        # Sort by position descending so we process cars from closest to the target to farthest
        for p, s in sorted(zip(position, speed), reverse=True):
            time = (target - p) / s
            stack.append(time)
            # If the current car catches up to the one ahead (time <= previous),
            # they form a single fleet, so discard the current time.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


        