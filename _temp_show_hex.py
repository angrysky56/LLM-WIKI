lines = open('/tmp/arxiv_results.md','rb').readlines()[:5]
for line in lines:
    print(repr(line))