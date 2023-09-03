from src.utils import converter, file_sort
from src.main import list_date, operations, list_operation, operation_last_5, list_5


def test_converter():
    assert converter("Visa Gold 9447344650495960") == "Visa Gold 9447 34** **** 5960"
    assert converter("MasterCard 3152479541115065") == "MasterCard 3152 47** **** 5065"
    assert converter("Счет 27248529432547658655") == "Счет **8655"

def test_file_sort():
    assert file_sort(list_date, operations) == list_operation

list_5_ = operation_last_5(list_5)

def test_operation_last_5():
    assert operation_last_5(list_5) == list_5_
