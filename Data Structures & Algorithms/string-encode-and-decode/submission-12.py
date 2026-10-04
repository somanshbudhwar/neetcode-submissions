class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return "<empty-splitter>"
        return "<splitter>".join(strs)

    def decode(self, s: str) -> List[str]:
        if s is "<empty-splitter>":
            return []
        return s.split("<splitter>")
