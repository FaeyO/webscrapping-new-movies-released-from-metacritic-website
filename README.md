# Web Scraping Metacritic for New Released Movies

This project utilizes Scrapy and Selenium to scrape new movie releases from the Metacritic website. Metacritic is a popular platform for aggregating reviews and ratings for movies, games, music, and TV shows.

## Objective

The objective of this project is to collect data on new movie releases, including movie title, release date, description, Metascore, and image link, from the Metacritic website.

## Technologies Used

- Python
- Scrapy
- Selenium

## Installation

1. Clone this repository to your local machine:

```
git clone <repository_url>
```

2. Install the required Python packages:

```
pip install scrapy selenium
```

## Usage

1. Navigate to the project directory:

```
cd metacritic-movie-scraper
```

2. Run the Scrapy spider to scrape data from the Metacritic website:

```
scrapy crawl new
```

## Process

1. **Setup**: The project is set up with Scrapy and Selenium to handle web scraping of dynamic content rendered by JavaScript.

2. **Scraping**: The Scrapy spider navigates through the Metacritic website, simulating user behavior with Selenium to access dynamically rendered content.

3. **Data Collection**: For each movie listed on the website, the spider extracts relevant information such as movie title, release date, description, Metascore, and image link.

4. **Data Processing**: The scraped data is processed and formatted within the Scrapy spider.

5. **Saving Data**: The formatted data is saved to a CSV file for further analysis and use.

## Output

The output CSV file contains the following columns:

- Movie Title
- Release Date
- Description
- Metascore
- Image Link

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


### website view

![image](https://github.com/FaeyO/webscrapping-new-movies-released-from-metacritic-website/assets/118575325/312b27f6-2741-4a28-a7c0-d0832136615b)
