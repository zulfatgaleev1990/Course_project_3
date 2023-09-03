import json
from src.utils import file_sort, file_reads
from src.utils import operation_last_5, empty_dict_filter


operations = file_reads()
list_date = empty_dict_filter(operations)
list_operation = file_sort(list_date, operations)
list_5 = list_operation[:5]
operation_last_5(list_5)
