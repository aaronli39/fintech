# Stock Price Queries in MongoDB

### The Goal

We've got a database with historical stock prices from Amazon (AMZN), Apple (AAPL), IBM (IBM) and Microsoft (MSFT). The data is stored in a MongoDB where each entry/document is in the following format:

```json
{
	"symbol" : "AMZN",
	"month" : "Mar",
	"year" : 2004,
	"price" : 43.28
}

```

Your challenge will be to query the MongoDB to produce a single result or multiple results according to the descriptions below.

## Environment Setup

We're going to continue working in your cloud9 environment, so clone this repository into your environment as you've done before.

You'll also need to install PyMongo and dnspython in the Cloud9 IDE to help connect to the MongoDB database:

```bash
pip install pymongo
pip install dnspython

```

### Running stocks.py

To run the `stocks.py` file, type `python stocks.py` in the Terminal in your IDE. Anything you `print()` will be shown in the Terminal, too.

# Challenges

## Warmups

#### 1. List all entries in the `prices` collection in the `stock-prices` database.

> You'll notice we've given you a bit help on this one to start out.
> 
> Any query that may return multiple documents is returned as a `Cursor`, and this is a data structure we haven't seen before. To convert the `Cursor` into something you're more familiar with, we can wrap the result in the `list()` method, in a similar way to how we used `dict()` before:
>
> ```python
> data = list(collection.find({...}))
> ```
>
> You can also iterate over the `Cursor` using a `for` loop:
>
> ```python
> for entry in data:
> 	print(entry)
> ```
> 
> So we've given you the search query solution. What's missing?

#### 2. List all historical Microsoft stock prices

#### 3. List all historical stock prices from 2004

#### 4. List all historical stock prices from September

#### 5. List all historical stock prices from September 2004

#### 6. List all historical stock prices in order from lowest value to highest value

#### 7. List all historical stock prices in order from highest value to lowest value

#### 8. List the first 5 historical stocks in the database.

#### 9. Find an historical stock that was valued at $100.52.

#### 10. How many entries are there in the database for Apple stock prices?

> Here's a bit of help:
>
> - [MongoDB .count() Method](https://docs.mongodb.com/manual/reference/method/db.collection.count/)
>
> You can use the `.count()` method to get the number of entries in the `Cursor`.

## Showtime

#### 11. List the first 10 Apple entries in the database.

#### 12. List the January IBM stock prices from lowest to highest.

#### 13. List all historical stock prices over $200.00

> Here's a bit of help:
> 
> - [MongoDB Query Comparison Operators](https://docs.mongodb.com/manual/reference/operator/query-comparison/)

#### 14. List all historical stock prices less than $10.00.

#### 15. What company's (or companies') stock was valued at $9.78 in October, 2000? Return only the name of the company.

#### 16. What was the price of Amazon's Stock in August, 2006? Return only the price.

#### 17. What was the highest historical price of Microsoft's stock? Return only the price.

#### 18. For how many months (in the historical database) has Apple's stock price been greater than $100.00? Return only the number of months.

## Additional Documentation

- [MongoDB Query Operators](https://docs.mongodb.com/manual/reference/operator/query/)
