from bs4 import BeautifulSoup
import requests
import sqlite3


DB_NAME = "MobileProduct.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()



cursor.execute("""
CREATE TABLE IF NOT EXISTS MobileDetails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    product_name TEXT,
    storage TEXT,
    ram TEXT,
    color TEXT,
    rating REAL
)
""")

cursor.execute("SELECT id, title, link FROM MobileData")
products = cursor.fetchall()
headers = {"User-Agent": "Mozilla/5.0"}

for product in products:

    product_id, title, link = product
    print("\n" + "=" * 70)
    print("محصول:", title)

    try:
        response = requests.get(link, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        h1 = soup.find("h1")
        product_name = h1.get_text(" ", strip=True)


        all_divs = soup.find_all("div",class_="bg-background-100")

        storage_results = []
        storage = None
        ram = None

        for div in all_divs:

            p_tag = div.find("p",class_="text-primary-shade-2")

            if p_tag:
                text = p_tag.get_text(strip=True)
                if "گیگابایت" in text:
                    storage_results.append(text)


        if len(storage_results) >= 2:

            storage = storage_results[0]
            ram = storage_results[1]

        elif len(storage_results) == 1:

            ram = storage_results[0]
        
        color = None
        color_label = soup.find(string=lambda text:text and text.strip() == "رنگ:")

        if color_label:
            parent = color_label.parent
            for element in parent.parent.find_all(string=True):
                value = element.strip()
                if value and value != "رنگ:":
                    color = value
                    break

        rating = None

        rating_label = soup.find(string=lambda text:text and text.strip() == "نمره کالا از دید کاربران")

        if rating_label:
            for element in rating_label.parent.find_all_previous():
                value = element.get_text(" ", strip=True)

                try:
                    number = float(value)
                    if 0 <= number <= 5:
                        rating = number
                        break
                except ValueError:
                    continue
        query = '''
            INSERT INTO MobileDetails
            (product_id, product_name, storage, ram, color, rating)
            VALUES (?, ?, ?, ?, ?, ?)
            '''
        cursor.execute (query, (product_id,product_name,storage,ram,color,rating))
        conn.commit()

        print("نام:", product_name)
        print("حافظه داخلی:", storage)
        print("RAM:", ram)
        print("رنگ:", color)
        print("امتیاز کاربران:", rating)

        print("✅ اطلاعات در دیتابیس ذخیره شد.")


    except requests.RequestException as error:
        print("خطا در دریافت صفحه:")
        print(error)

conn.close()