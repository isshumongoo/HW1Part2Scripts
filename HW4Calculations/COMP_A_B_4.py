''' The original units for this code is bytes. This is use for the problem that COMPUTER A AND B and for four questions '''

First_Segment_Contains = 106
Second_Segment_Contains = 78
Third_Segment_Contains = 97
First_12_Bytes = "0429 E206 0022 06F0 0000 1770"
Segment_from_Computer_B = 84

#Answer 1
First_12_Bytes = First_12_Bytes.replace(" ", "")
lastTwo = First_12_Bytes[16:]
lastTwoDecimal = int(lastTwo, 16)
thirdFourth = First_12_Bytes[8:16]
thirdFourthDecimal = int(thirdFourth, 16)
print(lastTwoDecimal,thirdFourthDecimal + Second_Segment_Contains)

#Answer 2
print(lastTwoDecimal,thirdFourthDecimal - First_Segment_Contains)

#Answer 3
print(thirdFourthDecimal + Second_Segment_Contains, lastTwoDecimal + Segment_from_Computer_B )

#Answer 4
print(lastTwoDecimal,thirdFourthDecimal - First_Segment_Contains)
