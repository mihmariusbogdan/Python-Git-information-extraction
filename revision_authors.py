from pydriller.metrics.process.commits_count import CommitsCount
from pydriller.metrics.process.contributors_count import ContributorsCount

metric = ContributorsCount(path_to_repo='/home/mih/spring-framework',
from_commit='8119659fb1e4ae6fabe8897c42ba7629fda07b21',
to_commit='c2f7b6575156a7c3e049e17248acb6b580ba899f')
author = metric.count()




metric = CommitsCount(path_to_repo='/home/mih/spring-framework',
from_commit='8119659fb1e4ae6fabe8897c42ba7629fda07b21',
to_commit='c2f7b6575156a7c3e049e17248acb6b580ba899f')
files = metric.count()



f = open("result3.txt", "w")
for (key, value), (key2, value2) in zip(files.items(), author.items()):
    f.write('File: ' + str(key) + ' has ' + str(value) + ' commits and ' + str(value2) + ' authors. \n')
f.close()