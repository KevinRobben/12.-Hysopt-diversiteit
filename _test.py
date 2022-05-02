import json
import os
import unittest
from app import change, save_data, get_data


class test_app(unittest.TestCase):

    @unittest.skip
    def test_data_loading(self):
        data = get_data("sudcal-future-situation.json")
        data = json.loads(data['simulationModel'])
        save_data("sudcal-future-situation.json", json.dumps(data))

    def test_sudcal(self):
        data = get_data("boomstructuur.json")

        data = change(data, 0.6)

        save_data("boomstructuur.json", str(json.dumps(data)))


if __name__ == "__main__":
    print("starting tests...")
    unittest.main()
