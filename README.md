# Django Referral API Project

This project is a Django-based API for managing user registrations and referrals.

## Features

- User Registration Endpoint: Allows users to register with their name, email, and password. Optionally, users can provide a referral code.
- User Details Endpoint: Allows users to view their registration details after authentication.
- Referrals Endpoint: Allows authenticated users to view a list of users who registered using their referral code.

## Requirements

- Python 3.x
- Django
- Django Rest Framework\
  ## usage
Register a new user by sending a POST request to /register/ endpoint with the required parameters: name, email, and password.
Obtain an authentication token by sending a POST request to the appropriate endpoint (e.g., /api/token/).
Use the obtained token to access the authenticated endpoints such as /user-details/ and /referrals/.
View user details and referrals using the authenticated endpoints
