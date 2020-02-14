from flask_script import Manager

from flask_alembic import ManageMigrations



manager = Manager(app)

manager.add_command("migrate", ManageMigrations())



if __name__ == "__main__":

        manager.run()
