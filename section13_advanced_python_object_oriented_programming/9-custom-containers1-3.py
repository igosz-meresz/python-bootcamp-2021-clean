# ---------------------------------------------------------------------------------
# ----------------------------**## Custom Containers 1 ##**------------------------
# ---------------------------------------------------------------------------------

# --**--**--**--**--** Example 22 ->>>> creating a custom container
# class BookmarkedPage:
#     def __init__(self):
#         self.bookmarks = {}

#     def add(self, bookmark):
#         self.bookmarks[bookmark] = self.bookmarks.get(bookmark, 0) + 1


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("python")

# print(target_bookmark.bookmarks)

# --**--**--**--**--** Example 23 ->>>> handling corner cases
# class BookmarkedPage:
#     def __init__(self):
#         self.bookmarks = {}

#     def add(self, bookmark):
#         self.bookmarks[bookmark.lower().upper()] = self.bookmarks.get(
#             bookmark.lower().upper(), 0) + 1


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("PYTHON")

# print(target_bookmark.bookmarks)

# --**--**--**--**--** Example 24 ->>>> getting the count of key
# class BookmarkedPage:
#     def __init__(self):
#         self.bookmarks = {}

#     def add(self, bookmark):
#         self.bookmarks[bookmark.lower()] = self.bookmarks.get(
#             bookmark.lower(), 0) + 1

#     def __getitem__(self, bookmark):
#         return self.bookmarks.get(bookmark.lower(), 0)


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("PYTHON")

# print(target_bookmark.bookmarks)

# print(target_bookmark["python"])

# ---------------------------------------------------------------------------------
# ----------------------------**## Custom Containers 2 ##**------------------------
# ---------------------------------------------------------------------------------

# --**--**--**--**--** Example 25 ->>>> getting the count of key
# class BookmarkedPage:
#     def __init__(self):
#         self.bookmarks = {}

#     def add(self, bookmark):
#         self.bookmarks[bookmark.lower()] = self.bookmarks.get(
#             bookmark.lower(), 0) + 1

#     def __getitem__(self, bookmark):
#         return self.bookmarks.get(bookmark.lower(), 0)

#     def __setitem__(self, bookmark, count):
#         self.bookmarks[bookmark.lower()] = count


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("PYTHON")

# target_bookmark["python"] = 110

# print(target_bookmark.bookmarks)

# print(target_bookmark["python"])

# --**--**--**--**--** Example 26 ->>>> getting the number of bookmark types
# class BookmarkedPage:
#     def __init__(self):
#         self.bookmarks = {}

#     def add(self, bookmark):
#         self.bookmarks[bookmark.lower()] = self.bookmarks.get(
#             bookmark.lower(), 0) + 1

#     def __getitem__(self, bookmark):
#         return self.bookmarks.get(bookmark.lower(), 0)

#     def __setitem__(self, bookmark, count):
#         self.bookmarks[bookmark.lower()] = count

#     def __len__(self):\
#         return len(self.bookmarks)


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("PYTHON")
# target_bookmark.add("JavaScript")
# target_bookmark.add("JavaScript")
# target_bookmark.add("JavaScript")
# target_bookmark.add("Java")
# target_bookmark.add("Java")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("React")

# print(target_bookmark.bookmarks)
# print(len(target_bookmark))
# # 5


# --**--**--**--**--** Example 27 ->>>> iterating over the class

# class BookmarkedPage:
#     def __init__(self):
#         self.bookmarks = {}

#     def add(self, bookmark):
#         self.bookmarks[bookmark.lower()] = self.bookmarks.get(
#             bookmark.lower(), 0) + 1

#     def __getitem__(self, bookmark):
#         return self.bookmarks.get(bookmark.lower(), 0)

#     def __setitem__(self, bookmark, count):
#         self.bookmarks[bookmark.lower()] = count

#     def __len__(self):
#         return len(self.bookmarks)

#     def __iter__(self):
#         return iter(self.bookmarks)


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("python")
# target_bookmark.add("JavaScript")
# target_bookmark.add("JavaScript")
# target_bookmark.add("JavaScript")
# target_bookmark.add("Java")
# target_bookmark.add("Java")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("React")

# print(target_bookmark.bookmarks)

# for bookmark in target_bookmark:
#     print(bookmark)

# ---------------------------------------------------------------------------------
# ----------------------------**## Custom Containers 3 ##**------------------------
# ----------------------------------Private Members--------------------------------

# --**--**--**--**--** Example 28 ->>>> accessing a dict key from outside
# class BookmarkedPage:
#     def __init__(self):
#         self.bookmarks = {}

#     def add(self, bookmark):
#         self.bookmarks[bookmark.lower()] = self.bookmarks.get(
#             bookmark.lower(), 0) + 1

#     def __getitem__(self, bookmark):
#         return self.bookmarks.get(bookmark.lower(), 0)

#     def __setitem__(self, bookmark, count):
#         self.bookmarks[bookmark.lower()] = count

#     def __len__(self):
#         return len(self.bookmarks)

#     def __iter__(self):
#         return iter(self.bookmarks)


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("python")
# target_bookmark.add("JavaScript")
# target_bookmark.add("JavaScript")
# target_bookmark.add("JavaScript")
# target_bookmark.add("Java")
# target_bookmark.add("Java")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("React")

# print(target_bookmark.bookmarks)

# # print(target_bookmark.bookmarks["PYTHON"])
# print(target_bookmark.bookmarks["python"])

# --**--**--**--**--** Example 29 ->>>> blocking a dict key from outside
# class BookmarkedPage:
#     def __init__(self):
#         self.__bookmarks = {}

#     def add(self, bookmark):
#         self.__bookmarks[bookmark.lower()] = self.__bookmarks.get(
#             bookmark.lower(), 0) + 1

#     def __getitem__(self, bookmark):
#         return self.__bookmarks.get(bookmark.lower(), 0)

#     def __setitem__(self, bookmark, count):
#         self.__bookmarks[bookmark.lower()] = count

#     def __len__(self):
#         return len(self.__bookmarks)

#     def __iter__(self):
#         return iter(self.__bookmarks)


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("python")
# target_bookmark.add("JavaScript")
# target_bookmark.add("JavaScript")
# target_bookmark.add("JavaScript")
# target_bookmark.add("Java")
# target_bookmark.add("Java")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("React")


# # '__' blocks access to certain attributes for private reasons
# print(target_bookmark.__bookmarks)  # Not Available

# --**--**--**--**--** Example 29 ->>>> accessing a blocked dict from outside
class BookmarkedPage:
    def __init__(self):
        self.__bookmarks = {}

    def add(self, bookmark):
        self.__bookmarks[bookmark.lower()] = self.__bookmarks.get(
            bookmark.lower(), 0) + 1

    def __getitem__(self, bookmark):
        return self.__bookmarks.get(bookmark.lower(), 0)

    def __setitem__(self, bookmark, count):
        self.__bookmarks[bookmark.lower()] = count

    def __len__(self):
        return len(self.__bookmarks)

    def __iter__(self):
        return iter(self.__bookmarks)


target_bookmark = BookmarkedPage()
target_bookmark.add("python")
target_bookmark.add("python")
target_bookmark.add("Python")
target_bookmark.add("python")
target_bookmark.add("Python")
target_bookmark.add("python")
target_bookmark.add("JavaScript")
target_bookmark.add("JavaScript")
target_bookmark.add("JavaScript")
target_bookmark.add("Java")
target_bookmark.add("Java")
target_bookmark.add("GoLang")
target_bookmark.add("GoLang")
target_bookmark.add("GoLang")
target_bookmark.add("GoLang")
target_bookmark.add("GoLang")
target_bookmark.add("GoLang")
target_bookmark.add("React")

# __dict__

print(target_bookmark.__dict__)
