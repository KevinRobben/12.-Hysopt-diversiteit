

from email.mime import base
import json
import os


script_dir = os.path.dirname(__file__)
testdata_path = "unit_test data"
testoutput_path = "unit_test data/output"


def get_data(path):
    p = os.path.join(script_dir, testdata_path, path)
    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def save_data(path, data: str):
    p = os.path.join(script_dir, testoutput_path, path)
    with open(p, "w") as f:
        f.write(data)


def change(data: dict, diversity: float):
    simulationModel = json.loads(data['simulationModel'])

    for floorPlan in simulationModel['floorPlans']:
        for baseCircuit in floorPlan['pipes']['baseCircuits']:

            if baseCircuit['typeName'] in ['DynamicRadiator', 'DynamicZonelessRadiator', 'FloorHeatingLoop']:
                for parameter in baseCircuit['parameters']:
                    if parameter['name'] == "designHeatFlow":
                        parameter['value'] = str(int(
                            float(parameter['value']) * diversity))

            if baseCircuit['typeName'] in ['ProductionParallel']:
                for parameter in baseCircuit['parameters']:
                    if parameter['name'] == "parallelProductionPrimaryHeatFlow":
                        parameter['value'] = str(int(
                            float(parameter['value']) * diversity))

    data['simulationModel'] = str(json.dumps(
        simulationModel, ensure_ascii=False))

    return data


def main():
    phase = 0

    while phase == 0:
        try:
            print('Enter filename in unit_test data folder')
            name = input()
            data = get_data(name)
        except Exception:
            print("file not found (press crtl+c to exit)")
        else:
            phase = 1

    while phase == 1:
        try:

            print('Enter diversity factor')
            divesity = input()
            divesity = float(divesity)
            if divesity > 1 or divesity < 0:
                raise ValueError

        except Exception:
            print("factor not a number or out of range (press crtl+c to exit)")
        else:
            phase = 2

    data = change(data, divesity)
    save_data(name, str(json.dumps(data)))

    print("succes, see unit_test data/output/" + name)


if __name__ == "__main__":
    print("starting tests...")
    main()
