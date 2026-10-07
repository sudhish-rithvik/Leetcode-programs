class Solution(object):
    def groupThePeople(self, groupSizes):
        groups = {}
        ans = []

        for person in range(len(groupSizes)):
            size = groupSizes[person]

            if size not in groups:
                groups[size] = []

            groups[size].append(person)

            if len(groups[size]) == size:
                ans.append(groups[size])
                groups[size] = []

        return ans