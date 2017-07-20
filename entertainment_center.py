import fresh_tomatoes
import media

gattaca = media.Movie("Gattaca",
                      "https://goo.gl/hy3CPn",
                      "https://www.youtube.com/watch?v=BpzVFdDeWyo")

five_centimeters_per_second = media.Movie("5 Centimeters Per Second",
                                          "https://goo.gl/JkvoKh",
                                          "https://goo.gl/gy1Zt4")

your_name = media.Movie("Your Name",
                        "https://goo.gl/LPFeqT",
                        "https://www.youtube.com/watch?v=xU47nhruN-Q")

five_hundred_days_of_summer = media.Movie("(500)Days of Summer",
                                          "https://goo.gl/nqV8gf",
                                          "https://goo.gl/qgjKL3")

movies = [gattaca,
          five_centimeters_per_second,
          your_name,
          five_hundred_days_of_summer]

fresh_tomatoes.open_movies_page(movies)
