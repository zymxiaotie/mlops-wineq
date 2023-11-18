import pytest 

class NotInRange(Exception):
    def __init__(self, message="value not in range"):
        self.message = message
        super().__init__(self.message)

# example of a test case
def test_generic(): # convention: start with "test_..."
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange
    
# # example of a test case
# def test_generic():
#     a = 2
#     b = 2
#     assert a==b