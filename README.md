Welcome to Food with Friends!

I have built this web application in order to assist with the "What's for dinner" conversation that I always have with my friends.

To run the project:
- Download the repository / code
- cd into the foodwithfriends directory
- Run python manage.py makemigrations foodpoll to make migrations for the foodpoll app
- Run python manage.py migrate to apply the migrations to the database
- Run python manage.py runserver

Features:
- Register/Login: You can register yourself as a user / log in with your email, username, and password.
- Set Preferences: Once logged in, you can set your user's food preferences (location, cuisine type, and price range).
- Search: Once you have saved your preferences, you can search for other users (searched by their username). For example, you can search for my test user: benjf
- Compare: In the search results, you can click to Compare Preferences with those particular users. The comparison will be made and those in-common preferences between your user and the user you selected will appear.

My models.py file includes all the datatypes involved. Users, Preferences, and some of those individual preference options (Location, Cuisine, Price).

I created a new urls.py file in my foodpoll application folder to include all the relevant paths that point you to the different views that are included in my views.py file.

To add data into my database manually, I registered all models in my admin.py file to make it easier to add test users and make sure data was being saved and retrieved accurately.
