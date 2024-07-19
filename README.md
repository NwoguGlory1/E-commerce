# Project Name
"HairSynC" 

## Introduction

Welcome to HairSynC, a brand that links lovers of authentic luxury hairs and wigs directly to trusted Hair Companies.

## Live Site url
 https://hairsync.onrender.com/

## FinalProject Blog Article:

## Author's GitHub urls: 
https://github.com/NwoguGlory1/E-commerce


## Author's LinkedIn urls: 
https://www.linkedin.com/in/nwogu-glory-a2a95020b/

## Installation
To run this project locally, follow these steps:

Clone the repository:
git clone https://github.com/NwoguGlory1/E-commerce

Navigate to the project directory:
cd hairsync
Install dependencies:
pip install -r requirements.txt

Set up your Django environment variables (e.g., database credentials, secret key).

Apply migrations:
python manage.py migrate

Activate virtual environment:
source ~/.virtualenvs/yournamedjango/Scripts/activate

Run the development server:
python manage.py runserver

Access the website at http://localhost:8000/store

## Usage
Browse through the different categories of hair products available on the website.
Click on All Products to view its details and add it to your cart.
Navigate to a specific product page (Straight Hairs, Wavy Hairs, etc) and click Add To Cart button to add it to cart.
Click the cart logo on the nav bar to navigate to the Shopping Page, review your selected items and proceed to checkout.
Select a choice Hair Company on the Checkout page. 
Choose a  shipping and payment option to complete your purchase. 
Note: HairSynC website did not integrate delivery or shipping info but provides users the option to choose any shipping option available on the platform.

## Contributing
We welcome contributions from the community to improve HairSynC. If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/improvement).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/improvement).
Create a new Pull Request.

 ## Related Projects
 Hair.com.ng
 https://www.naijabeautyhair.com

## Licensing
Distributed under the MIT License. See `LICENSE` for more information.

## Screenshot url
https://imgur.com/a/obVzsup
https://imgur.com/a/g4J1d7j

## Inspiration and Purpose
HairSynC was inspired from  the needto provide a platform where lovers of quality luxury hair can always get  only authentic hairs directly from trusted hair companies, without having to haggle with the wholesalers who might at the end of the day not offer quality hairs/wigs to customers. 

## Technical Details
FrontEnd: HTML5, CSS3, JavaScript
FrontEnd Framework: Bootstrap 5
BackEnd: Python
BackEnd Framework: Django
APIs:  RESTful API with Flask & Python
Database: Djnago SQlite
Libraries: Django inbuilt libraries
Hardware: Digital Ocean, Vscode, Git Bash, Git & GitHub, Youtube, Chrome.

Due to the limited number of human hair types I used for the website, I assumed that the listed Hair Companies that a user can select from our platform will always provide all the hair types that a user selects from the product page.   
The most technical difficulty I experienced for the frontend would be getting the Cart functionality right. This required a good knowlege of JavaScript. I was able to make the backend to correctly fetch items users add to cart by clicking the Add to Cart button, but we struggled with the JavaScript that would cause the Cart counter on the nav bar to reflect this count. It is only when the user 

## Challenges and Solutions
One of the major challenges was implementing the Cart functionality. Initially, the backend could correctly fetch items added to the cart, but there were issues with updating the cart counter on the navbar dynamically. The solution involved using alerts to inform users of successful additions to the cart and requiring a page reload to reflect changes.

Other issues included:
- **Cart Counter:** The JavaScript function to update the cart counter dynamically was not working as expected.
- **Clear Cart Functionality:** The cart items were not clearing from the frontend without a page reload.
- **Total Amount and Quantity Calculation:** The JavaScript functions for calculating totals and updating the cart were challenging to implement.

Due to time constraints, some functionality was simplified, but ongoing work aims to improve these features.

## Future Work
- Fully implement dynamic cart updates without requiring page reloads.
- Enhance user interface and user experience.
- Expand product offerings and integrate more hair companies.
- Dynamically retrieve and render each product pages based on their ID. As at the time of compiling this README, I resorted to defining individual views for each product and using HTTP GET requests to retrieve them.
- Improving the layout of  the Checkout Page the more such that it can a lot more appealing.
Working on the Search functionality. It is not functional at this moment.
- Linking the bi bi-cart dash and bi bi-cart plus in the Shopping Cart page such that when a user clicks either of them, the change in Quantity will also be reflected in the Total Shopping cart quantity, Total Amount and the Total Quantity.
- Getting the cart icon on the nav bar to reflect the number of items in the cart. I was not able to achieve this but I plan on doing more researches on this.
- The Clear Cart button in the cart page is a bit faulty. A user has to refresh the page before the user can see that the items was successfully cleared.
- Getting django to retrieve each product page dynamically, that is based off on their unique id.
- Integrating some third party service in the website. Due to time constraints, no third party was integrated into the site. Eg: a payment platform such as  Flutterwave, Paystack, a Shipping company platform. Due to time constraint, I made these to be an option for the user to select.
- Writing test for each of the models that represents each feature in my  website. Time failed me too do this, sadly.
- Slow rendering of the site. The site that was used for this integration is free and so, loading the site on a  new device can be very slow but it will eventually render all pages.
- Implementing the update user profile feature. 
