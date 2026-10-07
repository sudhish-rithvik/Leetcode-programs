class Solution(object):
    def convertDateToBinary(self, date):
        parts = date.split("-")

        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        return bin(year)[2:] + "-" + bin(month)[2:] + "-" + bin(day)[2:]