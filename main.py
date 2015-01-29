from crawler import Crawler


def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None 

c = Crawler('http://udacity.com/cs101x/urank/index.html')
index, graph = c.crawl_web()
print lookup(index, "everything")

