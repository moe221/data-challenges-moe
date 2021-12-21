# pylint:disable=C0111,C0103

def order_rank_per_customer(db):
    query = """

    SELECT OrderID, CustomerID, OrderDate, RANK() OVER(
        PARTITION BY CustomerID
        ORDER BY OrderDate
        ) AS OrderRank
    FROM Orders

    """
    db.execute(query)
    return db.fetchall()

def order_cumulative_amount_per_customer(db):
    query = """

    SELECT Orders.OrderID,
    Orders.CustomerID,
    (Orders.OrderDate),
    SUM(SUM(UnitPrice * Quantity)) OVER(
        PARTITION BY CustomerID
        ORDER BY orders.OrderDate
        ) AS OrderCumulativeAmount
    FROM Orders
    JOIN OrderDetails ON
    OrderDetails.OrderID = Orders.OrderID
    GROUP BY Orders.OrderID
    ORDER BY Orders.CustomerID;


    """
    db.execute(query)
    return db.fetchall()
