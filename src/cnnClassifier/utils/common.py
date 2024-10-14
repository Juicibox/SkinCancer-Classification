import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json 
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object

    Args:
        path_to_yaml (str): Path to the yaml file

    Raises:
        ValueError: If the yaml file is empaty

    Returns:
        ConfigBox: A ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Reading the yaml file from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"The yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directiories: list, verbose=True):
    """
    Create a list of directories

    Args:
        path_to_directiories (list): List of directories to create
        ignore_log (bool, optional): Ignore the log. Defaults to True.
    """
    for path in path_to_directiories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save a json file

    Args:
        Path (Path): Path to json file
        data (dict): Data to save
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"Json file saved at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load a json file

    Args:
        path (Path): Path to json file

    Returns:
        ConfigBox: A ConfigBox type
    """
    with open(path) as f:
        content = json.load(f)
        
    logger.info(f"Json file loaded from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path: Path):
    """
    Save a binary file

    Args:
        data (Any): Data to save
        path (Path): Path to save
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load a binary file

    Args:
        path (Path): Path to load

    Returns:
        Any: Data loaded
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file

    Args:
        path (Path): Path to the file

    Returns:
        str: Size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"~{size_in_kb} kb"


def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

