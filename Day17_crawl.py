import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy

async def main():
    # Configure a 2-level deep crawl
    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=2,
            include_external=False,
            #max_pages=50 # Limit to 50 pages for demonstration
        ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True
    )

    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun("https://www.wikipedia.org", config=config)

        print(f"Crawled {len(results)} pages in total")

        # Save results to text file
        with open("crawl_results3.txt", "w", encoding="utf-8") as f:
            f.write(f"Crawled {len(results)} pages in total\n\n")

            for i, result in enumerate(results, start=1):
                f.write(f"Page {i}\n")
                f.write(f"URL: {result.url}\n")
                f.write(f"Depth: {result.metadata.get('depth', 0)}\n")
                f.write("-" * 50 + "\n")
                f.flush()
                
        # Access individual results (for console preview)
        for result in results[:3]:  # Show first 3 results
            print(f"URL: {result.url}")
            print(f"Depth: {result.metadata.get('depth', 0)}")

if __name__ == "__main__":
    asyncio.run(main())
