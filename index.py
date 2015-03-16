def add_page_to_index(index, url, content): 
    words = content.split() 
    for word in words: 
        add_to_index(index, word, url) 

def add_to_index(index, keyword, url): 
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]     

def lookup(index, keyword): 
    if keyword in index:
        return index[keyword]
    return None
   
def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}  # ranks at time t-1
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {} # ranks at time t
        for page in graph:
            newrank = (1 - d) / npages
           
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len (graph[node]))
                    
            newranks[page] = newrank
        ranks = newranks
    return ranks
    
"""
rank(page, 0) = 1/npages

   rank(page, t) = (1-d)/npages 

                   + sum (d * rank(p, t - 1) / number of outlinks from p) 
              over all pages p that link to this page 
"""   
