class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        s = list(s)

        # [prefix, suffix, maximum, length]
        tree = [[0, 0, 0, 0] for _ in range(4 * n)]

        def build(node, l, r):
            if l == r:
                tree[node] = [1, 1, 1, 1]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node, l, r)

        def merge(node, l, r):
            left = tree[node * 2]
            right = tree[node * 2 + 1]

            lp, ls, lm, llen = left
            rp, rs, rm, rlen = right

            tree[node][0] = lp
            tree[node][1] = rs
            tree[node][2] = max(lm, rm)
            tree[node][3] = llen + rlen

            # Characters at the boundary are equal
            if s[(l + r) // 2] == s[(l + r) // 2 + 1]:

                if lp == llen:
                    tree[node][0] = llen + rp

                if rs == rlen:
                    tree[node][1] = rlen + ls

                tree[node][2] = max(
                    tree[node][2],
                    ls + rp
                )

        def update(node, l, r, pos, ch):
            if l == r:
                s[pos] = ch
                tree[node] = [1, 1, 1, 1]
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(node * 2, l, mid, pos, ch)
            else:
                update(node * 2 + 1, mid + 1, r, pos, ch)

            merge(node, l, r)

        build(1, 0, n - 1)

        ans = []

        for i in range(len(queryIndices)):
            update(
                1,
                0,
                n - 1,
                queryIndices[i],
                queryCharacters[i]
            )

            ans.append(tree[1][2])

        return ans