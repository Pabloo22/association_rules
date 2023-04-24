# -*- coding: utf-8 -*-
import os
import pandas as pd
import dotenv


def setup_project():
    """ Setup project path and load environment variables """
    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    project_path = dotenv.get_key(dotenv.find_dotenv(), "project_path")
    os.chdir(project_path)


def get_raw_data(filename: str = "movies"):
    setup_project()
    return pd.read_csv(f"data/raw/{filename}.csv")


if __name__ == '__main__':
    pass
