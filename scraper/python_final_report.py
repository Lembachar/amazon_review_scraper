from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import random

opts = Options()
opts.add_argument(r"--user-data-dir=C:\edge_amazon")
opts.add_argument("--start-maximized")

service = Service(r"C:\Users\hp\Desktop\edgedriver\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=opts)
wait = WebDriverWait(driver, 30)

rows = []
seen_ids = set()

STAR_FILTERS = {
    "five_star": "5 stars",
    "four_star": "4 stars",
    "three_star": "3 stars",
    "two_star": "2 stars",
    "one_star": "1 star"
}

SORT_MODES = {
    "helpful": "helpful",   
    "recent": "recent"
}

def crawl_product(asin, product_name, max_pages_per_view=10):
    for star_key, star_label in STAR_FILTERS.items():
        for sort_key in SORT_MODES:

            print(f"\n{product_name} | {star_label} | sort={sort_key}")

            base_url = (
                f"https://www.amazon.com/product-reviews/{asin}"
                f"/?filterByStar={star_key}"
                f"&sortBy={sort_key}"
                f"&reviewerType=all_reviews"
            )

            driver.get(base_url)

            for page in range(1, max_pages_per_view + 1):
                print(f"{product_name} | {star_label} | {sort_key} | page {page}")

                try:
                    wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "li[data-hook='review']")
                    ))
                except:
                    break

                reviews = driver.find_elements(By.CSS_SELECTOR, "li[data-hook='review']")
                if not reviews:
                    break

                first_review = reviews[0]
                new_on_page = 0

                for r in reviews:
                    
                    driver.execute_script("arguments[0].scrollIntoView(true);", r)
                    time.sleep(0.15)

                    review_id = r.get_attribute("id")
                    if not review_id or review_id in seen_ids:
                        continue
                    seen_ids.add(review_id)
                    new_on_page += 1

                    rating = ""
                    try:
                        rating = r.find_element(
                            By.CSS_SELECTOR, "i[data-hook='review-star-rating'] span"
                        ).get_attribute("innerHTML")
                    except:
                        try:
                            rating = r.find_element(
                                By.CSS_SELECTOR, "span.a-icon-alt"
                            ).get_attribute("innerHTML")
                        except:
                            pass

                    
                    try:
                        title = r.find_element(
                            By.CSS_SELECTOR, "a[data-hook='review-title'] span"
                        ).text
                    except:
                        title = ""

                    
                    try:
                        body = r.find_element(
                            By.CSS_SELECTOR, "span[data-hook='review-body'] span"
                        ).text
                    except:
                        body = ""

                    
                    try:
                        date = r.find_element(
                            By.CSS_SELECTOR, "span[data-hook='review-date']"
                        ).text
                    except:
                        date = ""

                    
                    verified = False
                    try:
                        r.find_element(By.CSS_SELECTOR, "span[data-hook='avp-badge']")
                        verified = True
                    except:
                        pass

                    
                    helpful = 0
                    try:
                        h = r.find_element(
                            By.CSS_SELECTOR, "span[data-hook='helpful-vote-statement']"
                        ).text.lower()
                        for w in h.split():
                            if w.replace(",", "").isdigit():
                                helpful = int(w.replace(",", ""))
                                break
                    except:
                        pass

                    rows.append([
                        product_name,
                        star_label,
                        sort_key,
                        rating,
                        date,
                        verified,
                        helpful,
                        title,
                        body
                    ])

                if new_on_page == 0:
                    break

               
                pd.DataFrame(rows, columns=[
                    "product",
                    "star_group",
                    "sort_mode",
                    "rating",
                    "date",
                    "verified_purchase",
                    "helpful_votes",
                    "review_title",
                    "review_content"
                ]).to_csv("amazon_reviews_PROGRESS.csv", index=False, encoding="utf-8-sig")

                time.sleep(random.uniform(2.5, 4.0))

                
                try:
                    next_btn = driver.find_element(By.CSS_SELECTOR, "li.a-last a")
                    driver.execute_script("arguments[0].click();", next_btn)
                    wait.until(EC.staleness_of(first_review))
                except:
                    break

crawl_product("B09SVSBVP1", "HP Chromebook", max_pages_per_view=10)
crawl_product("B0BSMSYM9N", "Canon Printer", max_pages_per_view=10)

driver.quit()

df = pd.DataFrame(rows, columns=[
    "product",
    "star_group",
    "sort_mode",
    "rating",
    "date",
    "verified_purchase",
    "helpful_votes",
    "review_title",
    "review_content"
])

df.to_csv("amazon_reviews_FINAL2.csv", index=False, encoding="utf-8-sig")
print("DONE. Total unique reviews:", len(df))
