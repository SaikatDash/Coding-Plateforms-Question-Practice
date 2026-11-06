class Solution:
    def generateUsernames(self, arr):
        # Set of names that are initially reserved.
        # These names cannot be used as generated usernames.
        reserved = set(arr)

        # Map each base name to the next suffix number to try.
        # Example: next_suffix["aba"] = 1 means try "aba1" next.
        next_suffix = {}

        # Final usernames in the same order as the input.
        ans = []

        for name in arr:
            # If this exact original name has not been assigned yet,
            # assign it unchanged.
            if name not in next_suffix:
                ans.append(name)

                # Mark that this base name has already been assigned once.
                next_suffix[name] = 1
                continue

            # This is a duplicate base name.
            # Start from the next suffix remembered for this base name.
            suffix = next_suffix[name]

            # Skip any username that is initially reserved
            # or already assigned to someone else.
            while name + str(suffix) in reserved:
                suffix += 1

            username = name + str(suffix)

            # Mark the generated username as used.
            reserved.add(username)

            # Remember the next suffix for this base name.
            next_suffix[name] = suffix + 1

            ans.append(username)

        return ans