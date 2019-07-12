import os

def reads_input_data(file_name):
    input_data = set()
    file_input = open(file_name, 'r')
    input_data.update(file_input.readlines())
    file_input.close()
    return input_data

def write_output_data(file_name, output_data):
    home = os.path.expanduser('~')
    base_path_out = home+'/data/out/'
    file_output = open(base_path_out+file_name+'.done.dat', 'w')
    file_output.write(output_data)
