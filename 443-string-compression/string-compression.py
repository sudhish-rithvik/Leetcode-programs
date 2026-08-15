class Solution(object):
    def compress(self, chars):
        read = 0
        write = 0
        n = len(chars)

        while read < n:
            current = chars[read]
            start = read

            # Count consecutive characters
            while read < n and chars[read] == current:
                read += 1

            count = read - start

            # Write the character
            chars[write] = current
            write += 1

            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write