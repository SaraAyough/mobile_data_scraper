Mobile Data Scraper

A Python web scraping project that collects mobile phone information from Technolife, stores the data in SQLite, and displays it through a Streamlit web application.

Features

- Scrape mobile phone titles, prices, images, and product links
- Scrape product details such as:
  - RAM
  - Storage
  - Color
  - User rating
- Store scraped data in SQLite
- Display products in a responsive Streamlit interface

Technologies

- Python
- Requests
- BeautifulSoup
- SQLite
- Pandas
- Streamlit

Project Structure

mobile-data-scraper/
├── src/
│   ├── scrape_products.py
│   ├── scrape_details.py
│   └── app.py
├── .gitignore
├── README.md
└── requirements.txt

How to Run

Install the dependencies:

pip install -r requirements.txt

Run the scripts in this order:

1. Scrape mobile products

python src/scrape_products.py

This creates the "MobileProduct.db" database and stores the basic product information.

2. Scrape product details

python src/scrape_details.py

This extracts additional product details and stores them in the database.

3. Run the Streamlit application

streamlit run src/app.py

The Streamlit app displays the scraped mobile products and their details.

Database

The project uses SQLite with two tables:

- "MobileData" — basic product information
- "MobileDetails" — additional product specifications

«The SQLite database is generated locally and is not included in the repository.»

👩‍💻 Author

Sara Ayough

⭐ If you find this project useful, feel free to explore the repository.