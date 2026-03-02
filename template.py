import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "my_project"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py"
    f"src/{project_name}/pipelines/prediction_pipeline.py"
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    
]

def create_directories(path_list):
    for path in path_list:
        file_path = Path(path)
        file_dir, file_name = os.path.split(file_path)

        if file_dir != "":
            os.makedirs(file_dir, exist_ok=True)
            logging.info(f"Directory created: {file_dir} for the file {file_name}")

        if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
            with open(file_path, "w") as f:
                pass
            logging.info(f"File created: {file_path}")
        else:
            logging.info(f"File already exists: {file_path}")

if __name__ == "__main__":
    create_directories(list_of_files)