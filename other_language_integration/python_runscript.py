"""
Generic python run script to demonstate how one might use subprocess to call a 
binary compiled in another language.
"""

import subprocess

executable = "./exe.x"
report_file = "./execution_report.txt"
input_file = "input_lattice.lat"

def generate_input_file(input_file):

    with open(input_file, 'w') as f:
        f.write('32\n')
        f.write('32\n')
        f.write('32\n')
        f.write('64\n')

if __name__ == '__main__':

    generate_input_file(input_file)
    
    #Run expects the command as a list where a space would separate
    #each argument.
    #Append any additional command line arguments as list items
    #if required.
    command = [executable]
    
    with open(report_file, 'w') as f:
        #Don't need all of the args, I have included them only to give an
        #idea of what is available.
        subprocess.run(command,
                       #Newline character tells the binary to stop reading.
                       #May be language dependent.
                       input=input_file + '\n',
                       #Do input/output in unicode not binary.
                       text=True,
                       stdout=f,
                       stderr=subprocess.STDOUT,
                       timeout=600) #in seconds
            
