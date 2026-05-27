class Solution:
    # might be parametrized, making a general-purpose stack-based validator (OCP)
    mapping = {")": "(", "}": "{", "]": "["}

    def __init__(self) -> None:
        self.stack: list[str] = []

    def isValid(self, s: str) -> bool:
        return self._is_valid(s)

    def _is_valid(self, sequence: str) -> bool:
        """
        Checks if every opening bracket has a corresponding closing bracket in the correct order.

        :param sequence: str: Sequence to check
        :return: bool: True if the sequence is valid
        """
        if len(sequence) < 2:
            return False

        valid_chars: set[str] = set(self.mapping.keys()).union(self.mapping.values())

        for item in sequence:
            if item not in valid_chars:
                return False

            if self._is_closing_bracket(item):
                if not self._top_matches_opening_bracket(item):
                    return False

                self.stack.pop()
            else:
                self.stack.append(item)  # push

        return not self.stack

    def _is_closing_bracket(self, item: str) -> bool:
        return item in self.mapping.keys()

    def _top_matches_opening_bracket(self, item: str) -> bool:
        return bool(self.stack) and self.stack[-1] == self.mapping[item]
