#!/usr/bin/python3

import os

start = {"E": 0, "W": 0, "N": 0, "S": 0}
waypoint = {"E": 10, "W": 0, "N": 1, "S": 0}


def parse_input(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path + '/' + filename, 'r')
    content = f.readlines()
    output = []

    for command in content:
        command = command.strip()
        if command == "R270":
            command = "L90"
        if command == "L270":
            command = "R90"

        output.append((command[:1], command[1:]))

    return output


def rotate_coordinates(by, direction, obj):
    rotated = {}

    if by == "180":
        rotated["E"] = obj["W"]
        rotated["W"] = obj["E"]
        rotated["S"] = obj["N"]
        rotated["N"] = obj["S"]
    elif by == "90" and direction == "R":
        rotated["S"] = obj["E"]
        rotated["E"] = obj["N"]
        rotated["W"] = obj["S"]
        rotated["N"] = obj["W"]
    else:
        rotated["W"] = obj["N"]
        rotated["S"] = obj["W"]
        rotated["E"] = obj["S"]
        rotated["N"] = obj["E"]
    
    return rotated


def transform_coordinates(obj):
    if obj["E"] >= obj["W"]:
        obj["E"] = obj["E"] - obj["W"]
        obj["W"] = 0
    if obj["W"] > obj["E"]:
        obj["W"] = obj["W"] - obj["E"]
        obj["E"] = 0
    if obj["N"] >= obj["S"]:
        obj["N"] = obj["N"] - obj["S"]
        obj["S"] = 0
    if obj["S"] > obj["N"]:
        obj["S"] = obj["S"] - obj["N"]
        obj["N"] = 0
    return obj

    
def execute_move(wp, pos, command):
    if command[0] in ["R", "L"]:
        wp = rotate_coordinates(command[1], command[0], wp)
        
    if command[0] in ["E", "W", "S", "N"]:
        wp[command[0]] += int(command[1])
        
    if command[0] == "F":
        for coordinate in wp:
            pos[coordinate] += int(command[1]) * wp[coordinate]
    
    return wp, pos
    

if __name__ == "__main__":
    data = parse_input('input.txt')
    output = 0 
    
    for move in data:
         current = execute_move(waypoint, start, move)
         waypoint = current[0]
         start = current[1]
         print(start['E']-start['W'],start['N']-start['S'], waypoint['E']-waypoint['W'], waypoint['N']-waypoint['S'])

        
    for key in transform_coordinates(start):
        output += start[key]
    
    print(output)

