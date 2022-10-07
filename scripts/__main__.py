import json
from json.tool import main
from jinja2 import Environment, FileSystemLoader

def load_json_data_from_file(file_path):
    """
        A compléter ....
    """
    print(file_path + "\n" + file_path)  
    pass


def load_yaml_data_from_file(file_path):
    """
        A compléter ....
    """
    pass


def render_network_config(template_name, data):
    """
        A compléter ....
    """
    pass


def save_built_config(file_name, data):
    """
        A compléter ....
    """
    pass


if __name__ == "__main__":

    env = Environment(loader=FileSystemLoader("templates"))
    f = open('data/lyon_r01.json') # Opening JSON file
    data = json.load(f) # returns JSON object as a dict
    template = env.get_template("config_lyon_r01.j2")
    print(template.render(data))

    file_path= "hello world"
    load_json_data_from_file(file_path)
    pass

