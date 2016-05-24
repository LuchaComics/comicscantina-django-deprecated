# Custom Constants
#
EMPLOYEE_OWNER_ROLE = 0
EMPLOYEE_MANAGER_ROLE = 1
EMPLOYEE_WORKER_ROLE = 2

# Product Types
COMIC_PRODUCT_TYPE = 1
FURNITURE_PRODUCT_TYPE = 2
COIN_PRODUCT_TYPE = 3
GENERAL_PRODUCT_TYPE = 4

# Receipt Error Codes
NO_ERROR_TYPE = 0
CANCELLED_ONLINE_ORDER_ERROR_TYPE = 1
SHIPPING_RATE_ERROR_TYPE = 2

# Receipt Status Types
NEW_ORDER_STATUS = 1
PICKED_STATUS = 2
SHIPPED_STATUS = 3
RECEIVED_STATUS = 4
IN_STORE_SALE_STATUS = 5
ONLINE_SALE_STATUS = 6

# Receipt Payment Method Types
CASH_PAYMENT_METHOD = 1
DEBIT_CARD_PAYMENT_METHOD = 2
CREDIT_CARD_PAYMENT_METHOD = 3
GIFT_CARD_PAYMENT_METHOD = 4
STORE_POINTS_PAYMENT_METHOD = 5
CHEQUE_PAYMENT_METHOD = 6
PAYPAL_PAYMENT_METHOD = 7
INVOICE_PAYMENT_METHOD = 8
OTHER_PAYMENT_METHOD = 9


#-----------#
# DROPDOWNS #
#-----------#


ROLE_CHOICES = (
    (EMPLOYEE_OWNER_ROLE, 'Owner'),
    (EMPLOYEE_MANAGER_ROLE, 'Manager'),
    (EMPLOYEE_WORKER_ROLE, 'Worker'),
)


PRODUCT_TYPE_OPTIONS = (
    (COMIC_PRODUCT_TYPE, 'Comic'),
    (FURNITURE_PRODUCT_TYPE, 'Furniture'),
    (COIN_PRODUCT_TYPE, 'Coin'),
    #(settings.GENERAL_PRODUCT_TYPE, 'General'),
)


RECEIPT_ERROR_CHOICES = (
    (NO_ERROR_TYPE, 'No Error'),
    (CANCELLED_ONLINE_ORDER_ERROR_TYPE, 'Cancelled Online Order'),
)


PAYMENT_METHOD_CHOICES = (
    (CASH_PAYMENT_METHOD, 'Cash'),
    (DEBIT_CARD_PAYMENT_METHOD, 'Debit Card'),
    (CREDIT_CARD_PAYMENT_METHOD, 'Credit Card'),
    (GIFT_CARD_PAYMENT_METHOD, 'Gift Card'),
    (STORE_POINTS_PAYMENT_METHOD, 'Store Points'),
    (CHEQUE_PAYMENT_METHOD, 'Cheque'),
    (PAYPAL_PAYMENT_METHOD, 'PayPal'),
    (INVOICE_PAYMENT_METHOD, 'Invoice'),
    (OTHER_PAYMENT_METHOD, 'Other'),
)


STATUS_CHOICES = (
    (NEW_ORDER_STATUS, 'New Order'),
    (PICKED_STATUS, 'Picked'),
    (SHIPPED_STATUS, 'Shipped'),
    (RECEIVED_STATUS, 'Received'),
    (IN_STORE_SALE_STATUS, 'In-Store Sale'),
    (ONLINE_SALE_STATUS, 'Online Sale'),
)


PRODUCT_DISCOUNT_TYPE_OPTIONS = (
    (1, '%'),
    (2, '$'),
)


# Note: https://en.wikipedia.org/wiki/ISO_4217
ISO_4217_CURRENCY_OPTIONS = (
    (124, 'CAD'),
    (840, 'USD'),
    (484, 'MXN'),
)


# Note: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
ISO_639_1_LANGUAGE_OPTIONS = (
    ('EN', 'English'),
)


# https://en.wikipedia.org/wiki/ISO_3166-1_numeric#Officially_assigned_code_elements
ISO_3166_1_NUMERIC_COUNTRY_CHOICES = (
    (124, 'Canada'),
    (840, 'United States'),
    (484, 'Mexico'),
)


STORE_HOUR_OPTIONS = (
    ('08:00', '08:00'),
    ('08:30', '08:30'),
    ('09:00', '09:00'),
    ('09:30', '09:30'),
    ('10:00', '10:00'),
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'),
    ('22:00', '22:00'),
    ('22:30', '22:30'),
)


CGC_RATING_OPTIONS = (
    (10.0, '10.0 Gem Mint'),
    (9.9, '9.9 Mint'),
    (9.8, '9.8 Near Mint/Mint'),
    (9.6, '9.6 Near Mint +'),
    (9.4, '9.4 Near Mint'),
    (9.2, '9.2 Near Mint -'),
    (9.0, '9.0 Very Fine/Near Mint'),
    (8.5, '8.5 Very Fine +'),
    (8.0, '8.0 Very Fine'),
    (7.5, '7.5 Very Fine -'),
    (7.0, '7.0 Fine/Very Fine'),
    (6.5, '6.5 Fine +'),
    (6.0, '6.0 Fine'),
    (5.5, '5.5 Fine -'),
    (5.0, '5.0 Very Good/Fine'),
    (4.5, '4.5 Very Good +'),
    (4.0, '4.0 Very Good'),
    (3.5, '3.5 Very Good -'),
    (3.0, '3.0 Good/Very Good'),
    (2.5, '2.5 Good +'),
    (2.0, '2.0 Good'),
    (1.8, '1.8 Good -'),
    (1.5, '1.5 Fair/Good'),
    (1.0, '1.0 Fair'),
    (.5, '.5 Poor'),
    (0, 'NG'),
)


LABEL_COLOUR_OPTIONS = (
    ('Yellow', 'CGC Yellow Label'),
    ('Blue', 'CGC Blue Label'),
    ('Purple', 'CGC Purple Label'),
    ('Red', 'CGC Red Label'),
    ('cbcs', 'CBCS'),
    ('pgx', 'PGX'),
)


CONDITION_RATING_RATING_OPTIONS = (
    (10, 'Near Mint'),
    (8, 'Very Fine'),
    (6, 'Fine'),
    (4, 'Very Good'),
    (2, 'Good'),
    (1, 'Fair'),
    (0, 'Poor'),
)


AGE_OPTIONS = (
    (1, 'Gold'),
    (2, 'Silver'),
    (3, 'Bronze'),
    (4, 'Copper'),
)


HELP_REQUEST_SUBJECT_CHOICES = (
    (1, 'Feedback'),
    (2, 'Error'),
    (3, 'Checkout'),
    (4, 'Inventory'),
    (5, 'Pull List'),
    (6, 'Sales'),
    (7, 'Emailing List'),
    (8, 'Store Settings / Users'),
    (9, 'Dashboard'),
)


PROVINCE_CHOICES = (
    ('Alberta', 'Alberta'),
    ('British Columbia', 'British Columbia'),
    ('Manitoba', 'Manitoba'),
    ('New Brunswick', 'New Brunswick'),
    ('Newfoundland and Labrador', 'Newfoundland and Labrador'),
    ('Nova Scotia', 'Nova Scotia'),
    ('Ontario', 'Ontario'),
    ('Prince Edward Island', 'Prince Edward Island'),
    ('Quebec', 'Quebec'),
    ('Saskatchewan', 'Saskatchewan'),
    ('Northwest Territories', 'Northwest Territories'),
    ('Nunavut', 'Nunavut'),
    ('Yukon', 'Yukon'),
    ('Alabama', 'Alabama'),
    ('Alaska', 'Alaska'),
    ('Arizona', 'Arizona'),
    ('Arkansas', 'Arkansas'),
    ('California', 'California'),
    ('Colorado', 'Colorado'),
    ('Connecticut', 'Connecticut'),
    ('Delaware', 'Delaware'),
    ('Florida', 'Florida'),
    ('Georgia', 'Georgia'),
    ('Hawaii', 'Hawaii'),
    ('Idaho', 'Idaho'),
    ('Illinois', 'Illinois'),
    ('Indiana', 'Indiana'),
    ('Iowa', 'Iowa'),
    ('Kansas', 'Kansas'),
    ('Kentucky', 'Kentucky'),
    ('Louisiana', 'Louisiana'),
    ('Maine', 'Maine'),
    ('Maryland', 'Maryland'),
    ('Massachusetts', 'Massachusetts'),
    ('Michigan', 'Michigan'),
    ('Minnesota', 'Minnesota'),
    ('Mississippi', 'Mississippi'),
    ('Missouri', 'Missouri'),
    ('Montana', 'Montana'),
    ('Nebraska', 'Nebraska'),
    ('Nevada', 'Nevada'),
    ('New Hampshire', 'New Hampshire'),
    ('New Jersey', 'New Jersey'),
    ('New Mexico', 'New Mexico'),
    ('New York', 'New York'),
    ('North Carolina', 'North Carolina'),
    ('North Dakota', 'North Dakota'),
    ('Ohio', 'Ohio'),
    ('Oklahoma', 'Oklahoma'),
    ('Oregon', 'Oregon'),
    ('Pennsylvania', 'Pennsylvania'),
    ('Rhode Island', 'Rhode Island'),
    ('South Carolina', 'South Carolina'),
    ('South Dakota', 'South Dakota'),
    ('Tennessee', 'Tennessee'),
    ('Texas', 'Texas'),
    ('Utah', 'Utah'),
    ('Vermont', 'Vermont'),
    ('Virginia', 'Virginia'),
    ('Washington', 'Washington'),
    ('West Virginia', 'West Virginia'),
    ('Wisconsin', 'Wisconsin'),
    ('Wyoming', 'Wyoming'),
    ('Other', 'Other'),
)

COUNTRY_CHOICES = (
    ('Canada', 'Canada'),
    ('United States', 'United States'),
    ('Mexico', 'Mexico'),
    ('Afghanistan', 'Afghanistan'),
    ('Albania', 'Albania'),
    ('Algeria', 'Algeria'),
    ('Andorra', 'Andorra'),
    ('Angola', 'Angola'),
    ('Antigua and Barbuda', 'Antigua and Barbuda'),
    ('Argentina', 'Argentina'),
    ('Armenia', 'Armenia'),
    ('Aruba', 'Aruba'),
    ('Australia', 'Australia'),
    ('Austria', 'Austria'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Bahamas, The', 'Bahamas, The'),
    ('Bahrain', 'Bahrain'),
    ('Bangladesh', 'Bangladesh'),
    ('Barbados', 'Barbados'),
    ('Belarus', 'Belarus'),
    ('Belgium', 'Belgium'),
    ('Belize', 'Belize'),
    ('Benin', 'Benin'),
    ('Bhutan', 'Bhutan'),
    ('Bolivia', 'Bolivia'),
    ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
    ('Botswana', 'Botswana'),
    ('Brazil', 'Brazil'),
    ('Brunei', 'Brunei'),
    ('Bulgaria', 'Bulgaria'),
    ('Burkina Faso', 'Burkina Faso'),
    ('Burma', 'Burma'),
    ('Burundi', 'Burundi'),
    ('Cambodia', 'Cambodia'),
    ('Cameroon', 'Cameroon'),
    ('Cape Verde', 'Cape Verde'),
    ('Central African Republic', 'Central African Republic'),
    ('Chad', 'Chad'),
    ('Chile', 'Chile'),
    ('China', 'China'),
    ('Colombia', 'Colombia'),
    ('Comoros', 'Comoros'),
    ('Congo, Democratic Republic of the', 'Congo, Democratic Republic of the'),
    ('Congo, Republic of the', 'Congo, Republic of the'),
    ('Costa Rica', 'Costa Rica'),
    ('Cote d\'Ivoire', 'Cote d\'Ivoire'),
    ('Croatia', 'Croatia'),
    ('Cuba', 'Cuba'),
    ('Curacao', 'Curacao'),
    ('Cyprus', 'Cyprus'),
    ('Czech Republic', 'Czech Republic'),
    ('Denmark', 'Denmark'),
    ('Djibouti', 'Djibouti'),
    ('Dominica', 'Dominica'),
    ('Dominican Republic', 'Dominican Republic'),
    ('East Timor', 'East Timor'),
    ('Ecuador', 'Ecuador'),
    ('Egypt', 'Egypt'),
    ('El Salvador', 'El Salvador'),
    ('Equatorial Guinea', 'Equatorial Guinea'),
    ('Eritrea', 'Eritrea'),
    ('Estonia', 'Estonia'),
    ('Ethiopia', 'Ethiopia'),
    ('Fiji', 'Fiji'),
    ('Finland', 'Finland'),
    ('France', 'France'),
    ('Gabon', 'Gabon'),
    ('Gambia, The', 'Gambia, The'),
    ('Georgia', 'Georgia'),
    ('Germany', 'Germany'),
    ('Ghana', 'Ghana'),
    ('Greece', 'Greece'),
    ('Grenada', 'Grenada'),
    ('Guatemala', 'Guatemala'),
    ('Guinea', 'Guinea'),
    ('Guinea-Bissau', 'Guinea-Bissau'),
    ('Guyana', 'Guyana'),
    ('Haiti', 'Haiti'),
    ('Holy See', 'Holy See'),
    ('Honduras', 'Honduras'),
    ('Hong Kong', 'Hong Kong'),
    ('Hungary', 'Hungary'),
    ('Iceland', 'Iceland'),
    ('India', 'India'),
    ('Indonesia', 'Indonesia'),
    ('Iran', 'Iran'),
    ('Iraq', 'Iraq'),
    ('Ireland', 'Ireland'),
    ('Israel', 'Israel'),
    ('Italy', 'Italy'),
    ('Jamaica', 'Jamaica'),
    ('Japan', 'Japan'),
    ('Jordan', 'Jordan'),
    ('Kazakhstan', 'Kazakhstan'),
    ('Kenya', 'Kenya'),
    ('Kiribati', 'Kiribati'),
    ('Korea, North', 'Korea, North'),
    ('Korea, South', 'Korea, South'),
    ('Kosovo', 'Kosovo'),
    ('Kuwait', 'Kuwait'),
    ('Kyrgyzstan', 'Kyrgyzstan'),
    ('Laos', 'Laos'),
    ('Latvia', 'Latvia'),
    ('Lebanon', 'Lebanon'),
    ('Lesotho', 'Lesotho'),
    ('Liberia', 'Liberia'),
    ('Libya', 'Libya'),
    ('Liechtenstein', 'Liechtenstein'),
    ('Lithuania', 'Lithuania'),
    ('Luxembourg', 'Luxembourg'),
    ('Macau', 'Macau'),
    ('Macedonia', 'Macedonia'),
    ('Madagascar', 'Madagascar'),
    ('Malawi', 'Malawi'),
    ('Malaysia', 'Malaysia'),
    ('Maldives', 'Maldives'),
    ('Mali', 'Mali'),
    ('Malta', 'Malta'),
    ('Marshall Islands', 'Marshall Islands'),
    ('Mauritania', 'Mauritania'),
    ('Mauritius', 'Mauritius'),
    ('Mexico', 'Mexico'),
    ('Micronesia', 'Micronesia'),
    ('Moldova', 'Moldova'),
    ('Monaco', 'Monaco'),
    ('Mongolia', 'Mongolia'),
    ('Montenegro', 'Montenegro'),
    ('Morocco', 'Morocco'),
    ('Mozambique', 'Mozambique'),
    ('Namibia', 'Namibia'),
    ('Nauru', 'Nauru'),
    ('Nepal', 'Nepal'),
    ('Netherlands', 'Netherlands'),
    ('Netherlands Antilles', 'Netherlands Antilles'),
    ('New Zealand', 'New Zealand'),
    ('Nicaragua', 'Nicaragua'),
    ('Niger', 'Niger'),
    ('Nigeria', 'Nigeria'),
    ('North Korea', 'North Korea'),
    ('Norway', 'Norway'),
    ('Oman', 'Oman'),
    ('Pakistan', 'Pakistan'),
    ('Palau', 'Palau'),
    ('Palestinian Territories', 'Palestinian Territories'),
    ('Panama', 'Panama'),
    ('Papua New Guinea', 'Papua New Guinea'),
    ('Paraguay', 'Paraguay'),
    ('Peru', 'Peru'),
    ('Philippines', 'Philippines'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Qatar', 'Qatar'),
    ('Romania', 'Romania'),
    ('Russia', 'Russia'),
    ('Rwanda', 'Rwanda'),
    ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
    ('Saint Lucia', 'Saint Lucia'),
    ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
    ('Samoa', 'Samoa'),
    ('San Marino', 'San Marino'),
    ('Sao Tome and Principe', 'Sao Tome and Principe'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Senegal', 'Senegal'),
    ('Serbia', 'Serbia'),
    ('Seychelles', 'Seychelles'),
    ('Sierra Leone', 'Sierra Leone'),
    ('Singapore', 'Singapore'),
    ('Sint Maarten', 'Sint Maarten'),
    ('Slovakia', 'Slovakia'),
    ('Slovenia', 'Slovenia'),
    ('Solomon Islands', 'Solomon Islands'),
    ('Somalia', 'Somalia'),
    ('South Africa', 'South Africa'),
    ('South Korea', 'South Korea'),
    ('South Sudan', 'South Sudan'),
    ('Spain', 'Spain'),
    ('Sri Lanka', 'Sri Lanka'),
    ('Sudan', 'Sudan'),
    ('Suriname', 'Suriname'),
    ('Swaziland', 'Swaziland'),
    ('Sweden', 'Sweden'),
    ('Switzerland', 'Switzerland'),
    ('Syria', 'Syria'),
    ('Taiwan', 'Taiwan'),
    ('Tajikistan', 'Tajikistan'),
    ('Tanzania', 'Tanzania'),
    ('Thailand', 'Thailand'),
    ('Timor-Leste', 'Timor-Leste'),
    ('Togo', 'Togo'),
    ('Tonga', 'Tonga'),
    ('Trinidad and Tobago', 'Trinidad and Tobago'),
    ('Tunisia', 'Tunisia'),
    ('Turkey', 'Turkey'),
    ('Turkmenistan', 'Turkmenistan'),
    ('Tuvalu', 'Tuvalu'),
    ('Uganda', 'Uganda'),
    ('Ukraine', 'Ukraine'),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('United Kingdom', 'United Kingdom'),
    ('Uruguay', 'Uruguay'),
    ('Uzbekistan', 'Uzbekistan'),
    ('Vanuatu', 'Vanuatu'),
    ('Venezuela', 'Venezuela'),
    ('Vietnam', 'Vietnam'),
    ('Yemen', 'Yemen'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe', 'Zimbabwe'),
    ('Other', 'Other'),
)

DOB_DAYS_OPTIONS = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
    (13, '13'),
    (14, '14'),
    (15, '15'),
    (16, '16'),
    (17, '17'),
    (18, '18'),
    (19, '19'),
    (20, '20'),
    (21, '21'),
    (22, '22'),
    (23, '23'),
    (24, '24'),
    (25, '25'),
    (26, '26'),
    (27, '27'),
    (28, '28'),
    (29, '29'),
    (30, '30'),
    (31, '31'),
)

DOB_MONTH_OPTIONS = (
    (1, 'January'), # 31 days
    (2, 'February'), # 28 days, 29 in leap years
    (3, 'March'), # 31 days
    (4, 'April'), # 30 days
    (5, 'May'), # 31 days
    (6, 'June'), # 30 days
    (7, 'July'), # 31 days
    (8, 'August'), # 31 days
    (9, 'September'), # 30 days
    (10, 'October'), # 31 days
    (11, 'November'), # 30 days
    (12, 'December'), # 31 days
)

DOB_YEAR_OPTIONS = (
    (1900, '1900'),
    (1901, '1901'),
    (1902, '1902'),
    (1903, '1903'),
    (1904, '1904'),
    (1905, '1905'),
    (1906, '1906'),
    (1907, '1907'),
    (1908, '1908'),
    (1909, '1909'),
    (1910, '1910'),
    (1911, '1911'),
    (1912, '1912'),
    (1913, '1913'),
    (1914, '1914'),
    (1915, '1915'),
    (1916, '1916'),
    (1917, '1917'),
    (1918, '1918'),
    (1919, '1919'),
    (1920, '1920'),
    (1921, '1921'),
    (1922, '1922'),
    (1923, '1923'),
    (1924, '1924'),
    (1925, '1925'),
    (1926, '1926'),
    (1927, '1927'),
    (1928, '1928'),
    (1929, '1929'),
    (1930, '1930'),
    (1931, '1931'),
    (1932, '1932'),
    (1933, '1933'),
    (1934, '1934'),
    (1935, '1935'),
    (1936, '1936'),
    (1937, '1937'),
    (1938, '1938'),
    (1939, '1939'),
    (1940, '1940'),
    (1941, '1941'),
    (1942, '1942'),
    (1943, '1943'),
    (1944, '1944'),
    (1945, '1945'),
    (1946, '1946'),
    (1947, '1947'),
    (1948, '1948'),
    (1949, '1949'),
    (1950, '1950'),
    (1951, '1951'),
    (1952, '1952'),
    (1953, '1953'),
    (1954, '1954'),
    (1955, '1955'),
    (1956, '1956'),
    (1957, '1957'),
    (1958, '1958'),
    (1959, '1959'),
    (1960, '1960'),
    (1961, '1961'),
    (1962, '1962'),
    (1963, '1963'),
    (1964, '1964'),
    (1965, '1965'),
    (1966, '1966'),
    (1967, '1967'),
    (1968, '1968'),
    (1969, '1969'),
    (1970, '1970'),
    (1971, '1971'),
    (1972, '1972'),
    (1973, '1973'),
    (1974, '1974'),
    (1975, '1975'),
    (1976, '1976'),
    (1977, '1977'),
    (1978, '1978'),
    (1979, '1979'),
    (1980, '1980'),
    (1981, '1981'),
    (1982, '1982'),
    (1983, '1983'),
    (1984, '1984'),
    (1985, '1985'),
    (1986, '1986'),
    (1987, '1987'),
    (1988, '1988'),
    (1989, '1989'),
    (1990, '1990'),
    (1991, '1991'),
    (1992, '1992'),
    (1993, '1993'),
    (1994, '1994'),
    (1995, '1995'),
    (1996, '1996'),
    (1997, '1997'),
    (1998, '1998'),
    (1999, '1999'),
    (2000, '2000'),
)

TSHOP_THEME_OPTIONS = (
    ('ecantina-style-0.css', 'Green'),
    ('ecantina-style-1.css', 'Ligh Green'),
    ('ecantina-style-2.css', 'Aqua Green'),
    ('ecantina-style-3.css', 'Blue'),
    ('ecantina-style-4.css', 'Purple'),
    ('ecantina-style-5.css', 'Red'),
    ('ecantina-style-6.css', 'Dark Grey'),
    ('ecantina-style-7.css', 'Grey'),
    ('ecantina-style-8.css', 'Light Aqua Green'),
    ('ecantina-style-9.css', 'Yellow'),
    ('ecantina-style-10.css', 'Light Red'),
    ('ecantina-style-11.css', 'Dark Blue'),
    ('ecantina-style-black.css', 'Black'),
)