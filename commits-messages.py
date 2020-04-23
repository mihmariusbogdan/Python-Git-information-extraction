from pydriller import RepositoryMining

for commit in RepositoryMining("/home/mih/guava").traverse_commits():
    f = open("result.txt", "w")
    f.write(commit.msg)
    f.close()
