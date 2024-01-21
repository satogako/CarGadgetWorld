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
