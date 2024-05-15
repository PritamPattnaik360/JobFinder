# JobFinder
Is a Flask web application designed to scrape job postings from LinkedIn based on user-defined parameters, visualize job title distribution, and save scraped data as a CSV file for further analysis.

## Summary 
The LinkedIn Job Scraper project provides users with a convenient way to gather real-time job postings from LinkedIn's extensive database. With a user-friendly interface built using Flask, users can specify their desired job title, location, and the number of times to scrape, empowering them to access relevant job opportunities quickly and efficiently.
## Application in Action
coming soon
## How it works
The LinkedIn Job Scraper provides a straightforward process for users to scrape job postings from LinkedIn: 
Input Job Details: Users start by entering the job title they are interested in, along with the desired location and the number of times they want to scrape job postings. Scrape Job Postings: Upon submitting the form, the Flask web application sends requests to the LinkedIn job search API using Python's requests library. The responses are then parsed using BeautifulSoup to extract relevant job information from the HTML structure of the LinkedIn pages. Visualize Data: The scraped job data is organized into a pandas DataFrame, allowing users to visualize the distribution of job titles using Plotly, an interactive graphing library. This provides users with insights into the types of job opportunities available based on their search criteria. Save Data for Analysis: Additionally, the scraped job data is automatically saved as a CSV file (Data.csv) within the project directory. This allows users to further analyze the data using external tools or import it into other applications for additional processing or reporting.
By following these simple steps, users can efficiently gather real-time job postings from LinkedIn, gain insights into the job market, and save valuable data for future reference or analysis.

## Dependencies Utilized
- [Python](https://www.python.org)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [pandas](https://pypi.org/project/pandas/)
- [plotly](https://plotly.com/python/)
- [Bootstrap](https://getbootstrap.com/)
