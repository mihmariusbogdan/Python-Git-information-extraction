from pydriller.metrics.process.commits_count import CommitsCount
from pydriller.metrics.process.lines_count import LinesCount

metric = LinesCount(path_to_repo='/home/mih/guava',
from_commit='db3929bd79ef57f8da40515b663f40200a941fa8',
to_commit='25e4590775329cdcee32423e5819ffdc08077add')
added_count = metric.count_added()

metric = CommitsCount(path_to_repo='/home/mih/guava',
from_commit='db3929bd79ef57f8da40515b663f40200a941fa8',
to_commit='25e4590775329cdcee32423e5819ffdc08077add')
files = metric.count()



f = open("result2.txt", "w")
for (key, value), (key2, value2) in zip(files.items(), added_count.items()):
    f.write('File: ' + str(key) + ' has ' + str(value) + ' commits and ' + str(value2) + ' lines of code. \n')
f.close()
