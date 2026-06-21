from src.excel.reader import Reader
from src.excel.writer import Writer
from src.logic.load_aggregator import LoadAggregator
from src.logic.load_assigner import LoadAssigner

reader = Reader()

old_records = reader.read("src/data/15 вариант.xls")

autumn_records = reader.read("src/data/Список 15вар - осень.xls")

spring_records = reader.read("src/data/Список 15вар - весна.xls")

current_records = (autumn_records + spring_records)

aggregator = LoadAggregator()

current_records = (aggregator.aggregate(current_records))

assigner = LoadAssigner(old_records)

result_records = assigner.assign(current_records)

writer = Writer()

writer.write(result_records, "src/data/result.xlsx")

print("Файл result.xlsx сохранен")
