class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = sorted(
            [(p, s) for p, s in zip(position, speed)],
            reverse=True,
            key=lambda x: x[0],
        )

        for p, s in pos_speed:
            time = (target - p) / s
            stack.append(time)

            if stack:
                if len(stack) >= 2 and stack[-1] <= stack[-2]:
                    stack.pop()

        print("Car fleet", stack)
        return len(stack)