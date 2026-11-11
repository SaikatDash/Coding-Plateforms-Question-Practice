class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """If k equals the length of the cardPoints,
        the maximum points are achieved by picking all cards.
        TC - O(N) (sum() function takes N time, where N is len cardPoints)
        SC - O(1), No extra space used."""
        if k == len(cardPoints):
            return sum(cardPoints)

        max_sum = 0
        left_sum = 0
        right_sum = 0
        n = len(cardPoints)
        # Take all k from the left initially
        for i in range(k):
            left_sum += cardPoints[i]
        max_sum = left_sum

        # Slide: give back from left, take from right
        right_index = n - 1
        for i in range(k - 1, -1, -1):
            left_sum -= cardPoints[i]          # remove one from the left window
            right_sum += cardPoints[right_index]  # add one from the right tail
            right_index -= 1
            max_sum = max(max_sum, left_sum + right_sum)
        return max_sum