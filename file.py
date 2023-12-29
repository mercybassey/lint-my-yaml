import yaml

def read_and_write_file(input, output):
    try:
        with open(f'{input}.yaml', 'r') as f:
            data =  list(yaml.safe_load_all(f))
        with open(f'{output}.yaml', 'w') as file:
            yaml.dump_all(data, file)
    except (FileNotFoundError, yaml.YAMLError):
        print(f"Error: No valid YAML or YAML file found for '{input}'.") 
    
read_and_write_file('example', 'output')


