import sys

class Solution(object):

    def __init__(self):
        self.bits = ['0'] * (B + 1)
        self.cur_idx = self.same_pair_idx = self.diff_pair_idx = 0

    @staticmethod
    def _read_bit_at(idx):
        print(idx)
        sys.stdout.flush()
        return input()

    def _waste_queries(self):
        if self.same_pair_idx <= 0:
            self._read_bit_at(1)
        if self.diff_pair_idx <= 0:
            self._read_bit_at(1)
    
    def _get_fluctuation(self):
        is_complemented = is_reversed = False
        # Check for complement first
        if self.same_pair_idx > 0 and self.bits[self.same_pair_idx] != self._read_bit_at(self.same_pair_idx):
            is_complemented = True
        # Check for reverse next
        if self.diff_pair_idx > 0:
            is_reversed = (
                    is_complemented and self.bits[self.diff_pair_idx] == self._read_bit_at(self.diff_pair_idx)
                ) or (
                    not is_complemented and self.bits[self.diff_pair_idx] != self._read_bit_at(self.diff_pair_idx)
                )
        # For readable code
        self._waste_queries()
        return is_complemented, is_reversed

    def _update_bits(self):
        is_complemented, is_reversed = self._get_fluctuation()
        if is_complemented:
            self.bits = ['0' if self.bits[i] == '1' else '1' for i in range(len(self.bits))]
        if is_reversed:
            self.bits[1:] = self.bits[1:][::-1]

    def _find_same_and_diff_pairs(self):
        if self.bits[self.cur_idx] == self.bits[B - self.cur_idx + 1] and self.same_pair_idx <= 0:
            self.same_pair_idx = self.cur_idx
        if self.bits[self.cur_idx] != self.bits[B - self.cur_idx + 1] and self.diff_pair_idx <= 0:
            self.diff_pair_idx = self.cur_idx

    def _perform_actions(self):
        # Always waste two queries on checking fluctuation and update existing bits
        self._update_bits()
        # Perform another 8 queries for reading new data
        for _ in range(4):
            self.cur_idx += 1
            if self.cur_idx > B // 2:
                return
            self.bits[self.cur_idx] = self._read_bit_at(self.cur_idx)
            self.bits[B - self.cur_idx + 1] = self._read_bit_at(B - self.cur_idx + 1)
            # Look for same and diff pairs if not found yet
            self._find_same_and_diff_pairs()

    def solve(self):
        while self.cur_idx <= B // 2:
            self._perform_actions()
        print(''.join(self.bits[1:]))
        sys.stdout.flush()
        if input() == 'N':
            exit()

T, B = map(int, input().split())
for _ in range(T):
    Solution().solve()
