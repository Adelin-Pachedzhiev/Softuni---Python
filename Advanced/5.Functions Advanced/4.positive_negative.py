input_li = [int(n) for n in input().split(' ')]

pos_li=[ n for n in input_li if n > 0]
neg_li=[ n for n in input_li if n < 0]
sum_pos = sum(pos_li)
sum_neg = sum(neg_li)
print(sum_neg)
print(sum_pos)

print("The negatives are stronger than the positives" if abs(sum_neg) > sum_pos else 'The positives are stronger than the negatives')
