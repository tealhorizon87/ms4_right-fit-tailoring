# Right Fit Tailoring

Right Fit Tailoring is a full service bespoke tailoring company that offers ready made men's fashion items and accessories as well as made to measure and alteration services. This application is their online store that customers can use to buy items, order made to measure and purchase alteration services. The deployed site can be viewed [here](https://tealhorizon-rf-tailoring.herokuapp.com/)

![mockup](docs/images/home-page-small.png)

## Table of Contents
1. [UX](#ux)
    - [User Stories](#user-stories)
    - [Design](#design)
    - [Wireframes](#wireframes)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits](#credits)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)

## UX

### User Stories
General User Stories:
  - As a user, I want to -
    - have a clear idea of what the site sells or does
    - easily navigate the site and any information within it
    - see the shopping cart total at all times
    - register for an account
  - As the site owner/administrator, I want to -
    - add new items to the site
    - edit and remove items that are already on the site
    - add discounts or deals to items or groups of items
    - view orders such that they can be easily fulfilled

Shopping Cart app user stories:
  - As a user, I want to -
  	- be able to easily add and remove items from the shopping cart
  	- see the shopping cart total at all times
  	- see a breakdown of costs for each item in the cart before the checkout
  	- see if there is an extra charge for delivery, and be told how to reduce it
  	- have the option to go back to the store if I'm not ready to checkout

Checkout add user stories:
  - As a user, I want to -
    - be confident that I can checkout securely
    - clearly see what will be charged before submitting the form
    - be able to save my details for future use if registered

Profile app user stories:
  - As a registered user, I want to -
    - save my delivery information for future use, and edit when necessary
    - save my measurements for future use, and edit when necessary
    - see my previous orders
    - be able to delete my account and all personal details if necessary

Wish list app user stories:
  - As a registered user, I want to -
    - be able to add and remove items to a wish list
    - be able to see what the total cost of the items in the wish list is
    - be able to add items to the shopping cart directly from the wish list

### Design
This application is an e-commerce store utilising the [Django](https://www.djangoproject.com/) framework for functionality, and [Stripe](https://stripe.com/) for payment processing. The site is useable by both registered and unregistered users, with certain features only available to registered users. Functionality for the site is broken into several apps:

#### Home
  - The home app contains functionality for the home page, namely rendering the home page to users when they enter the site.

#### Products
  - The products app contains functionality concerning the products and how they are displayed to the user.

#### Made to Measure
  - This app displays all material products so the user can choose one for their garment to be made from. It also contains the order form and order models associated with this function.

#### Profiles
  - The profiles app displays the user's profile page once they have registered, the saved delivery and measurement details, and a list of the previous orders of the user. This app also contains the function to delete the user's profile when they wish it.

#### Cart
  - The cart app concerns itself with displaying the shopping cart to the user and the functionality for adding and removing items to the cart.

#### Checkout
  - The checkout app contains the forms and models required to create an order, both to be displayed to the user and to the administrator, all the stripe functionality to process payment and systems to protect that function.

#### Wish list
  - The wish list app allows users to set up a wish list, add and remove items to said wish list, and display them back to the user.

<br>

The font families used for the application are Cinzel Decorative for the logo, Oswald for all headings, Josefin Sans for main body text, and Italianno for decorative text. All fonts have been sourced from [Google Fonts](https://fonts.google.com/).

The palette was generated by [coolors](https://coolors.co/) and are as follows:
![colour palette image](docs/images/right-fit-tailoring.png)

### Wireframes
Below are the wireframes used to design the layout. They were created using [Balsamiq](https://balsamiq.com/)
  - [Home page](docs/wireframes/1_home.png)
  - [Log in/Register](docs/wireframes/2_login_register.png)
  - [Profile](docs/wireframes/3_profile.png)
  - [All Products](docs/wireframes/4_all_products.png)
  - [Product Detail](docs/wireframes/12_product_detail.png)
  - [Shopping Cart](docs/wireframes/5_shopping_cart.png)
  - [Checkout](docs/wireframes/6_checkout.png)
  - [Made To Measure](docs/wireframes/7_made_to_measure.png)
  - [Made to Measure Form](docs/wireframes/8_mtm_form.png)
  - [Alterations](docs/wireframes/9_alterations.png)
  - [Wish List](docs/wireframes/10_wishlist.png)
  - [Contact](docs/wireframes/11_contact.png)

Back to [Table of Contents](#table-of-contents)

### Database
Below is the link to a tabulated view of how the data is stored in the database. The tables' columns have the displayed field name, the programmatic field name, the type of field that they are and any validation. All fields have validation of `null=False, blank=False` unless stated otherwise.

[database schema](docs/docs/database_schema.pdf)

## Features
- A page header containing all menus, search bar and shopping cart that is present on all pages for easy navigation
- Profile management with [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) for users to register, log in and log out to/from their profile
- A filtering system so that users can change the order that the product pages display the products
- Clicking on the image of a product will direct the user to that product's page where they can view more details and add it to their cart
- A checkbox to allow registered users to save their details at the checkout for future use
- A wish list ability to allow users to create lists of future purchases

### Future Features
- Similar to how the delivery details can be saved to the user's profile, a system to save measurement details for further use
- Sizing and measurement charts that the user can access to better determine what size they might need, and how to do their body measurements
- Log in functionality to include social media accounts
- Payment system to include PayPal and Apple Pay
- Add a product management section so that admin users can add and edit products from the live site rather than the django admin page

## Technologies Used
### Languages:
  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - This is the main mark-up language for the project
  - [CSS3](https://en.wikipedia.org/wiki/CSS)
    - Used for personalised styling over and above the Bootstrap styles
  - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - Used to animate and control aspects of the pages that move
  - [Python](https://www.python.org/)
    - Used to connect the frontend application to the backend database, and to control the navigation and publication of the application

### Libraries and Frameworks:
  - [Google Fonts](https://fonts.google.com/)
    - Used as the source for the font databases used in this site
  - [Font Awesome 5.15.3](https://fontawesome.com/)
    - Used as the source for the icons used
  - [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
    - The main CSS library used to style the pages and make it responsive
  - [Django](https://www.djangoproject.com/)
    - A full stack framework used facilitate the production of the application (see `requirements.txt` for a full list of dependencies)

### Tools:
  - [Atom](https://atom.io/) with [GitHub Desktop](https://desktop.github.com/)
    - Atom is my preferred text editor, linked with GitHub Desktop in order to push the code to GitHub
  - [Git](https://git-scm.com/)
    - Used for version control
  - [GitHub](https://github.com/)
    - Used to store the project files
  - [Balsamiq](https://balsamiq.com/)
    - A wireframe program used to create the mock-ups
  - [Coolors](https://coolors.co/)
    - An online tool to create colour palettes
  - [Stripe](https://stripe.com/gb)
    - The system used to process payments

Back to [Table of Contents](#table-of-contents)

## Testing

I have gathered all my testing data, and stored it in a separate file, which can be found [here](TESTING.md)

### Known Bugs

#### Name field in checkout doesn't pre-populate
The first and last name of the user is not gathered by the registration form, and only by the social media sign up form. As there is no social media sign up currently for this page, this means that the 'name' field in the checkout app will never be pre-filled. This issue should be rectified if a social media sign up system is added.

## Deployment
### Heroku
Deployment for this project is via [Heroku](https://www.heroku.com).
1. Create a requirements.txt file by typing `pip3 freeze --local > requirements.txt` in your repository terminal
2. Create a Procfile so that Heroku knows how to run the app, and write this line: `web: gunicorn right_fit_tailoring.wsgi:application`, making sure that there is no trailing whitespace
3. Make sure these files have been pushed to the GitHub repository and then navigate to [Heroku](https://www.heroku.com)
4. Log in and select 'new' in the top right, name your app and choose a region that is closest to you. The app name must be unique
5. On the dashboard for your app, select the 'Deploy' tab and under deployment method, select GitHub (the easiest option if your repository is in GitHub)
6. Enter the repository name underneath that and hit search. select the repository by clicking 'Connect'
7. You can either select Automatic or Manual deployment depending on your method. Remember that if you choose manual, then every time the main/master branch is changed, you will need to re-deploy the app
8. Go to the resources tab and add an instance of Heroku Postgres. You will need to add this to your django settings and migrate all the database info again
9. Next, go to the 'Settings' tab and select 'Reveal Config Vars'
10. Here you need to add several KEY: VALUE pairs for the app to run. They are
  - For database and django:
    - SECRET_KEY: *randomly generated secret key for example from https://miniwebtool.com/django-secret-key-generator/*
    - DATABASE_URL: *the Postgres url from the settings section in the Postgres resource*
  - For the AWS sections to work:
    - AWS_ACCESS_KEY_ID: *access key from AWS account*
    - AWS_SECRET_ACCESS_KEY: *this is found in the same location*
    - USE_AWS: True *this makes sure that the static files are taken from the AWS host*
  - For Stripe to work:
    - STRIPE_PUBLIC_KEY: *found in your stripe account*
    - STRIPE_SECRET_KEY: *found in your stripe account*
    - STRIPE_WH_SECRET: *found in the stripe webhooks section once an endpoint has been made*
  - For email sending to work:
    - EMAIL_HOST_USER: *the email address associated with the account use want to use to send emails*
    - EMAIL_HOST_PASS: *from your email provider*
11. Add the Heroku app URL to the `ALLOWED_HOSTS` list in the settings file
12. Once these KEY: VALUE pairs have been added, deploy the site manually to make sure the new config variables are loaded, and the site will be available from the 'Open app' button in the top right

### Forking the Repository
If you would like to view/change the code for the project then you can copy this repository to your GitHub account by forking it. You will then be able to do this without affecting the original repository:
1. From the repository home page,  click the 'fork' button (just below your picture with the dropdown menu)
2. You should now have a copy of the repository on your account

### Making a Local Clone
1. From the repository home page, select the 'code' tab (next to the green 'Gitpod' button)
2. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
3. Open Git Bash
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Type 'git clone', and then paste the URL you copied in Step 2.
6. Press Enter. Your local clone will be created.
7. Alternatively, you can use 'Open with GitHub Desktop' and follow the instructions, or just download the ZIP file containing the code files

Click [Here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository#cloning-a-repository-to-github-desktop) to view the GitHub documentation on deployment, or [Here](https://devcenter.heroku.com/)for the Heroku documentation for further help and advice.

Back to [Table of Contents](#table-of-contents)

## Credits

### Content
  - All code was written by myself or taken from the [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/), [Django](https://www.djangoproject.com/) or [Stripe](https://stripe.com/gb) documentation, with inspiration taken from the Code Institute walkthrough projects
  - In particular, the method for adding sizes to clothing items and setting up confirmation emails
  - The wishlist app was inspired by [VinylRack](https://github.com/peejaywk/VinylRack) and adapted for this project
  - The 'no-image' image was taken from [Free Icons PNG](https://www.freeiconspng.com/)
  - All the products with their images and descriptions were taken from [Suit Direct](https://www.suitdirect.co.uk/)
  - The main background image was sourced from [Pixabay](https://pixabay.com/)
  - The method and code for placing the footer correctly was taken from [freeCodeCamp](https://www.freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c/)

### Acknowledgements
  - Thanks to my mentor for help, guidance and support during this project as always
  - [Stack Overflow](https://stackoverflow.com/) - much like w3schools, an essential source of guidance...there is always someone who has had the same problem, and the answer is likely here
  - [Code Institute](https://codeinstitute.net/) - from inspiration through all the walkthrough projects to the tools needed to complete this project

Back to [Table of Contents](#table-of-contents)
