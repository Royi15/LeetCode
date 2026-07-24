class Solution(object):
    def help(self, direction, instruction):
        if direction == 'north':
            if instruction == 'L':
                return 'west'
            else:
                return 'east'
        elif direction == 'east':
            if instruction == 'L':
                return 'north'
            else:
                return 'south'
        elif direction == 'south':
            if instruction == 'L':
                return 'east'
            else:
                return 'west'
        else:  # west
            if instruction == 'L':
                return 'south'
            else:
                return 'north'

     
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x,y = 0,0
        direction = 'north'

        for i in range(len(instructions)):
            if instructions[i] == 'G':
                if direction == 'west':
                    x -= 1
                elif direction == 'south':
                    y -= 1
                elif direction == 'north':
                    y += 1
                else:
                    x += 1

            else:
                direction = self.help(direction,instructions[i])

        if (x,y) == (0,0) or direction != 'north':
            return True

        return False
