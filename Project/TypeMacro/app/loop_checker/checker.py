from app.model.commands.full_macro import FullMacro
import warnings


class Checker:
    visited: set[FullMacro]
    recursion_stack: set[FullMacro]

    def detect_cycle(self, full_macros: list[FullMacro], file_name: str):
        self.visited = set()
        self.recursion_stack = set()
        # Check all FullMacro nodes
        for full_macro in full_macros:
            if full_macro not in self.visited:
                if self.dfs(full_macro, full_macros):
                    warnings.warn("There is a cycle detected in: " + file_name)
                    return

    # Helper function for DFS
    def dfs(self, full_macro: FullMacro, full_macros: list[FullMacro]) -> bool:
        if full_macro in self.recursion_stack:
            # Cycle detected
            return True
        if full_macro in self.visited:
            # Already processed, no cycle here
            return False

        # Mark the current FullMacro as visited and in the recursion stack
        self.visited.add(full_macro)
        self.recursion_stack.add(full_macro)

        # Traverse dependencies
        for macro_command in full_macro.sequence:
            for full_macro_check in full_macros:
                if full_macro_check.is_activated_by(macro_command):
                    if self.dfs(full_macro_check, full_macros):
                        return True

        # Backtrack
        self.recursion_stack.remove(full_macro)
        return False
