CUSTOMERS = [
  {
    "id": 1,
    "name": "Hannah Hall",
    "address": "7002 Chestnut Ct",
    "email": "hhall@gmail.com"
  },
  {
    "id": 2,
    "name": "Phillip Phan",
    "address": "123 Four St",
    "email": "phil@phil.phil"
  },
  {
    "id": 3,
    "name": "Lebron James",
    "address": "567 Yuh Way",
    "email": "kobe@yahoo.net"
  },
  {
    "email": "notphil@phil.phil",
    "name": "john smith",
    "address": "1 this way",
    "id": 4
  }
]

def get_all_customers():
  return CUSTOMERS

def get_single_customer(id):
  requested_customer = None

  for customer in CUSTOMERS:
    if customer["id"] == id:
      requested_customer = customer

  return requested_customer

def create_customer(customer):
  max_id = CUSTOMERS[-1]["id"]

  new_id = max_id + 1

  customer["id"] = new_id

  CUSTOMERS.append(customer)
  
  return customer

def delete_customer(id):
  customer_index = -1

  for index, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
      customer_index = index
  
  if customer_index >= 0:
    CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
  for index, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
      CUSTOMERS[index] = new_customer
      break