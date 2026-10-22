class Solution:

    def encode(self, strs: List[str]) -> str:


        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res
    def decode(self, s: str) -> List[str]:

        list_str = []

        i = 0
        while i < len(s):

            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i : j])

            string = s[j + 1 : j + 1 + length]
            list_str.append(string)

            i = j + 1 + length


        return list_str

