# Book Inventory
Evaluation Project
The application has been deployed on http://book-inventory-1.herokuapp.com/

## Implementation
The application has been made so as to be intuitive with many features which include notification messages that come up within the application to notify the user of the actions taken. The application has been designed to be visually appealing as well as intuitive and also mobile friendly.

The application has been developed in the Model View Controller (MVC) methodology. The code has been written with the correct format with comments added wherever possible to ensure extensibility and easy readability.
The code also makes use of DRY concept (Don't repeat yourself) which is why templates are used and extended wherever possible to make the code as neat as possible and also to ensure easy extensibility of the application in the future.

#### Homepage
![Homepage Image](/Screenshots/Homepage.png?raw=true "Homepage")

#### Add Book
![Homepage Image](/Screenshots/Adding Book.png?raw=true "Homepage")
The user searches for the book in the search box that searches Google API for the corresponding book and it's details and consequently fills the corresponding entries automatically along with Google Books Volume ID. This is done to maintain integrity and consistency.

#### Entering Details In Search Box
![Homepage Image](/Screenshots/Entering Details.png?raw=true "Homepage")

#### Entry Gets Added 
![Homepage Image](/Screenshots/Entry Gets Added.png?raw=true "Homepage")

#### Editing Book Details
![Homepage Image](/Screenshots/Editing Book Details.png?raw=true "Homepage")

#### Notification Popups
![Homepage Image](/Screenshots/Notification Popup.png?raw=true "Homepage")

#### Search Results
![Homepage Image](/Screenshots/Search Results 1.png?raw=true "Homepage")
The user can use the search box in the navigation bar to search for books, the application searches for books from Google Books API and also shows which books are 'Available/Out Of Stock' in inventory along with the corresponding button next to it to view the book.
It shows 'Not Available' for books that are unavailable in the inventory.

#### Search Results
![Homepage Image](/Screenshots/Search Results 2.png?raw=true "Homepage")

## Assumptions Made
Here are the assumptions made in developing the application:-
  - Every book requires a Google Books Volume ID.
      - This is why the entries are fetched from Google Books API to ensure that each entry has a Google Books Volume ID.
  - Data format is important which is why no custom entries are permitted.
  - The application being dynamic is important.
  - The book store owner sells a huge stock of books in one go which is why there is no button for Sale which decrements the stock by one on each click.
  - The publisher of the book does not matter.
  - Description and additional details of the book is not mandatory.
  
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

## Getting Started 
The application has been hosted on http://book-inventory-1.herokuapp.com/, however if you wish to setup the application on your local server, here is the way to do so:-
1. Change to the folder
    ```
    cd book_inventory
    ```

2. Install all the dependencies
    ```
    pip install -r requirements.txt
    ```
3. Run the server using
  ```
  python manage.py runserver
  ```
4. Visit http://127.0.0.1:8000/ on your local browser.

