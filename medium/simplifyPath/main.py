class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        dirs = path.split("/")
        for dir in dirs[1:]:
            if dir == "" or dir == ".":
                continue

            if dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)

        return "/" + "/".join(stack)


print(Solution().simplifyPath("/.../a/../b/c/../d/./"))
