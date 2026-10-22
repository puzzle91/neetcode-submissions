class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        Format: {length}#{string} for each string
        """
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string back to a list of strings.
        """
        result = []
        i = 0

        while i < len(s):
            # Find the delimiter '#'
            delimiter_pos = i
            while s[delimiter_pos] != '#':
                delimiter_pos += 1
            
            # Extract the length
            length = int(s[i:delimiter_pos])
            
            # Extract the string of that length
            start = delimiter_pos + 1
            end = start + length
            result.append(s[start:end])
            
            # Move to the next encoded string
            i = end

        return result