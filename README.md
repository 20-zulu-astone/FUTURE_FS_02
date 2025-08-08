# FUTURE_FS_02
A mini ecommerce platform website .
MiniStore is a simple e-commerce web application built with Django. It features a shopping cart, order checkout, and a payment simulation system to mimic the payment process during development.

## Features

- Add products to a session-based shopping cart
- Place orders using a checkout form
- Simulate payments by selecting payment methods (Cash, Bank Transfer, Mobile Money)
- Bootstrap integration for a clean and responsive UI
- Manage cart and orders without user authentication (session-based)

## Installation

Follow these steps to set up the project locally:

```bash
git clone https://github.com/20-zulu-astone/FUTURE_FS_02
cd ministore
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Usage
Open your browser and visit http://127.0.0.1:8000/

Browse products and add them to your cart

Go to the cart and proceed to checkout

Fill out the order form and select a payment method

Submit the form to simulate a successful payment

You will be redirected to a success page confirming your order

Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

License
All rights reserved

Contact
Astone Zulu - zuluastone80@gmail.com