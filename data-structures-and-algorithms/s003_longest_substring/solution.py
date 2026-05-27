class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        character_index_map: dict[str, int] = {}
        global_max_length: int = 0
        local_max_length: int = 0

        for index, character in enumerate(s):
            if character in character_index_map:
                character_index_map = {}

                global_max_length = max(global_max_length, local_max_length)

                character_index_map[character] = index
                local_max_length = 1
            else:
                character_index_map[character] = index
                local_max_length += 1

        global_max_length = max(global_max_length, local_max_length)

        return global_max_length
