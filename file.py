import yaml

def read_file(input_filename):
    try:
        with open(f'{input_filename}.yaml', 'r') as f:
            data = list(yaml.safe_load_all(f))
            return data
    except (FileNotFoundError, yaml.YAMLError):
        print(f"Error: No valid YAML or YAML file found for '{input_filename}'.")
        return None

def write_file(output_filename, data):
    try:
        with open(f'{output_filename}.yaml', 'w') as file:
            yaml.dump_all(data, file)
    except (FileNotFoundError, yaml.YAMLError):
        print(f"Error: Unable to write YAML data to '{output_filename}'.")
    
def read_and_write_file(input_filename, output_filename):
    data = read_file(input_filename)

    if data:
        write_file(output_filename, data)
        print(f'Done! Contents of {input_filename} written to {output_filename}')

read_and_write_file('example', 'output')




