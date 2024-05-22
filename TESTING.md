# Readers Realm Testing

## Table of contents

- [Cricket gear hub testing](#Cricket-gear-hub-testing)
  - [Table of contents](#table-of-contents)
  - [Overview](#overview)
  - [Automated Testing](#automated-testing)
    - [Lighthouse](#lighthouse)
    - [HTML validator](#html-validator)
    - [CSS validator](#css-validator)
    - [JavaScript Validator](#javascript-validator)
  - [wave reports](#wave-reports)
  - [Manual Testing](#manual-testing)
    - [Testing user Stories](#testing-user-stories)
    - [Full Testing](#full-testing)

## Overview

I used test driven development throughout the entire build for this project.
This includes using chrome developer tools to test for responsiveness and for general positioning of elements, I also used the dev tools and the terminal with the use of print statements in my python to help identify if there was any errors in the console and where the issues may of been arising from.


## Automated Testing

### Lighthouse

- Desktop Lighthouse report perfect scores all round!

![Desktop Lighthouse report](documentation/lighthouse/lighthouse-desktop.png)

- Mobile lighthouse report 

![Mobile lighthouse report](documentation/lighthouse/lighthouse-mobile.png)

### HTML validator

I have used the html validator [W3C HTML Validator](https://validator.w3.org/)
Initially many of my html files had either info's or warnings, which have all been corrected,
A couple of my html files had errors which have now also been fixed and are all clear of errors.
![HTML Validation](documentation/validation/html-validation.png)

### CSS validator

- My css has come back with no errors and no warnings.

![CSS Validation](documentation/validation/css-validation.png)

### JavaScript Validator

- Home page JavaScript validation on JShint

![JavaScript validation](documentation/validation/javascript-validation.png)

- As you can see if the above image it's coming back with two info's

- First one is about emailJS not being defined, I followed along the code institute tutorial for
  setting up emailJS and emailJS is initialized in my base.html file starting on line 11.
  
- Second is the function sendMail being unused, but this is called on line 7 in my contact.html page

## wave reports

- Home Page

![Home page](documentation/wave-reports/home-page-wave.png)

- Browse Books Page

![Browse Books Page](documentation/wave-reports/browse-books-wave.png)

- Contact page

![Contact Page](documentation/wave-reports/contact-page-wave.png)

- Login page

![Login Page](documentation/wave-reports/login-wave.png)

- Register page

![Register page](documentation/wave-reports/register-page-wave.png)

- Review Page
  
![Review page](documentation/wave-reports/review-page.png)


## Manual Testing

### Testing user Stories

- **First time Visitors**

| Goals | How are they achieved? |
| ------------ | ------------ |
| As a first-time visitor, I want to be able to easily browse products. | This was achieved by ensuring there are multiple links easily seen by users when they enter the website, and giving users access to links to view products no matter what page they may be on. |
| As a first-time visitor, I want to be able to checkout as a guest. | This was achieved by not putting any restrictions on my checkout functions for non-users, therefore allowing them to be able to purchase items. |
| As a first-time visitor, I want the website to be visually attractive and provide a good user experience. | This was achieved by using Bootstrap's utility classes and some of my own custom CSS. |
| As a first-time visitor, I want to view individual products. | This was achieved by allowing users the ability to click on any product they like the look of, to then be taken to an individual product's page, where users will be able to view the product in a lot more detail. |
| As a first-time visitor, I want to be able to search for products manually, rather than scrolling through the website. | This was achieved by adding a search bar in my `base.html` so users can search for products on any page on the website. |


- **Returning Visitor Goals**

| Goals  |  How are they achieved? |
| ------------ | ------------ |
|  As a returning Visitor I want to be able to create an account. | This was achieved by using Django's built in package called allauth |
| As a returning Visitor I want a profile section on where I can view previous orders. | This was achieved by creating a profile app within my Django project, so that users have the ability to update their current address details, and also view their order history. |
| As a returning Visitor I want to be able to add/edit my current address. | This was achieved by allowing users to be able to edit their current address on their own profile pages. |
| As a returning visitor I want to be able to reset my password Incase I forget it. | This was achieved again by using the Django allauth package allowing users to recieve an email to click a link to reset their passwords.|
​

- **Frequent visitor goals**

|  Goals | How are they achieved  |
| ------------ | ------------ |
| As a frequent visitor, I want the e-commerce site to be mobile-friendly, so I can shop easily from my smartphone or tablet. | This was achieved by using bootstraps grid system using rows and columns, to determine how the website would look on different screen sizes ranging from mobile - p.c |
| As a frequent visitor, I want to leave reviews for products I have purchased, so I can share my experience with other customers. | This was achieved by adding reviews on the individual products page for logged in users to be able to add the reviews. |
| As a frequent visitor, I want to read reviews from other users, so I can make informed purchasing decisions. | This was achieved by allowing all users to be able to read reviews left by other users on the individual products page. |
| As a frequent visitor, I want my shopping cart to be saved across sessions, so I don't lose my selected items if I leave the site. | This was achieved by adding the users cart to a session storage, thus when users leave the website the items in their current cart will still be there, the cart is only reset when users have completed a purchase. |

### Full Testing

Testing was done on the following devices and browsers

- Devices
  - Lenovo Laptop 14inch screen
  - oppo xp lite (android)

- Browsers
  - Google chrome
  - Firefox

-**Base.html**

**Please note the following testing for base.html will consist of all the links which are also seen on every other page, as they all extend the base.html**

| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Cricket Gear Hub logo | To either refresh is on home page, or take me to home page if on another page. | Click logo | The page refreshed when I was on the home page, and when I wasn't on the home page I was taken to the home page | Pass |
| Search bar | Enter search criteria in and be taken to products that match search criteria | Enter search query | When entering in search queries I was taken to a page where It displayed products that match my query. | Pass |
| account icon(not logged in) | when clicked it should dropdown login and signup and links should take me to the correct pages| Click account icon | It displayed login and signup and when clicked I was taken to the correct page | Pass |
| account icon(logged in as superuser) | When clicked it should display Product management, staff management, profiile and logout  | Click icon and click links | When I clicked the icon all the relevent links where displayed, and I was taken to the correct pages when I clicked the links, and when I clicked logout, it logged me out of my account | Pass |
| account icon(logged in as user) | When account icon clicked it should display profile and logout, and when the links are clicked it should take me to the correct page | Click account icon and links | When I clicked the account icon It displayed profile and logout, and when I clicked the links it took me to the correct page | Pass |
| Mail Icon | When clicked it should take me to a contact page | Click Icon | I was taken to the contact page | Pass |
| Cart Icon | When clicked it should take me to the cart page | Click Icon | I was taken to the cart page | Pass |
| Footer links (social)| When clicked it should open a new tab and direct user to the relvant pages | Click links | New tabs were open and I was taken to the correct page | Pass |
| Footer links | When clicked I should be taken to the correct page | Click links | I was taken to the correct page everytime. | Pass |

- **Home page**

| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Carousel images | There are 4 carousel images, each each has a seperate url link that will direct users to the corresponding category of product | Click carousel image | I was taken to the correct urls | Pass |
| featured product image links | When clicked it should take me to that products individual page | Click image | I was taken to the individual page | Pass |
| View all button | When clicked I should be taken to the all products page | Click button | I was taken to the all products page | Pass |
| Description modal on featured product | When I click on the description text, it should pop up a modal with that product description | Click on text | The correct product title and description appeared in the modal for each | Pass |

- **Product pages**

| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Product image links | When Clicked it should take me to that products individiual product page | Click image | I was taken to the individual product page for the specific product | Pass |
| View button | When Clicked it should take me to that products individiual product page | Click button | I was taken to the individual product page for the specific product | Pass |
| Description modal | When I click on the description text, it should pop up a modal with that product description | Click on text | The correct product title and description appeared in the modal for each | Pass |
| Edit button(superuser only) | When clicking on edit button it should take me to the product management for that product, where I'll be able to edit details of that product | Click edit button | I was taken to the product management for that product, and was successfully able to edit product details | Pass |
| Delete Button(Superuser only) | When I click on the delete button it should pop up a modal, asking for confirmation that I want to delete the product, and if so it should delete the product from the database | Click delte button, and then confirm on the modal | The modal popped open, and then I was asked if i wanted to delete said product, after clicking confirm it then deleted the product from the database, and everywhere on the website. | Pass |

- **Individual product pages**

| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |  
| Add to cart form(error handling) | empty sizes or quanities less than 1 will throw an error message to the user | Don't enter a size, and make quantity zero. | Error shown to the user | Pass |
| Add to cart form(successful submission) | When the form has been succesfully filled it, it should add the product to the users cart and a toast message should pop up letting the user know it's been added | Fill out form and submit | The correct product was added to my cart, and correct price displayed next to the cart icon(top right) and the toast messsge popped up letting me know it's been successful | Pass |
| Edit button(superuser only) | When clicking on edit button it should take me to the product management for that product, where I'll be able to edit details of that product | Click edit button | I was taken to the product management for that product, and was successfully able to edit product details | Pass |
| Delete Button(Superuser only) | When I click on the delete button it should pop up a modal, asking for confirmation that I want to delete the product, and if so it should delete the product from the database | Click delte button, and then confirm on the modal | The modal popped open, and then I was asked if i wanted to delete said product, after clicking confirm it then deleted the product from the database, and everywhere on the website. | Pass |
| User reviews(not logged in) | As a user not logged in I should be able to add reviews for that product, and only be allowed to view other user reviews | Stay logged off and try to access adding a review | I was unable to add a review when logged off | Pass |
| User reviews(logged in) | When the user is logged in they should be able to view the add review section on the page, and add their review if successful form submission | goto page, and fill out form and submit | I was able to see the add review section, and after successfull form submission I was able to add a review, and the review was then displayed on the page. | Pass |
| Add review form validation | When fields are left empty it should leave an error message for the user if failed submission | Leave fields blank | Error message popped up to inform me of the error when I tried to submit. | Pass | 

- **cart Page**
  
| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| update quantity button/form | When I adjust the quantity it should stay at what I changed it to, also It should update the subtotals, grandtotals, and the total next to the icon(top right of screen) | change quantity | When I changed the quantity It updated all sub totals and totals to their correct amounts | Pass |
| Proceed to checkout button | Take user to checkout page |  |  |  |
| Remove button link, and confirming in modal | When user clicks the remove button they should see a modal appear where they will be asked if they want to remove item from cart, if they confirm it will delete the item from the cart, if they canel it will hide the modal. | Click remove button | Once clicked the modal appeared, When I clicked cancel it hide the modal, and when I pressed confirm it deleted the item from my cart | Pass |


- **Error Page**
  
| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Different error messages 404, 500, 503 to appear depending on what the error is | Different error number messages to appear depending on what is broken. | break website to display different error message | Different error messages appeared | Pass |
| Return home button | Taken user to home page | Click home page button | I was taken to the home page | Pass |

- **Add Book Page**
  
| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Input field user prompts if left blank | For the user to be prompted that the input fields need filling in, apart from the image url input field | Leave input fields blank, and fill in one by one | I was prompted to fill in input field on all but the image url as expected | Pass |
| Add book button | Once the user has filled in all input fields, they will be taken to the browse books page, where there book should be newly displayed, and it should also appear on the user's profile page, under book added. | Fill out add book form, and click add book | I was taken to the browse books page where the book I just added is displayed, It also was displayed under books added on my profile page | Pass |

- **Edit Book Page**
  
| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Book details already stored in input fields from the database. | When I arrive on the edit book page, I will expect the book details for that certain book to be already there. | Goto edit book page | I checked two books, and the details for that certain book were already in the input fields. | Pass |
| User to be promoted if they leave input fields blank when editing. | User to be prompted to fill in a certain input field if left blank. | Leave input fields blank. | I was prompted to fill in the input field when I left them blank. | Pass |

- **Add Review Page**
  
| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Form Input fields | for user to be prompted to fill in both input fields. | Leave input fields blank to see if a prompt occurs. | When I left the input fields blank I was prompted to if fill out both input fields. | Pass |
| Add review button | Once the user clicks on the add review button they should be taken back to the review page for the certain book they left their review on, their new review will be displayed, and it will also be displayed in the users profile, under reviews added. | Click add review button. | I was directed to the review page for the book I left a review on, I also went over to my profile, to find that my review was also added under reviews added. | Pass |

- **Edit Review Page**
  
| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
|  Book details already stored in input fields from the database. | Review details already stored in the input fields. | Go to edit review page to see if the review details are already stored. | When I went to the edit review page the review details were already stored in the form input fields | Pass |
| Form Input fields | for user to be prompted to fill in both input fields.  | leave input field blank. | When I left any of the input fields blank, I was prompted to fill them out. | Pass |
| Edit review button | Once user has clicked button, It should refresh page, flash a message to the user, confirming review has been edited, pre populate with new data. | Click edit review button. | Once I clicked the edit review button the page reloaded, and a flash messaged appeared confirming that the editing had been completed, and the new data was pre populated in the form fields | Pass |

- **Review Page**
  
| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Add review button | Once clicked, it should take user to the add review page. | Click button | I was taken to the add review page. | Pass |

- **Profile Page**
  
| Feature  | Expected outcome  | Testing performed  | Result  | Pass/Fail  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Delete Buttons on Reviews and Books. | Once A user clicks on the delete button, a pop up modal should appear giving the user an option of cancelling the delete, or deleting the review or book. | Click delete button. | Pop up modal popped up every time a delete button was clicked. | Pass |
| Cancel button on modal. | To close modal down. | Click cancel button. | Modal closed | Pass |
| Delete button on modal. | Once the delete button has been clicked on the modal, it will close the modal down, and it will delete the review or book the user has chosen to delete, note this will delete them everywhere on the website. | Click delete modal button. | Once I deleted a review and deleted a book, they disappeared everywhere on the website. | Pass |