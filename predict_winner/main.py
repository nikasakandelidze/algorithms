class Solution:
    # The definition of a problem is to return True if player 1 CAN win the game.
    #   Meaning that even if there is one combination of choosing numbers where player 1 wins, answer is true
    #
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def recursive_search(p1_score, p2_score, p1_time, start_idx, end_idx):
            if start_idx > end_idx:
                return p1_score >= p2_score
            first = nums[start_idx]
            last = nums[end_idx]
            if p1_time:
                p1_temp1 = recursive_search(p1_score + first, p2_score, False, start_idx+1, end_idx)
                p1_temp2 = recursive_search(p1_score + last, p2_score, False, start_idx, end_idx-1)
                return p1_temp1 or p1_temp2
            else:
                p2_temp1 = not recursive_search(p1_score, p2_score + first, True, start_idx+1, end_idx)
                p2_temp2 = not recursive_search(p1_score, p2_score + last, True, start_idx, end_idx-1)
                return not(p2_temp1  or p2_temp2)
        return recursive_search(0, 0, True, 0, len(nums)-1)
