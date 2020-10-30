# Book Inventory
Evaluation Project
The application has been deployed on book-inventory-1.herokuapp.com

## Implementation
The application has been made so as to be intuitive with many features which include notification messages that come up within the application to notify the user of the actions taken. The application has been designed to be visually appealing as well as intuitive and also mobile friendly.

The application has been developed in the Model View Controller (MVC) methodology.

#### Homepage
![Homepage Image](/Screenshots/Homepage.png?raw=true "Homepage")

## Reasoning Behind Implementation
The fields have been so chosen so as to match with the criteria. The fields specifically chosen in the tables are:- 
  - ID (which is the primary key of the database)
  - Title (Title of the book, which is automatically fetched from the Google Books API)
  - Author (Author of the book, which is automatically fetched from the Google Books API)
  - Google ID (Google Books Volume ID, which is automatically fetched from the Google Books API)
  - Stock (Has to be entered by the user, can only be greater than or equal to zero)
  - Status (Status of the Book - Available/Out Of Stock is automatically and dynamically entered by the system depending on the stock in inventory)

Notification messages popups within the application are implemented using Materialize Toasts to notify the user of the happenings within the system and to enhance the application's appeal.

It has been made sure that the stock of the book cannot be negative. It can only be greater than or equal to zero.

Validation checks are in place to ensure correct data entry into the application's database.

The automatic fetching from Google Books API is done so as to maintain consistency throughout the application as well as to make sure that the Google Books Volume ID is there for every book in the database.
As the entries for the above are fetched using Google Books API, the user can enter the details of the book in anyway he wishes to do so. 
Therefore, the three fields namely Title, Author and Google ID are read-only and the user has to enter the details of the book in the search box above to search the Google Books API, and then all the corresponding fields gets filled automatically to ensure integrity

AJAX has been used to fetch the data from the Google Books API in the Add Book/Edit Book section to enhance the usage of the application.

Suppose if the user enters a book which already exists in the database, then the stock of that particular book automatically gets updated in the inventory so as to ensure consistency as well as to prevent accidental duplication.

The status of the book dynamically gets updated as and when the stock gets altered.
