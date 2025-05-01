from student_registration import registration
def test_case():
    assert registration("Ankitha","123456","RD012345")=="Registration successful"
    assert registration("nanditha","123456","RD012345")=="invalid student name"
    assert registration("Ankitha","8765","RD012345")=="invalid student id"
    assert registration("Ankitha","123456","RD0123")=="wrong student income number"
    print("All tests correct")

if __name__=="__main__":
    test_case()


