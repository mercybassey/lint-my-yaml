import yaml

def read_and_write_file(input, output):
    with open(f'{input}.yaml', 'r') as f:
        data =  list(yaml.safe_load_all(f))
    print(data)

    with open(f'{output}.yaml', 'w') as file:
        yaml.dump_all(data, file)
    
read_and_write_file('example', 'output')
