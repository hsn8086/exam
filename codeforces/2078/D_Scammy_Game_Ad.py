
for _ in range(int(input())):
    n = int(input())
    dp = {(1, 1)}
    for _ in range(n):
        inp = input().split()
        left_inp = inp[:2]
        right_inp = inp[2:]
        left_op, left_v = left_inp[0], int(left_inp[1])
        right_op, right_v = right_inp[0], int(right_inp[1])
        new_dp = set()
        for left, right in dp:
            if left_op[0] == "+":
                add_l = left_v
            else:
                add_l = left * (left_v - 1)

            if right_op[0] == "+":
                add_r = right_v
            else:
                add_r = right * (right_v - 1)

            total_add = add_l + add_r

            for a in range(total_add + 1):
                new_l = left + a
                new_r = right + (total_add - a)
                new_dp.add((new_l, new_r))
        dp = new_dp
    print(max(left + right for left, right in dp))
