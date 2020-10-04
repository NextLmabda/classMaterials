from functions import Slice

sent = 'We are in Data Science Training having Fun'
sl = Slice(2, 20, 3, sent)

sl.fit()

output1 = sl.transform()

print(output1)

output2 = sl.fit_transform()

print(output2)

