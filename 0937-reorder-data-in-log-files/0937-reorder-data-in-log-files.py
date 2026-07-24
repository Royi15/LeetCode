class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        WordLogs = [word for word in logs if word.split(" ", 1)[1][0].isalpha()]

        WordLogs.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))

        for i in range(len(logs)):
            if logs[i].split(" ", 1)[1][0].isdigit():
                WordLogs.append(logs[i])

        return WordLogs


        