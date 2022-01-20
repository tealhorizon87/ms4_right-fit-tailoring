# Testing

This page contains all the stages that I went through to test this application and it's features.

You can return to the main README page [here](README.md)
## Table of Contents
1. [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
2. [Responsiveness](#responsiveness)
3. [Performance](#performance)
4. [Objective Testing](#objective-testing)
5. [User Story Evaluation](#user-story-evaluation)

## Code Validation

### HTML
The HTML code was passed through the [W3C Markup Validation Service](https://validator.w3.org/). Minor changes were made such as removing a `<p>` tag as a child of a `<button>` tag, and removing unnecessary attributes. The changes made can be seen in commit [#504bbca](https://github.com/tealhorizon87/ms4_right-fit-tailoring/commit/504bbcae80fcfcd6f24d601106054cc6036e8aa1).

### CSS
The CSS files were passed through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). No errors or warnings were found.

### JavaScript
The JavaScript file was copied into [JSLint](https://www.jslint.com/) for error checking. No errors were found.

### Python
The python code was copied into [PEP8 online](http://pep8online.com/) for error checking. Minor issues were fixed, such as line length and line spacing. The changes made can be seen in commit [#d872a0a](https://github.com/tealhorizon87/ms4_right-fit-tailoring/commit/d872a0a3e5738e9b1283c35af105cd6cac785bee).

## Responsiveness

This application was built using [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) and as such, responsiveness was inherent within the design. All pages are displayed correctly on all screen sizes without compromising the content of the page.

## Performance

### Lighthouse
Lighthouse was used to assess the performance of the page. This was done for both desktop and mobile versions. All pages were tested successfully and returned values in the green band for all sections. Those items that were not passed, such as text contrast in the search bar, are considered acceptable issues, or issues involving externally linked pages.

### Cross-Browser Compatibility
The link for the site was uploaded to [BrowserStack](https://www.browserstack.com/). The site was then loaded using multiple browsers, and all worked exactly as expected.

Back to [Table of Contents](#table-of-contents)

## Objective Testing

Due to time constraints on this project, unit testing was not possible. However, I have endeavoured to check all the functionality through objective testing according to the below test matrix:

![test matrix](docs/images/test-matrix.png)

The full table can be found [here](docs/docs/test-matrix.pdf).

The user authentication section has not been tested in this project as it has come directly from Django allauth and will have been thoroughly tested before release.

Back to [Table of Contents](#table-of-contents)

## User Story Evaluation

Finally, to make sure that the goals set out at the beginning of the project have been met, the user stories were evaluated:

Back to [Table of Contents](#table-of-contents)
