#Function: This program determines if a student will be admitted or rejected.
#Input:  Interactive
#Output: Accept or Reject

# Get input and convert to correct data type for testScore and classRank

# Test using admission requirements and print Accept or Reject
test_score = float(input("Enter the test score: "))
class_rank = int(input("Enter the class rank: "))

if test_score >= 90:
    if class_rank >= 25:
        print("Accept")
    else:
        print("Reject")
elif test_score >= 80:
    if class_rank >= 50:
        print("Accept")
    else:
        print("Reject")
elif test_score >= 70:
    if class_rank >= 75:
        print("Accept")
    else:
        print("Reject")
else:
    print("Reject")
