import json

import requests
def main():
	isbn = input("ISBN: ")
	res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "bj5nIMELv3WJ17pmfNxpg", "isbns":isbn})
	if res.status_code != 200:
		raise Exception("ERROR 404: API request not found.")
	data = res.json()
	count = data['books'][0]['work_ratings_count']
	score = data['books'][0]['average_rating']
	print(f"The number of ratings that this book has received is {count} . And the book's average score out of 5 is {score}")
 
if __name__ == "__main__":
    main()


