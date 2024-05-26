# Readers Realm

------------
[Link to live site here](https://cricket-gear-hub-f9339f25dfca.herokuapp.com/  "Link to live site here")

![Am I responsive image](./readme_media/design_images/am_i_responsive.png)

## Table of Contents

- [Readers Realm](#readers-realm)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [User Experience (UX)](#user-experience-ux)
    - [User Stories (US)](#user-stories-us)
    - [Design](#design)
      - [**Colour**](#colour)
      - [typography](#typography)
      - [Structure](#structure)
      - [Imagery](#imagery)
      - [Wireframes](#wireframes)
    - [Accessability](#accessability)
    - [Database schema](#database-schema)
      - [Final data schema](#final-data-schema)
    - [CRUD](#crud)
      - [Step 1 Create](#step-1-create)
      - [Step 2 Read](#step-2-read)
      - [Step 3 Update](#step-3-update)
      - [Step 4 Delete](#step-4-delete)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
  - [Testing](#testing)
    - [Bugs](#bugs)
  - [Deployment \& Local Development](#deployment--local-development)
    - [Deployment](#deployment)
    - [Local Development](#local-development)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
  - [Credits](#credits)
    - [Images used](#images-used)
    - [Code Used](#code-used)
    - [Content](#content)
    - [media](#media)
    - [Acknowledgments](#acknowledgments)

## Introduction

I have created a simple online book review web app, it will allow users to be able to register to the website, so they can utilize everything the website has to offer. Users that are'nt registered will still be able to view all the books on show, and be able to view reviews that may have been left by other users.
If a user want's to be able to add a book to display on the website they must be registered and logged in, and if users want to leave reviews on any books on the website, they must also be registered and logged in. Registered users will also have their own profile page, which will allow them to view all the reviews and books they have added, users will also be able to edit and delete the reviews and books they've added.

## User Experience (UX)

### User Stories (US)

- **First time visitor goals**
    1. As a first time visitor I want to be able to easily browse products.
    2. As a first time visitor I want to be able checkout being only a guest.
    3. As a first time visitor I want a website to visually attractive and provide good user experience.
    4. As a first time visitor I want to view individual products.
    5. As a first time visitor I want to be able to search for products manually, rather than scrolling through the website.

  - **Returning Visitor goals**
    1. As a returning Visitor I want to be able to create an account.
    2. As a returning Visitor I want a profile section on where I can view previous orders.
    3. As a returning Visitor I want to be able to add/edit my current address.
    4. As a returning visitor I want to be able to reset my password Incase I forget it.
   
  - **Frequent visitor goals**
    1. As a frequent visitor, I want the e-commerce site to be mobile-friendly, so I can shop easily from my smartphone or tablet.
    2. As a frequent visitor, I want to leave reviews for products I have purchased, so I can share my experience with other customers.
    3. As a frequent visitor, I want to read reviews from other users, so I can make informed purchasing decisions.
    4. As a frequent visitor, I want my shopping cart to be saved across sessions, so I don't lose my selected items if I leave the site.
  

### Design

#### **Colour**
![Colour Pallette](./readme_media/design_images/palette.png)

#### typography
I have used the following for the majority of the text font-family: 'EB Garamond', serif;
So I've used EB garamond from google font's and with the backup of serif incase that fails/

And for the headings of the website I have used the playfair-display font again used from google fonts.

#### Structure

When users land on the website they will be taken to the home page where all users are free to browse, users can access all of the websites pages (apart from the site owners pages for crud implementation e.g adding products / staff members etc).
From the home page users can access and view all the products the site has to offer, they can also view the current staff team, and they can also contact the team via email.

On the top right of the home page users can access their profile page, contacting the team and view their carts.
and below this are the links for all of the products on the site which are spilt into different categories, and then withing each category users can either view them in price order, rating order, or just view each type of category of product, there is also a link for all products where users can view every product on the page.

Users can then click on the images of products to view the individual product itself where users can then view descriptions, reviews and if they wanted to add the item to the cart from here.

Users have to be logged in to be able to leave a review.

Once users have added products to their cart and ready to pay for their products they can then click on their cart, and they will then see a button to click to proceed to checkout, which they can then fill out the relevant details and proceed to payment, after successful payment is made users will then be taken to a checkout success page thank them for their purchase and provides details of the order they placed, and gives uers the option to easily return back to the home page where nessacary.


  
#### Imagery

#### Wireframes

<details>
<summary>Home Page</summary>

<details>
<summary>Desktop</summary>

![Desktop Image](./readme_media/wireframes/home-desktop.png)

</details>

<details>
<summary>Tablet</summary>

![Tablet Image](./readme_media/wireframes/home-tablet.png)

</details>

<details>
<summary>Mobile</summary>

![Mobile Image](./readme_media/wireframes/home-mobile.png)

</details>

</details>

<details>
<summary>Cart Page</summary>

<details>
<summary>Desktop</summary>

![Desktop Image](./readme_media/wireframes/cart-desktop.png)

</details>

<details>
<summary>Tablet</summary>

![Tablet Image](./readme_media/wireframes/cart-tablet.png)

</details>

<details>
<summary>Mobile</summary>

![Mobile Image](./readme_media/wireframes/cart-mobile.png)

</details>

</details>

<details>
<summary>Checkout Page</summary>

<details>
<summary>Desktop</summary>

![Desktop Image](./readme_media/wireframes/checkout-desktop.png)

</details>

<details>
<summary>Tablet</summary>

![Tablet Image](./readme_media/wireframes/checkout-tablet.png)

</details>

<details>
<summary>Mobile</summary>

![Mobile Image](./readme_media/wireframes/checkout-mobile.png)

</details>

</details>

<details>
<summary>Individual Products Page</summary>

<details>
<summary>Desktop</summary>

![Desktop Image](./readme_media/wireframes/individual-products-desktop.png)

</details>

<details>
<summary>Tablet</summary>

![Tablet Image](./readme_media/wireframes/individual-products-tablet.png)

</details>

<details>
<summary>Mobile</summary>

![Mobile Image](./readme_media/wireframes/individual-products-mobile.png)

</details>

</details>

<details>
<summary>Login Page</summary>

<details>
<summary>Desktop</summary>

![Desktop Image](./readme_media/wireframes/login-desktop.png)

</details>

<details>
<summary>Tablet</summary>

![Tablet Image](./readme_media/wireframes/login-tablet.png)

</details>

<details>
<summary>Mobile</summary>

![Mobile Image](./readme_media/wireframes/login-mobile.png)

</details>

</details>

<details>
<summary>Products Page</summary>

<details>
<summary>Desktop</summary>

![Desktop Image](./readme_media/wireframes/products-desktop.png)

</details>

<details>
<summary>Tablet</summary>

![Tablet Image](./readme_media/wireframes/products-tablet.png)

</details>

<details>
<summary>Mobile</summary>

![Mobile Image](./readme_media/wireframes/products-mobile.png)

</details>

</details>

<details>
<summary>Profile Page</summary>

<details>
<summary>Desktop</summary>

![Desktop Image](./readme_media/wireframes/profile-desktop.png)

</details>

<details>
<summary>Tablet</summary>

![Tablet Image](./readme_media/wireframes/profile-tablet.png)

</details>

<details>
<summary>Mobile</summary>

![Mobile Image](./readme_media/wireframes/profile-mobile.png)

</details>

</details>

<details>
<summary>Sign up Page</summary>

<details>
<summary>Desktop</summary>

![Desktop Image](./readme_media/wireframes/sign_up-desktop.png)

</details>

<details>
<summary>Tablet</summary>

![Tablet Image](./readme_media/wireframes/sign-up-tablet.png)

</details>

<details>
<summary>Mobile</summary>

![Mobile Image](./readme_media/wireframes/sign-up-mobile.png)

</details>

</details>

### Accessability



## Database schema

![database schema](./readme_media/data_schema/data_schema.png)

### Final data schema

![Final database schema](./readme_media/data_schema/final_db_diagram.png)

### Differences Between the Database Schemas
#### Overview
This section outlines the differences between two versions of the database schema for our application. The first schema represents an initial design with fewer tables and relationships, while the second schema is more comprehensive, including additional tables and refined relationships to better capture the complexity of the application's data model.

##### Initial Schema
The initial schema contains the following tables:

users
products
orders
order_items
addresses
UserProfile
Table Details:
users

Contains basic user information such as username, email, password, first name, and last name.
Each user can have multiple addresses and orders.

**products**

Stores product details like name, description, price, image URL, size, and availability.
orders

Captures order-related information including the user who placed the order, the total amount, created date, and Stripe charge ID.

**order_items**

Represents items within an order, linking orders to products with additional fields like quantity and price.
addresses
Holds user address information, related to the user table via user_id.

**UserProfile**

Contains profile-specific information for users, linking to users and addresses.

##### Comprehensive Schema
The comprehensive schema includes the following tables, which extend the initial design:

users
products
orders
orderlineitems (renamed from order_items)
user_profiles (renamed from UserProfile)
addresses
categories
sizes
product_sizes
reviews
contactmessages
staffmembers
Table Details:
users

Similar to the initial schema but with additional fields for user status (is_staff, is_active) and date joined.

**products**

Includes a foreign key to categories and an association with sizes through the product_sizes table.
Stores product-related information including category, price, description, image, and availability status.

**orders**

Enhanced to include more detailed fields such as delivery cost, order total, and grand total.
Links to user_profiles instead of directly to users.

**orderlineitems**

Renamed from order_items to better reflect the naming convention and includes a product_size field.

**user_profiles**

Stores user profile information, linking to users and including default address details.
addresses
Expanded to store more detailed address information and linked to user_profiles.

**categories**

New table to categorize products, including a friendly name field.

**sizes**

New table to handle product sizes.

**product_sizes**

Intermediate table to handle many-to-many relationships between products and sizes.

**reviews**

New table to store product reviews, linking to products and optionally to users.

**contactmessages**

New table to capture contact messages from users or customers.

**staffmembers**

New table to store staff member information, including profile picture and bio.

Key Differences
Enhanced User and Profile Management

The comprehensive schema includes a more detailed users table and separates user profile information into the user_profiles table.
Adds fields for user status and date joined.
Address Management

Both schemas include an addresses table, but the comprehensive schema provides more fields and links to user_profiles for default address details.
Product Categorization and Sizes

The comprehensive schema introduces categories and sizes tables to better organize products.
Adds a product_sizes table to manage the many-to-many relationship between products and sizes.
Order and Order Items

The orders table in the comprehensive schema includes more detailed financial information.
The order_items table is renamed to orderlineitems and includes an additional product_size field.
Additional Tables

The comprehensive schema adds reviews, contactmessages, and staffmembers tables to capture more aspects of the application's functionality.

**Summary**
The comprehensive schema provides a more robust and detailed representation of the application's data model, supporting enhanced functionality and more complex relationships between entities. This refined design ensures better data integrity, organization, and scalability for future enhancements.


## Crud 

### Step 1 Create
For CRUD implementation, we have several features throughout the website:

Adding Products: Superusers can add new products from the product management link. They can input all necessary details such as name, description, image, sizes, and quantity.

Adding Staff Members: Superusers can add new staff members via the website. They can provide details like first name, last name, job title, bio, and profile picture.

Creating Reviews: Regular users can create reviews for products. They can rate the product and provide comments based on their experience with it.

### Step 2 Read
Users can view:

Product Listings: Users can browse through a list of available products, view their details such as name, description, and image, and see reviews and ratings provided by other users.

Individual Product Pages: Users can access detailed information about a specific product, including its name, description, image, available sizes, and reviews.

Staff Members Page: Users can see a list of staff members along with their names, job titles, and brief bios.

### Step 3 Update
Superusers can update:

Product Details: They can edit existing product details such as name, description, image, sizes, and quantity.

Staff Member Details: Superusers have the ability to modify staff members' information, including their names, job titles, bios, and profile pictures.

Reviews: only logged in user's can add/edit/delete reviews, superuser also has the ability to edit reviews where appropiate.

### Step 4 Delete
Superusers can delete:

Products: They have the authority to remove products from the system entirely, along with all associated details and reviews.

Staff Members: Superusers can delete staff members from the database, removing their information from the staff members' list.

Reviews: Superusers can delete inappropriate or irrelevant reviews submitted by users. This action removes the review from the product's page and the database.

## Stripe


When testing Stripe payment integrations, you can use specific test card numbers provided by Stripe. These card numbers simulate various payment scenarios. Here are the commonly used test card numbers for successful and unsuccessful purchases:

**Successful Purchase**

Visa: 4242 4242 4242 4242
Any CVC number
Any future expiration date

**Unsuccessful Purchase**

Card Declined: 4000 0000 0000 9995
Insufficient Funds: 4000 0000 0000 9995
Incorrect CVC: 4000 0000 0000 0127
Expired Card: 4000 0000 0000 0069
Processing Error: 4000 0000 0000 0119

## Features

### Home page 

![Homepage](./readme_media/site_images/home_page.png)

### All products page

![All products](./readme_media/site_images/all_products.png)

### individual products page

![individual products](./readme_media/site_images/individual_products.png)

### Cart page

![Cart page](./readme_media/site_images/cart.png)

### Checkout page 

![Checkout page](./readme_media/site_images/Checkout.png)

### Checkout Success page 

![Checkout success](./readme_media/site_images/checkout_success.png)



## Technologies Used

### Languages Used

HTML, CSS, JavaScript and Python have been used for this project.

### Frameworks, Libraries & Programs Used

Git - For version control.

[coolor](https://coolors.co/1c2321-7d98a1-5e6572-a9b4c2-eef1ef) This was used for my colour pallette.

[Github](https://github.com/Craig-Hudson) - To save and store the files for the website.

​
[Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.

​
[Font Awesome](https://fontawesome.com/) - For the iconography on the website.

​Chrome Dev Tools - To troubleshoot and test features, solve issues with responsiveness and styling.

[Convert png to webp](https://www.freeconvert.com/) - I converted my images to webp using this site.

[tiny.png](https://tinypng.com/) - To reduce the file size of my images for better website performance

Balsamiq - I used Balsamiq wireframes from a desktop app for my wireframes,

[W3School](https://www.w3schools.com/) To refer to anything Java script related that i may have been unsure of.

Gitpod - I have used vscode as my ide

## Testing

All my testing can be found in the [testing file](testing.md)

### Bugs

- **Solved Bugs**

- **Known Bugs**

Currently There is no known bugs

## Deployment & Local Development

### Deployment

The project is deployed using Heroku. To deploy the project:

#### ** Live Database**

SQL Lite can be used in local development, however for live deployment we must use an online external database. I have chosen Elephant SQL

1. Go to the [ElephantSQL](https://www.elephantsql.com/) dashboard and click 'new instance button' .
2. Name the plan, select tiny turtle plan (this is the free plan) and choose the region that is closest to you then click the review button.
3. Check the details are all correct and then click create instance in the bottom right.
4. Go to the dashboard and select the database just created.
5. Copy the URL

#### **Heroku setup**

  1. From the [Heroku dashboard](https://dashboard.heroku.com/), click the new button in the top right corner and select create new app.
  2. Name your app, select the region that is closest to you and then click the create app button bottom left.
  3. Open the settings tab and create a new config var of `DATABASE_URL` and paste the database URL you copied from elephantSQL into the value.

#### **Actions in IDE**

1. Install dj_database_url and psycopg2 by typing 'pip3 install dj_database_url==0.5.0 psycopg2'   

2. Type pip3 freeze > requirements.txt   

3. In settings.py underneath import os, add `import dj_database_url`

4. Under 'DATABASES', comment out the existing code. Type: DATABASES = { 'default': dj_database_url.parse('elephantsql-db-url-here')  } 

5. In the terminal, type 'python manage.py showmigrations

6. You should see a list of migrations that are unchecked. If so, type 'python manage.py makemigrations' followed by 'python manage.py migrate'   

7. Create a superuser for the new database by typing 'python manage.py createsuperuser. Follow the instructions and note the details  

8. Replace your DATABASE code (including commented-out code) with the following:

    if 'DATABASE_URL' in os.environ:
        DATABASES = {
          'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
          }
        }
   
10. Install gunicorn by typing 'pip3 install gunicorn' followed by 'pip3 freeze > requirements.txt'
    

11. Create a file called 'Procfile' in the root directory and add this line 'web: unicorn app_name.wsgi:application'

12. Ensure both your IDE and Heroku in the Allowed Hosts:
    
    ALLOWED_HOSTS = ['{heroku site URL}', 'localhost' ]

13. Save, commit and push all changes to GitHub

#### **Amazon Web Service for static files**

Access your AWS account:

Go to https://aws.amazon.com.
Click "Manage My Account" (top right) to sign up or log in.
Navigate to the S3 service.
Create a storage bucket:

Name the bucket after your project.
Choose your nearest region.
Under "Object Ownership," select "ACLs enabled" -> "Bucket owner preferred."
Under "Block Public Access," uncheck the box and acknowledge to make the bucket public.
Click "Create bucket."
Enable static web hosting:

Open the newly created bucket.
Go to the "Properties" tab.
Find "Static web hosting" and click "Enable."
Set "Index document" to index.html and "Error Document" to error.html (these files won't be used).
Configure bucket permissions:

Open the "Permissions" tab.
Copy the bucket's ARN (Amazon Resource Name).
In the "Bucket policy" section, click "Edit" -> "Policy generator."
Set the following:
Policy Type: S3 Bucket Policy
Principal: * (allow all)
Actions: Get Object
ARN: (Paste the copied ARN)
Click "Add Statement" -> "Generate Policy."
Copy the generated policy, paste it into the Bucket Policy Editor, and:
Add /* to the end of the Resource value.
Click "Save."

   

5. Paste the following code (replace this with the actual CORS configuration if you have a specific one):
[
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]

6. Now we need to edit the access control list (ACL) section. Click edit and enable list for everyone(public access) and accept the warning box.

#### **Creating AWS groups, policies and users**

Simplified Instructions

Access IAM and Create User Group

On the AWS Console, click the "Services" icon (top right) and find "IAM".
In the left menu, go to "User Groups" and click "Create Group."
Name your group (e.g., "manage-cricketgearhub")
Create an S3 Access Policy

Click "Create Policy."
Switch to the "JSON" tab and click "Import Managed Policy" (top right).
Search for "AmazonS3FullAccess" and click "Import."
Modify the Policy

In the "Resources" section:
Replace * with your bucket's ARN.
On the next line, paste the ARN again and add /* at the end.
Click "Next: Tags" -> "Next: Review."
Name and Create the Policy

Provide a name and description (e.g., "cricketgearhub-policy | Access to S3 bucket...").
Click "Create Policy."
Attach Policy to User Group

Navigate to "User Groups" (left menu) and select your group.
Go to the "Permissions" tab and click "Add Permissions" -> "Attach Policies."
Select your newly created policy and click "Add Permissions."
Create a User

Go to "Users" (left menu) and click "Add Users."
Create a username (e.g., "cricketgearhub-staticfiles-user").
Select "Programmatic Access" and click "Next: Permissions."
Add User to Group

Add your user to the group you created.
Click "Next: Tags" -> "Next: Review" -> "Create User."
Retrieve Keys

Immediately download the CSV with your user's access keys. This is your only chance to obtain them.

Connecting Django to Your S3 Bucket

1. Installation

Install necessary packages and update your requirements file:

Bash
pip3 install boto3 django-storages
pip3 freeze > requirements.txt
Use code with caution.
content_copy
Add storages to INSTALLED_APPS in your settings.py file.

2. Configure Django Settings (settings.py)

Add this code, replacing placeholders with your actual values:

Python
if 'USE_AWS' in os.environ:
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=9460800',
    }
    AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
    AWS_S3_REGION_NAME = 'your-region'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
Use code with caution.
play_circleeditcontent_copy
3. Set Heroku Config Vars

Add these keys/values in Heroku's config vars section, using the values from your AWS CSV file:

| KEY                      | VALUE                                              |
| ------------------------ | -------------------------------------------------- |
| AWS_ACCESS_KEY_ID        | Your access key from the CSV                       |
| AWS_SECRET_ACCESS_KEY    | Your secret access key from the CSV                |
| USE_AWS                  | True                                               |

4. Setup Custom Storages

Create custom_storages.py in your project root and add:

Python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = 'static'

class MediaStorage(S3Boto3Storage):
    location = 'media'

play_circleeditcontent_copy
5. Update Django Settings (settings.py)

Python
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage' 
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

play_circleeditcontent_copy
6. Deploy and Verify

Commit and push your changes to Heroku.
Verify static files were collected during deployment.
Check your S3 bucket for the 'static' folder.
7. Create S3 Media Folder

Navigate to your S3 bucket.
Create a new folder named 'media'.

Setting up Stripe

Obtain Stripe Keys

Log into your Stripe account.
Go to "Developers" -> "API Keys".
Retrieve your publishable key and secret key.
Add Keys to Heroku Config Vars

In Heroku's settings, create two new config vars:
STRIPE_PUBLIC_KEY (paste your publishable key)
STRIPE_SECRET_KEY (paste your secret key)
Set up Webhook

In Stripe, go to "Developers" -> "Webhooks" -> "Add endpoint".
Provide your deployed site's Webhook URL (e.g., https://your-site.herokuapp.com/webhook/)
Add a description (e.g., "Webhook for my-site")
Select "Receive all events".
Click "Create endpoint".
Retrieve the generated Webhook signing secret.
Add Webhook Secret to Heroku

Create a new Heroku config var:
STRIPE_WH_SECRET (paste your Webhook signing secret)
Update Django Settings (settings.py)

Python
import os

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
Use code with caution.
play_circleeditcontent_copy
Important: Ensure you replace the placeholder Webhook URL (https://your-site.herokuapp.com/webhook/) with your actual deployed site's Webhook endpoint.



### Local Development

How to Fork the Project

Have a GitHub account: If you don't have one, sign up for free.
Find the project: Go to https://github.com/Craig-Hudson/cricket-gear-hub.
Click "Fork": You'll find this button in the top-right corner of the project page. This creates your own copy of the project.
How to Clone the Project

Have a GitHub account: You'll need one if you don't already have it.
Find the project: Go to https://github.com/Craig-Hudson/cricket-gear-hub.
Copy the Clone Link:
Click the "Code" button.
Choose your preference (HTTPS, SSH, GitHub CLI) and copy the provided link.
Open your Code Editor: Use the one you're comfortable with.
Choose a Folder: Decide where you want to save the project on your computer.
Use the 'git clone' Command:
In your editor's terminal, type git clone and paste the copied link. Press Enter.
Optional: Set up a Virtual Environment (Skip this if unsure or using a pre-made setup)
Install Packages: In your terminal, run pip install -r requirements.txt
​

## Credits

### Images used


### Code Used

- Some of the code in the project was used from the walkthrough project provided by code institute this will be noted with comments in the code, and the remaining bits of code were written by myself.

### Content

The use of w3schools/MDN web docs and code institute lessons for any prompts and reminders for any template syntax or how to create the database models.

The other content for this project was written by Craig Hudson.

### media

- The images for this are royalty free images, some images that user's may add may not be royalty free.

### Acknowledgments

I would like to acknowledge the following people who helped me along the way in completing this project:

- My code institute mentor Brian for feedback and the many ways I can improve.
- My partner for having the patience with me and allowing me more time to work on projects.
- My fellow classmates Ross and dan for any hints and tips that they have given me over the last few weeks.
- Other family who have helped test my online book review and have given me constructive feedback, and ideas that I would be able to improve my application.