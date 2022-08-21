from flask import Flask
from config import app
from views.home_controller import HomeController
from views.news_controller import NewsController
from views.users_controller import UsersController


if __name__ == '__main__':
    hc = HomeController()
    nc = NewsController()
    uc = UsersController()
    app.run()
