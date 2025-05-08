from scrapy.crawler import CrawlerProcess, CrawlerRunner
from links.links.spiders.LinkSpider import LinkSpider
from populate_db import *
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks

os.environ["OPENAI_API_KEY"] = ""

def Scrape_Links():
    allowed_domains = input("\nAdd Allowed domains seperated by ',': ").split(",")
    allowed_domains = list(map(str.strip, allowed_domains))
    start_urls = input("\nAdd Start Urls seperated by ',': ").split(",")
    start_urls = list(map(str.strip, start_urls))
    filename = input("\nEnter CSV Filename: ")

    runner = CrawlerRunner(settings={
        "FEEDS": {f"crawl_data/{filename}.csv": {"format":"csv"}},
    })
    runner.crawl(LinkSpider, 
                  allowed_domains=allowed_domains, 
                  start_urls=start_urls
                  )

    @inlineCallbacks
    def start_crawl():
        yield runner.crawl(LinkSpider, 
                  allowed_domains=allowed_domains, 
                  start_urls=start_urls
                  )
        reactor.stop()

    start_crawl()
    reactor.run()    

def Train_Model():

    urls = urls_from_csv(input("\nEnter CSV Name: "))

    # Create (or update) the data store.
    for url in urls:
        data = load_documents(url)
        chunks = split_documents(data)
        add_to_chroma(chunks)


def Query_Model():
    return

    
def handler():

    print("\n------- DESC AI -------\n")
    print("Options:\n")
    print("1. Scrape Links\n2. Train Model\n3. Query Model\n\n")

    option = input("Enter Choice: ")
    if option == "1":
        Scrape_Links()
    elif option == "2":
        Train_Model()
    elif option == "3":
        Query_Model()
    else:
        print("\nWrong Option, Retry")




if __name__=="__main__":
    while True:
        handler()