# pylint:disable=C0111,C0103

def get_average_purchase(db):
    # return the average amount spent per order for each customer ordered by customer ID

    query = """

    WITH OrderPrice AS (
        SELECT CustomerID, Orders.OrderID, SUM(UnitPrice * Quantity) AS Price
        FROM OrderDetails
        JOIN Orders ON
        Orders.OrderID  = OrderDetails.OrderID
        GROUP BY Orders.OrderID
    )
    SELECT CustomerID, ROUND(AVG(Price), 2) AS AverageOrderedAmount FROM OrderPrice
    GROUP BY CustomerID
    ORDER BY CustomerID;

    """

    db.execute(query)
    return db.fetchall()

def get_general_avg_order(db):
    # return the average amount spent per order
    query = """

    SELECT ROUND(AVG(Cost), 2) FROM(
	SELECT OrderID, SUM((UnitPrice * Quantity)) AS Cost
	FROM OrderDetails
	GROUP BY OrderID
    )

    """

    db.execute(query)
    return db.fetchall()[0][0]

def best_customers(db):
    # return the customers who have an average purchase greater than the general average purchase
    query = """

    WITH CustomerAverage AS(
    WITH OrderPrice AS (
    SELECT CustomerID, Orders.OrderID, SUM(UnitPrice * Quantity) AS Price
    FROM OrderDetails
    JOIN Orders ON
    Orders.OrderID  = OrderDetails.OrderID
    GROUP BY Orders.OrderID
    )
    SELECT CustomerID, ROUND(AVG(Price), 2) AS AverageOrderedAmount FROM OrderPrice
    GROUP BY CustomerID
    ORDER BY CustomerID
    )
    SELECT CustomerID, AverageOrderedAmount FROM CustomerAverage
    WHERE AverageOrderedAmount > (SELECT ROUND(AVG(Cost), 2) FROM(
    SELECT OrderID, SUM((UnitPrice * Quantity)) AS Cost
    FROM OrderDetails
    GROUP BY OrderID
    ))
    ORDER BY AverageOrderedAmount DESC

    """

    db.execute(query)
    return db.fetchall()


def top_ordered_product_per_customer(db):
    # return the list of the top ordered product by each customer based on the total ordered amount
    query = """

    WITH customerPurchase AS (
        SELECT Orders.CustomerID, OrderDetails.ProductID, SUM(OrderDetails.Quantity * OrderDetails.UnitPrice) AS purchaseVal
        FROM Orders
        JOIN OrderDetails ON
        OrderDetails.OrderID  = Orders.OrderID
        GROUP BY  Orders.CustomerID, OrderDetails.ProductID
        ORDER BY purchaseVal
        )
    SELECT CustomerID, ProductID, MAX(purchaseVal) AS OrderedAmount
    FROM customerPurchase
    GROUP BY CustomerID
    ORDER BY OrderedAmount DESC;

    """

    db.execute(query)
    return db.fetchall()


def average_number_of_days_between_orders(db):
    # return the average number of days between two consecutive orders of the same customer
    query = """

    WITH x AS(
    SELECT CustomerID, OrderDate, LAG(OrderDate) OVER(
        PARTITION BY CustomerID
        ORDER BY OrderDate
        ) AS offsetDate FROM Orders
    )
    SELECT ROUND(AVG((JULIANDAY(OrderDate) - JULIANDAY(offsetDate)))) AS daysBetween
    FROM x;

    """
    db.execute(query)
    return int(db.fetchall()[0][0])
