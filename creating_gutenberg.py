from src.app.project_setup import ProjectSetup

setup = ProjectSetup()

setup.create_combs()

setup.create_datasets(10, 5, 115)