# APP'S TYPE
ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

# APP'S TYPE
APP_TYPE = (
    ('1', 'WEB'),
    ('2', 'API'),
)

# CARDS TYPES
CARD_TYPE = (
    (1, 'Visa'),
    (2, 'Mastercard'),
    (3, 'Maestro'),
    (4, 'American Express'),
    (5, 'Dinner Club'),
)

# CATEGORY CHOICES
CATEGORY_CHOICES = (
    ('Cap',         'Cap'),
    ('Men',         'Men Wear'),
    ('Outwear',     'Outwear'),
    ('Shirt',       'Shirt'),
    ('Sportwear',   'Sport Wear'),
    ('Women',       'Women Wear'),
)

# CURRENCIES
CURRENCIES = (
    ('CDF', 'CDF'),
    ('EUR', 'EUR'),
    ('USD', 'USD'),
    ('GBP', 'GBP'),
    ('ZAR', 'ZAR'),
)

# ISSUES TYPES
ISSUE_TYPE = (
      (1, 'Bug'),               # Bug
      (2, 'Enhancement'),       # Enhancement
  )

# LABELS CHOICES
LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

# LANGUAGES
LANGUAGES = (
    ('EN', 'English'),
    ('FR', 'French'),
    ('DE', 'German'),
    ('PT', 'Portuguese'),
    ('ES', 'Spanish'),
)

# MOBILE MONEY'S TYPE
MOBILE_MONEY_TYPE = (
    (1, 'M-pesa'),
    (2, 'Orange Money'),
    (3, 'Airtel Money'),
    (4, 'Afri Money'),
)

# ORDER TYPE
ORDER_TYPE = (
    ('D', 'Delivery'),
    ('S', 'Shipment'),
    ('P', 'Pick up'),
)

# PAYMENT TYPES
PAYMENT_TYPE = (
    (1, 'Mobile Money'),
    (2, 'Credit Card'),
    (3, 'Debit Card'),
    (4, 'Bank Transfer'),
    (5, 'Paypal'),
    (6, 'Skrill'),
)

# REFUND STATUS
REFUND_STATUS = (
    (1, 'Processed'),
    (2, 'Cancelled'),
    (3, 'Completed'),
)

# STATUS TYPES
STATUS_TYPE = (
      (1, 'Assigned'),          # Assigned
      (2, 'Resolved'),          # Resolved
      (3, 'Closed'),            # Closed
  )

# USER TYPES
USER_TYPE = (
      (1, 'BTK Systems'),       # BTK Systems
      (2, 'SR Staff'),          # SR Staff
      (3, 'Customer'),          # Customer
  )

# USER LEVEL TYPES
USER_LEVEL = (
    (1,1),      # View & Popular for All
    (2,2),
    (3,3),      # View Most but Edit limited
    (4,4),
    (5,5)       # All Access
)

# WEEKDAYS
WEEKDAYS = (
    (0, 'Sunday'),
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
)