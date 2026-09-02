class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_list = []

        for word in strs:
            encoded_list.append(str(len(word)))
            encoded_list.append("#")
            encoded_list.append(word)

        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:

        decoded_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1

            word = s[i:i + length]
            decoded_list.append(word)

            i += length

        return decoded_list