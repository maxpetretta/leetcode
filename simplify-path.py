class Solution:
    def simplifyPath(self, path: str) -> str:
        # Assemble new path as a stack, following given rules, O(n), O(n)
        folders = [folder.strip() for folder in path.split("/")]
        
        shortened = []
        for folder in folders:
            if folder == "." or folder == "":
                continue
            elif folder == ".." and len(shortened) > 0:
                shortened.pop()
            elif folder != "..":
                shortened.append(folder)
            
        # Assemble final string
        final = "/" + "/".join(shortened)
        return final


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.simplifyPath("/home/"))
    print(solver.simplifyPath("/../"))
    print(solver.simplifyPath("/home//foo/"))
    print(solver.simplifyPath("/"))
    print(solver.simplifyPath("///"))
