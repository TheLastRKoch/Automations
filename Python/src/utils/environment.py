from dotenv import load_dotenv
from os import environ as env


class UtilEnvironment:
    @classmethod
    def get_and_check_variables(self, variable_list):
        load_dotenv()
        variable_dict = {}
        for variable_name in variable_list:
            if env.get(variable_name) is None:
                raise ValueError(f"The env variable {variable_name} could not be empty")
            variable_dict[variable_name] = env.get(variable_name)
        return variable_dict
