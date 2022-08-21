from config import app
from views.home_controller import HomeController
from views.employees_controller import EmployeesController
from views.users_controller import UsersController


if __name__ == '__main__':
    hc = HomeController()
    nc = EmployeesController()
    uc = UsersController()
    app.run(debug=True)
