# FBLA 2022 Project Planning

A reverse-chronological order log of project planning phases can be found here. 

This page will be updated as new changes are decided upon to showcase the design process of which the project undergoes.

***

## 1/15/23

+ Update CSS
+ Update icons

***

## 1/14/23

+ CSS for website aesthetics begun

***

## 1/11/23

+ Finished project requirements
+ Add prizes page complete with prize selection and error messages when users have insufficient credits
+ Added grade level to leaderboard
+ Added credit system where users who win during a previous quarter are granted credits to spend during the next quarter corresponding to their point balance
+ Began planning additional changes
  + Admin vs student accounts
  + Creating events on admin account
  + Informational page with information on how to use the website
  + CSS to beautify the project
  + Display attended events on dashboard page
  + Save redemption codes to user account
  + Beautify code

***

## 1/10/23

+ Sorted leaderboards by point value
+ Added ability to archive a quarter's leaderboard
+ Added ability to view old leaderboards

***

## 1/9/23

+ Added leaderboard page (wip)
+ Created leaderboard.html and prizes.html
+ Completed events page, users can now add events and earn points

***

## 1/8/23

+ Added point values to each event
+ Added ability to select and view a specific event on the events page

***

## 1/7/23

+ Fixed bug where users could sign up if student number was already in use
+ Added error message display for unsuccessful signup and login attempts
+ Added length requirement to forms on login page
+ Created three new files: events.html, events.json, events.py
+ Added events data to events.json
+ Displayed all events on new events page

***

## 1/5/23

+ Finished sign up and login portals
  + Users cannot login unless if they have already signed up

***

## 1/4/23

+ Created data folder for storing JSON files
+ Created users.py to handle the functionality of adding and checking users in a JSON file
+ Created users.json to store existing user information
+ Began the creation of adding and checking the users data upon attempted sign-up

***

## 1/3/23

+ plan.md renamed to planning.md
+ New template dashboard.html created
+ Add user session functionality (similar to browser cookies) to track if a user is logged in
+ Created a decorator in server.py to wrap functions, redirecting users when appropriate

***

## 1/2/23

+ Created templates and static folder to hold the HTML, CSS, and other related assets for the visuals of the website
  + Two templates, base.html and login.html, were created
+ requirements.txt created; flask, flask-session, and python-dotenv were listed as project requirements
+ server.py created with code to run a (basic) login and dashboard page for the website
+ HTML form created on the login page which redirects on submission

***

## 12/28/22

+ Project repository created.
+ README.md, plan.md, and .gitignore (for Python) files created.
+ Brainstorming of project begins. It was decided that a program accessed through a website, likely using the Flask micro web framework[^1], would be the most appropriate way to approach the prompt.
+ A few website names were considered, including: "Activitea" where each event ("activitea") fills up your teacup with more points; "Highlight" where the website is colorful to promote the idea that school events are fun and the "highlight" of your education; and "TrackPack" where you track events to fill up your 'trackpack', similar to a school backpack, which promotes an eduational theme. "TrackPack" was chosen as the best option.

__The following features were considered based on specific criteria from the project rubric.__

- [x] *"You must have a way to pick a random winner each quarter from each grade level, as well as the student with the top point accumulation."*
+ A student who wins for having the most points during a specific quarter will get an attribute on their profile stating their victory, i.e., "Top tracker Q1-22". Possible 2nd and 3rd place prizes could be offered. Consider picking the top person per grade level (ex. a senior had the most points overall, but in a different grade level, reward the top accumulator)
+ Students are chosen at random from each grade level to win if they participate with at least X number of points. One per grade level (4 total).

- [x] *"The number of points a person has accumulated will translate to the prize they win."*
+ Students who win randomly will be able to cash in their points for different prizes. If a student does not have enough points they cannot select locked prizes.

- [x] *"You will need to have at least three prizes (a school reward, a food reward, and a school spirit item).*"
+ School rewards: Tardy excuse, Skip the lunch line, be an administrator for a day... revisit ideas later
+ Food rewards: Chick-Fil-A lunch (a typical offer for being an Honors student), free a-la-carte item from the cafeteria, candy bag
+ School Spirit Item: School spirit hoodie, t-shirt, lanyards, stickers

- [x] *"Assign a point value for participating in or attending events."*
+ Participating in an event, for example, playing on a sports team, being in the school band, or volunteering at an event earns more points than watching, listening, or attending the same events in order to promote direct involvement rather than observation (but still rewarding both).
+ Proof of participating in or attending an event must be submitted. This could include a text box explaining what was done or an image upload to take a picture of a ticket to verify that the student was present.

- [x] *"Must have at least five sporting events and five non-sports school events."*
+ Sporting events include, but are not limited to: Baseball, basketball, soccer, football, flag football, tennis, golf, lacrosse, swimming
+ Non-Sporting events include, but are not limited to: Orchestra concert, band concert, math competition, Poetry Jam, Open House Information Night, Prom, Homecoming, studying sessions, club meetings
+ A teacher / administrator profile type could be created so events can be added as needed

- [x] *"Track students' names, grades, and points."*
+ Student name, grade level, student number and DOB can be stored on account creation
+ Points can be tracked using a file which sorts by student number (a unique identifier)

- [x] *"Generate a report at the end of the quarter to show points per student in each grade."*
+ Each student can have a dashboard where their points and total events for the year are visible
+ A leaderboard can be visible at all times with optional grade level filters to help students view their progress
+ TBD: How can students view a "final" copy of their rankings? Should there be a special page to show statistics (Ex. archives of Q1, Q2, etc. data with top events and students? A page to view current quarter statistics?

- [x] *"Data must be stored persistently. Storage may be in a relational database, a document-oriented NoSQL database, flat text files, flat JSON, or XML files."*
+ This will be revisited at a later date. Consider using flat JSON files for general data.
+ How will account login info be stored?

- [x] *"The user interface must be a GUI with a minimum of five different control types including such things as drop-down lists, text fields, checkboxes, date picker, or other relevant control types."*
+ Text box: For inputting event attendance validation, username, password, search fields, etc.
+ Drop-down menu: Filtering by grade level in leaderboard
+ Checkboxes: Prize page filter (show school rewards, food rewards, and school spirit items in a custom combination)
+ Other types can be determined at a later date

- [x] *"All data entry must be validated with appropriate user notification and error messages including the use of required fields."*
+ This can be used for word count minimums, password length requirements, and error messages when a username or student number is already in use

[^1]: https://flask.palletsprojects.com/en/2.2.x/
