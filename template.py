import os
from pathlib import Path


list_of_files = [
   ".github/workflows/ci.yaml",
   
   "src/__init__.py",
   "src/components/__init__.py", 
   "src/components/data_ingestion.py", 
   "src/components/data_transformation.py", 
   "src/components/model_evaluation.py", 
   "src/components/model_trainer.py", 
   "src/exception/unit/__init__.py",
   "src/exception/unit/exception.py",
   "src/logger/__init__.py",
   "src/logger/app_logging.py",
   "src/pipeline/__init__.py",
   "src/pipeline/prediction_pipeline.py",
   "src/pipeline/training.pipeline.py",
   "src/utils/__init__.py",
   "src/utils/utils.py",
   
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   
   "experiments/experiments.ipynb", 
   
   "artifacts/",
   
   "templates/form.html",
   "templates/index.html",
   "templates/result.html",
   
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt", 
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "app.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file

#its updated