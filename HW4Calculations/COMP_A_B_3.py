''' The original units for this code is bytes. This is use for the problem that COMPUTER A AND B and for three questions '''

First_Segment_Contains = 65
Second_Segment_Contains = 68
Third_Segment_Contains = 91
First_12_Bytes = "0628 E218 0033 4500 0000 4E20"
Segment_from_Computer_B = 74

#Answer 1
First_12_Bytes = First_12_Bytes.replace(" ", "")
Source_Port = First_12_Bytes[0:4]
Source_Port_Decimal = int(Source_Port, 16)
Destination_Port = First_12_Bytes[4:8]
Destination_Port_Decimal = int(Destination_Port, 16)
Sequence_Number = First_12_Bytes[8:16]
Sequence_Number_Decimal = int(Sequence_Number, 16)
print(Source_Port_Decimal,",", Destination_Port_Decimal,",", Sequence_Number_Decimal - First_Segment_Contains - 1,",", 1,",", 0,",", 0)

#Answer 2
Acknowledgement_Number = First_12_Bytes[16:]
Acknowledgement_Number_Decimal = int(Acknowledgement_Number, 16)
print(Destination_Port_Decimal,",", Source_Port_Decimal,",", Acknowledgement_Number_Decimal - 1,",", Sequence_Number_Decimal - First_Segment_Contains,",", 1,",", 1,",", 0)

#Answer 3
print(Source_Port_Decimal,",", Destination_Port_Decimal,",", Sequence_Number_Decimal - First_Segment_Contains,",", Acknowledgement_Number_Decimal,",", 0,",", 1,",", 0)