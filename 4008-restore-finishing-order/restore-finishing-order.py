class Solution(object):
    def recoverOrder(self, order, friends):
        friend_set = set(friends)
        ans = []

        for person in order:
            if person in friend_set:
                ans.append(person)

        return ans