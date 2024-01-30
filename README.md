# Car Gadget World

[![](docs/images/car_gadget_world.jpg)](https://car-gadget-world-605f69b77cdd.herokuapp.com/)
[Link to Live Site](https://car-gadget-world-605f69b77cdd.herokuapp.com/)


## Introduction

The project is an E-commerce site for a store that sells both universal accessories and branded ones for a specific car brand.

Users, including guests, can view accessories, and only registered users can add them to their cart and place orders.

The project was built with Agile management principles in mind, and I used a lot of GitHub features like Issues and Projects to implement the scrum methodology, even though I was working on my own.

I wanted to create an interface for the business owner to manage the store without logging into the Django admin panel.

[Kanban Board for project](https://github.com/users/satogako/projects/6/views/1)

[Closed Issues on GitHub for the project](https://github.com/satogako/CarGadgetWorld/issues?q=is%3Aissue+is%3Aclosed)

I used [GitHub issues](https://github.com/satogako/CarGadgetWorld/issues) for the product backlog containing the user stories.

I used the tags feature in GitHub Issues for assigning story points, prioritising features based on [the MoSCoW method](https://en.wikipedia.org/wiki/MoSCoW_method).

I used the [Milestones feature](https://github.com/satogako/CarGadgetWorld/milestones?state=closed) to plan sprints and set deadlines.


## User Stories

User stories were prepared using GitHub Issues and assigned story points based on estimated completion time.

User Stories can been seen below under [User Story Testing](#user-story-testing), and in the [GitHub Issues](https://github.com/satogako/CarGadgetWorld/issues?q=is%3Aissue+is%3Aclosed) for full details story points and associated sprints.


## UX

I used the color palette below for the overall design of the site pages:
![](docs/images/colour_palette1.jpg)

The following color palette was used for active site elements such as buttons and links:
![](docs/images/colour_palette2.jpg)

I used CSS Variables to use my chosen colour palette and font across the project easily.
```
    CSS
:root {
    --font-display-font: 'Rubik', sans-serif;
    --main-bg-color: #f7f7f7;
    --color-primary: #333333;
    --color-secondary: #007bff;
    --color-white: rgba(255, 255, 255, 1);
    --color-gray: rgb(224,224,224);
    --button-color: #28a745;
    --color-red: #ff4136;
    --color-black: #000103;
    --color-off-white: rgba(255, 255, 255, 0.8);
    --color-text: #666666;
    --color-header: #333333;
}
```

I used the version of Bootstrap (5.0), which includes support for CSS Variables. 
I used this new recommended approach along with my own variables to customise bootstrap elements. 

An example of this can be seen on one of the custom classes for button link:
```
    CSS
.btn-home-color:hover{
    background-color: var(--color-black) !important; 
    border-color: var(--color-secondary) !important;
    color: var(--color-white) !important;
}
```
See: [Bootstrap Docs - Root Variables](https://getbootstrap.com/docs/5.0/customize/css-variables/#root-variables)


### Typography

I used the sans-serif font [Rubik](https://fonts.google.com/specimen/Rubik) from Google Fonts. I like its subtle rounded corners and it makes a nice readable display font for the logo and headings.

![](docs/images/rubik_font_preview.jpg)

For the body text, I let Bootstrap style the font as it used a native font stack for different devices resulting in a nice native looking appearance.
See: [Bootstrap Docs - Native Font Stack](https://getbootstrap.com/docs/5.0/content/reboot/#native-font-stack)


### Wireframes

I drew some wireframes using [Balsamiq](https://balsamiq.com/) of the landing page and products page. I knew I had the elements available in Bootstrap to get this layout up and running fast.

![](docs/images/wireframe_home.png)

![](docs/images/wireframe_accessories.png)


### Accessibility

I ensured the website is accessible to people with visual impairments by: 
- Used semantic HTML elements like  ```<header> ,  <nav> ,  <main> ,  <footer>```  etc. This helps screen readers navigate the page. 
- Provided alt attributes for all images. The alt attributes describe the image content to screen readers. For example:
	```
		<img src="{{ product.image_link }}" 
				alt="{{ product.name }}"/>
	```
- Used Bootstrap components which are accessible by default. For example, Bootstrap buttons, forms, modals etc. come with proper ARIA attributes and keyboard functionality.  
- Adding  aria-label  attributes to icons and links to convey meaning to screen readers. For example:
  ```
    <a href="https://github.com/satogako/CarGadgetWorld"
			target="_blank"
			rel="noopener"
			aria-labelledby="github-repo">
			<i class="fa-brands fa-square-github fa-xl"></i> 
			<span id="github-repo"> Github Repo</span>
    </a>
  ```
- Ensured good color contrast between foreground and background colors to aid low vision users. I used a color contrast checker to verify contrast ratios.
- Ensured all interactive elements are keyboard focusable and the visual focus indicator is clearly visible.


# Features

## Existing Features

### Landing Page

The landing page contains an attractive main image and a headline that provides the user with a brief description of what the store sells.

 Below that is a Shop Now button that prompts the user to see items for sale. The button has a green color and, when pressed, takes on the main colors of the image, which gives the client the effect of starting the car. All this additionally encourages the customer to click and go to the store's accessory sales page.

 <details>
<summary>
Screenshot of the full landing page on desktop and mobile
</summary>

![](docs/images/landing_page1.jpg)

![](docs/images/landing_page2.jpg)

![](docs/images/landing_page_mob1.jpg)

![](docs/images/landing_page_mob2.jpg)

</details>


### Navbar

The navigation panel contains drop-down menus for viewing accessories: by category, by car brand, and by car accessory manufacturer.

Guests see links to Register or Login.

Logged in users will see their username and a dropdown list containing:
- Logout

<details>
<summary>
Screenshot of dropdown for users
</summary>

![](docs/images/drop_down_registered_users.jpg)

</details>


In addition to these, staff members have access to:
- Product Management
- Logout

<details>
<summary>
Screenshot of dropdown for staff members
</summary>

![](docs/images/drop_down_staff_members.jpg)

</details>


### Shopping cart

Only registered users can add products to their shopping cart, and the cart total is clearly displayed in the navigation bar on large screens and above. On smaller screens, click on the burger button to see the cart total.

On the cart page, users can change the quantity and if they want to remove the accessory from the cart

<details>
<summary>
Screenshots of Shopping Cart on desktop and mobile
</summary>

![](docs/images/screenshot_desktop_cart.jpg)

![](docs/images/Screenshot_mobile_cart.jpg)

</details>


### Breadcrumbs

Breadcrumbs are present on all pages, which help the user to quickly orient himself on which page of the store he is on. Also, with the help of Breadcrumbs, the user can go to previous pages that he has already visited.

<details>
<summary>
Screenshot of breadcrumbs on desktop and mobile
</summary>

![](docs/images/breadcrumbs_desktop.jpg)

![](docs/images/breadcrumbs_mobile.jpg)

</details>


### List of All Accesories.

If you are on the All Accessories page, you will see a list of products that are sold in the Сar Gadger World online store.

Each product has:
- Picture. 
- The name of the manufacturer who made this accessory.
- The name of the product.
- Stock Keeping Unit.
- Informing the buyer of which cars the accessory is suitable for, or information that this product is universal and suitable for all brands of cars.
- The price of the accessory has a larger font and is placed on a gray background to make it easier and faster for the buyer to find it.

Sort options are available to sort the list by:
- The newest ones first
- Name (A-Z)
- Name (Y-A)
- Price (low to high)
- Price (from high to low)

<details>
<summary>
Screenshots of the All Accessories page
</summary>

![](docs/images/all_accessories_page.jpg)

List of accessories with sorting options:
![](docs/images/all_accessories_page_with_sortmenu.jpg)

</details>
<br>

**Only staff have access to the buttons:**
- Edit. Allows to edit the accessory.
- Delete. Allows to delete the accessory.


### Product Details Page

The Product Details page provides users with an enlarged image and has the following information about the accessory:
- Enlarged image. 
- The name of the manufacturer who made this accessory.
- The name of the product.
- Stock Keeping Unit.
- Detailed description of the accessory.
- Informing the buyer of which cars the accessory is suitable for, or information that this product is universal and suitable for all brands of cars.
- The price of the accessory has a larger font and is placed on a gray background to make it easier and faster for the buyer to find it.
- A cell for entering the quantity. 
- A button to add the accessory to the shopping cart.

If the user has previously registered, the accessory is added to the cart by clicking the ADD TO CART button, and if not, the user is redirected to the Register page for registration.

If the accessory is not available, instead of the ADD TO CART button, the inactive OUT OF STOCK button is displayed in gray.

<details>
<summary>
Screenshots of Product Detail page
</summary>

![](docs/images/product_details.jpg)

![](docs/images/product_details_out_of_stock.jpg)

</details>
<br>

**Only staff have access to the buttons:**
- Edit. Allows to edit the accessory.
- Delete. Allows to delete the accessory.


### Sign UP / Sign In

Users can register using the Sign UP page or, if the user was previously registered, Sign In on the Login page.

After registration, the Confirm Email page opens, where users are provided with information that the letter has been sent to their mailbox for verification.

<details>
<summary>
Screenshot of Sign UP, Sign In, Confirm Email and Sign Out pages
</summary>

![](docs/images/sign_up.jpg)

![](docs/images/sign_in.jpg)

![](docs/images/confirm_email.jpg)

![](docs/images/sign_out.jpg)

</details>


### Checkout

The ordering process consists of two stages:

1.  - View the order
    - Add delivery address
    ![](docs/images/checkout_address_and_order.jpg)
    - Enter payment details
    ![](docs/images/checkout_payment_info.jpg)
2.  - Order confirmation
    ![](docs/images/order_success.jpg)

The Checkout page clearly displays the total to be paid. And also under the button COMPLETE ORDER will appear a message which
 will inform the buyer that he will be charged an amount equal to the amount of the order.

 If the user enters incorrect card data, the message "You card number is invalid" will appear under the Payment cell, which clearly informs him about the problem.

All information related to Billing is handled by Stripe.

Billing Address or Card details are **never** saved in the database.


### Footer

The Footer includes:

- A link back to the All Accessories page
- Link to the Subscribe to the Newsletter page.
- A link to the Privacy Policy
- A link to the [GitHub repository for the project](https://github.com/satogako/CarGadgetWorld).

<details>

<summary>Screenshot of Footer on desktop and mobile</summary>

![](docs/images/footer_large_screen.jpg)

![](docs/images/footer_mobile_screen.jpg)


</details>


### Privacy Policy

I included a Privacy Policy link in the Footer which explains how data may be used. I used [Privacy Policy Generator](https://www.privacypolicygenerator.info/) for help writing the policy.

<details>
<summary>
Screenshot of Privacy Policy
</summary>

![](docs/images/privacy_policy1.jpg)
![](docs/images/privacy_policy2.jpg)
![](docs/images/privacy_policy3.jpg)
![](docs/images/privacy_policy4.jpg)
![](docs/images/privacy_policy5.jpg)
![](docs/images/privacy_policy6.jpg)

</details>


### Notifications

Django Notifications and Bootstrap's notification elements have been combined to create elegant notifications that can be dismissed when the user performs an action.

The user, depending on his actions, can receive four types of messages:
- Success notification.
- Informative message.
- Warning.
- Error message.

<details>
<summary>
Screenshots of four types of messages
</summary>

![](docs/images/success_message.jpg)

![](docs/images/info_message.jpg)

![](docs/images/warning_message.jpg)

![](docs/images/error_message.jpg)

</details>


### Favicon

![](media/favicons/favicon.ico)

Users can add a link to the Car Gadget World website to the home screen of their smartphone or tablet if they are using a mobile browser. At the same time, the icon of the website will be displayed on the main screen, as well as the name of the application. Users can conveniently launch the website by clicking on this icon on their device's home screen.

I added theme color and background_color `"theme_color": "#333333",
"background_color": "#333333",` in the site.webmanifest file to give the site a more consistent look in [PWA](https://en.wikipedia.org/wiki/Progressive_web_app) mode and better match its overall color scheme.


## Staff Only Features

### Product Management

Staff can add products without using the Django admin panel. For this, a convenient form is used on the Add a Product page. To get to this page, the staff needs to click on the user's name in the Navbar and select Product Management.

<details>
<summary>
Screenshot of Add a Product page
</summary>

![](docs/images/add_product_page.jpg)

</details>


### All Accessories page

For staff, the All Accessories page contains links to each product:
- Edit. To edit the product, the user is redirected to a separate page.
- Delete. To remove the product. The user remains on this same page. When you click on remove, the product is immediately removed without confirmation.

<details>
<summary>
Screenshot of All Accessories page as staff member
</summary>

![](docs/images/all_accessories_staff.jpg)

Screenshot of editing a product as staff member
![](docs/images/edit_product_staff.jpg)

</details>


### Product Details page

For staff, the Product Details page contains links to each product:
- Edit. To edit the product, the user is redirected to a separate page.
- Delete. To remove the product. The user remains on this same page. When you click on remove, the product is immediately removed without confirmation.

<details>
<summary>
Screenshot of Product Details page as staff member
</summary>

![](docs/images/product_details_staff.jpg)

Screenshot of editing a product as staff member
![](docs/images/edit_product_staff.jpg)

</details>


## Custom Error Page

Custom error page were added for 404 errors.

<details>
<summary>Screenshot of custom 404 page</summary>

![](docs/images/screenshot_404.jpg)

</details>


## Features Left to Implement

Features I didn't get to implement in this iteration but plan to add in future include:

- Guests should be able to place orders without registering for an account
- A Discount Code system or Option for time-based Sales
- I would like migrate to using Stripe Checkout as some of these features like discount codes come built-in.
- Mailchimp could be connected to user profiles to include campaigns such as birthday emails with discounts, or follow up emails on completed orders.
- Sign in with Google.
- Add a CAPTCHA or some other form of validation to Contact Us form to prevent abuse.
- Add a "recently viewed" carousel of products to follow the user around the site.
- Add the ability for users to add products to their wish list. This would be useful for users who want to keep track of products they are interested in but don't want to purchase.
- Add a page that would display a list of orders made, so that staff do not need to enter the admin panel, but can do it directly from the site itself.
- Compress product images with [TinyPNG](https://tinypng.com/) to speed up pages loading.
- I haven't finished the user profiles due to lack of time, which I plan to complete so that returning buyers don't have to add their details again.
- Add auto-completion of the email field on the checkout page so that the user who registered or logged in does not need to fill it in again.


## Technologies Used

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [pip](https://pip.pypa.io/en/stable/) for installing Python packages.
- [Git](https://git-scm.com/) for version control.
- [Sourcetree](https://www.sourcetreeapp.com/) for managing the remote repository.
- [AWS S3](https://aws.amazon.com/s3) used for online static file storage.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [GitHub](https://github.com/) for storing the repository online during development.
- [Visual Studio Code](https://code.visualstudio.com/) as a local based IDE.
- [Balsamiq](https://balsamiq.com/wireframes/) for wireframing.
- [Bootstrap 5](https://getbootstrap.com/) as a front end framework.
- [Google Chrome](https://www.google.com/intl/en_ie/chrome/), [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) and [Safari](https://www.apple.com/safari/) for testing on macOS Monterey.
- [Microsoft Edge](https://www.microsoft.com/en-us/edge) for testing on Windows 11.
- [Safari](https://www.apple.com/safari/) on iOS and iPadOS 15.
- [Google Chrome](https://www.google.com/intl/en_ie/chrome/) on Android 12.
- [Mailchimp](https://mailchimp.com/) for newsletter subscription service.
- [favicon.io](https://favicon.io/favicon-generator/) to make a favicon for site.
- [Meta Tags](https://metatags.io/) to prepare the Meta tags for social media share previews.


## Ecommerce Business Model

This site sells goods to individual customers, and therefore follows a `Business to Customer` model.
It is of the simplest **B2C** forms, as it focuses on individual transactions, and doesn't need anything
such as monthly/annual subscriptions.

It is still in its early development stages, although it already has a newsletter, and links for social media marketing.

Social media can potentially build a community of users around the business, and boost site visitor numbers,
especially when using larger platforms such a Facebook.

A newsletter list can be used to send regular messages to site users who opt in, such as what items are on special offer, new items in stock.


## Search Engine Optimization (SEO) & Social Media Marketing

### Keywords

I've identified some appropriate keywords to align with my site, that should help users
when searching online to find my page easily from a search engine.
I made sure to make use of semantic html so these keywords were picked up by search engines.

```html
<title>Car Gadget World | Car Accessories</title>
      <meta name="description" 
        content="Car Gadget World is an online store offering high quality
         and stylish car accessories to enhance your driving experience."
      >

      <meta name="keywords" 
        content="car accessories, car gadgets, car chargers, car phone holders,
         car vacuum cleaners, car air fresheners, car organizers, car pillows, 
         car keychains, branded car accessories, car accessory brands, luxury 
         car accessories, car interior accessories, car exterior accessories, 
         premium car accessories"
      >
```


### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file.
This was generated using my deployed site URL: https://car-gadget-world-605f69b77cdd.herokuapp.com/

After it finished crawling the entire site, it created a
[sitemap.xml](sitemap.xml) which I've downloaded and included in the repository.


### Robots

I've created the [robots.txt](robots.txt) file at the root-level.
Inside, I've included the settings:

```
User-agent: *
Disallow: /cart/
Disallow: /checkout/
Disallow: add/
Disallow: edit/
Disallow: delete/

Sitemap: https://car-gadget-world-605f69b77cdd.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)


### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales.

I included links in the footer which could be used for potential Facebook, Twitter, Instagram and TikTok presences for the business.

I've created a mockup Facebook business account using the
[Balsamiq template](https://code-institute-org.github.io/5P-Assessments-Handbook/files/Facebook_Mockups.zip)
provided by Code Institute.

<details>

<summary>Facebook Page Mockup</summary>

![](docs/images/facebook_page_cgw.jpg)

</details>
<br>
For this business I envision a lot of the social media marketing being very visual, using the current most popular formats like Instagram Reels and TikTok. As these are primarily video based I did not mock any for the purposes of this coding project.


### Newsletter Marketing

I used [Mailchimp](https://mailchimp.com/) to set up a newsletter sign-up form on my application, to allow users to supply their
email address if they are interested in learning more and to drive repeat business. 

There's a lot of power in Mailchimp, and campaigns could be set up such as a discount code near a customer's birthday, or integration with webhooks.

<details>
<summary>
Screenshots of Newsletter Sign-up Form
</summary>

![](docs/images/news_letter_page.jpg)

</details>






