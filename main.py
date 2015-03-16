#from crawler import Crawler
import crawler


c = crawler.Crawler('http://udacity.com/cs101x/urank/index.html')
index, graph = c.crawl_web()
ranks = crawler.compute_ranks(graph)
keyword = raw_input("Input the keyword: ")

print crawler.lucky_search(index, ranks, keyword)
print crawler.all_search(index, ranks, keyword)

