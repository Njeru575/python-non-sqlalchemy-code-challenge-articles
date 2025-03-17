class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        author._articles.append(self)  
        magazine._articles.append(self)  
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string.")
        if len(value) < 5 or len(value) > 50:
            raise Exception("Title must be between 5 and 50 characters, inclusive.")
        if hasattr(self, "_title"):
            raise Exception("Title cannot be changed after instantiation.")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be of type Author.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be of type Magazine.")
        self._magazine = value
class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        if len(value) == 0:
            raise Exception("Name must be more than 0 characters.")
        if hasattr(self, "_name"):
            raise Exception("Name cannot be changed after instantiation.")
        self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    all = []  

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []  
        Magazine.all.append(self)  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) < 2 or len(value) > 16:
            raise Exception("Name must be between 2 and 16 characters, inclusive.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string.")
        if len(value) == 0:
            raise Exception("Category must be more than 0 characters.")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None


author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")

magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Architecture")

article1 = Article(author_1, magazine_1, "How to wear a tutu with style")
article_2 = Article(author_2, magazine_2, "Dating life in NYC")

author_1.add_article(magazine_1, "How to dye your hair")

print(article_2.title)
print(author_1.articles())
print(author_2.magazines())