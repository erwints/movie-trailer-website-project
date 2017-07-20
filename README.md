# movie-trailer-website-project

movie-trailer-website-project is a project in my Full Stack Web Developer Nanodegree Program

# Prerequisites

  - [Python](https://www.python.org/) must be installed
  - This repository must be forked and cloned

# How to Run
  - Open a terminal
  - Change directory to the location of the project
  - Run the following:
    ```sh
    $ python entertainment_center.py
    ```
# How to Add/Modify Movie List
  - Open `entertainment_center.py`
  - Add an instance in the designated area by using the following code and replacing the bracketed text(replace bracket as well):
    ```python
    [instance] = media.Movie("[movie title]",
                             "[movie box art link]",
                             "[youtube trailer link]")
    ```
    Example:
    ```python
    gattaca = media.Movie("Gattaca",
                          "https://goo.gl/hy3CPn",
                          "https://goo.gl/nhgjSW")
    ```
  - Run the following:
    ```sh
    $ python entertainment_center.py
    ```
# License
movie-trailer-website-project uses code from [this repository](https://github.com/adarsh0806/ud036_StarterCode) which does not list a license and for my purposes will be [unlicensed](https://unlicense.org/).
