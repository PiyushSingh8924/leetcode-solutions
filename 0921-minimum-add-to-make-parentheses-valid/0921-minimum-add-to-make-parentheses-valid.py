class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        for ch in s:
            if ch == '(':
                st.append(ch)
            elif ch == ')':
                if st and st[-1] == '(':
                    st.pop()
                else:
                    st.append(ch)
        return len(st)
