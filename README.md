# probleme-3-coloration


## Installation.

For this project you will need a python3 version.

You will need the following package:
    
    sudo apt install python3
    sudo apt install virtualenv
    sudo apt install python3-pip
    sudo apt install python3-tk
 
Prepare your virtualenv:

    virtualenv venv
    . venv/bin/activate
    pip install -r requirements.txt   

If you want to exit your virtualenv:

    deactivate

## Usage

### Run Specific algorithm

If you want to test a specific algorithm you can enter the following command

    python game_dynamic.py list_point_file.txt --min-dist-bade  
    python game_dynamic.py board_file.txt --min-dist-fast  
    
In this 2 command we will execute the algorithm of the question a) and b)

### Run a time measure

If you want to do a time measure of a specific algorithm you can do the following command

    python game_dynamic.py list_point_file.txt --min-dist-bade --time-measure="100 1000 10"

This command will execute the algorithm of the question a). The start length will be 100 and the end length will be 1000
then we will increment the size of the list by 10

**Note** In this case the input file **list_point_file.txt** will be not used.
