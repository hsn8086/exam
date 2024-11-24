G = 10
inp_f, inp_i = input().rsplit(maxsplit=1)
h, si, v, l_, k = map(float, inp_f.split())
n = int(inp_i)
d_of_car = h

count=0
for x in range(n):
    s_left = si - x
    t_left = s_left / v
    fall_d_left = 0.5 * G * (t_left**2)
    #print(fall_d_left,d_of_car,s_left,t_left)
    if fall_d_left > d_of_car+0.0001:
        continue

    s_right = si + l_ - x
    t_right = s_right / v
    fall_d_right = 0.5 * G * t_right**2
    if fall_d_right < d_of_car-k-0.0001:
        continue
    
    count+=1

print(count)