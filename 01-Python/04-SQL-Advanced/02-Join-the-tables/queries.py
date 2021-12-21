# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    query = """

    SELECT OrderID, ContactName, FirstName from Orders
    JOIN Customers ON
    Customers.CustomerID = Orders.CustomerID
    JOIN Employees ON
    Employees.EmployeeID = Orders.EmployeeID ;

    """

    db.execute(query)
    return db.fetchall()

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    query = """

    SELECT Customers.ContactName, x.cost FROM (
        SELECT Orders.CustomerID,
        ROUND(SUM(UnitPrice * Quantity), 2) AS cost
        FROM Orders
        JOIN Customers ON
        Customers.CustomerID = Orders.CustomerID
        JOIN OrderDetails ON
        OrderDetails.OrderID = Orders.OrderID
        GROUP BY Orders.CustomerID
        ORDER BY cost ASC
        ) AS x
    JOIN Customers ON
    Customers.CustomerID = x.CustomerID

    """

    db.execute(query)
    return db.fetchall()


def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''

    query = """

    SELECT FirstName, LastName, SUM(UnitPrice * Quantity) as sales
    FROM Employees
    JOIN Orders ON
    Employees.EmployeeID = Orders.EmployeeID
    JOIN OrderDetails ON
    OrderDetails.OrderID = Orders.OrderID
    GROUP BY Employees.EmployeeID
    ORDER BY sales DESC
    LIMIT 1

    """

    db.execute(query)
    return db.fetchall()[0]


def orders_per_customer(db):
    '''TO DO: return a list of tuples where each tupe contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''

    query = """

    SELECT ContactName, COUNT(DISTINCT(OrderID)) as number_of_orders
    FROM Customers
    LEFT JOIN Orders ON
    Orders.CustomerID = Customers.CustomerID
    GROUP BY ContactName
    ORDER BY number_of_orders ASC

    """
    db.execute(query)
    return db.fetchall()
