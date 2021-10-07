# ---------------------------------------------------------------------------------
# --------------------**## Class Property & Property Decorator ##**----------------
# ---------------------------------------------------------------------------------

# --**--**--**--**--** Example 30

# class MovieRating:
#     def __init__(self, rating):
#         self.rating = rating

# movie_rating = MovieRating(10)
# movie_rating = MovieRating(-10)

# --**--**--**--**--** Example 31

# this is not a Pythonic code

# class MovieRating:
#     def __init__(self, rating):
#         self.set_rating(rating)

#     def get_rating(self):
#         return self.__rating

#     def set_rating(self, value):
#         if value < 0:
#             raise ValueError("Movie ratings cannot be 0")
#         self.__rating = value

# movie_rating = MovieRating(-5)


# --**--**--**--**--** Example 32

# class MovieRating:
#     def __init__(self, rating):
#         self.set_rating(rating)

#     def get_rating(self):
#         return self.__rating

#     def set_rating(self, value):
#         if value < 0:
#             raise ValueError("Movie ratings cannot be 0")
#         self.__rating = value

#     rating = property(get_rating, set_rating)

# movie_rating = MovieRating(-5)
# movie_rating = MovieRating(8)
# print(movie_rating.rating)


# --**--**--**--**--** Example 33

class MovieRating:
    def __init__(self, rating):
        self.rating = rating

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("movie rating cannot be 0")
        self.__rating = value


movie_rating = MovieRating(8)
print(movie_rating.rating)
