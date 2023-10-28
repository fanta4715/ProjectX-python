import time
import json

class DummySensor:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": 0,
            "mars_base_external_temperature": 0,
            "mars_base_internal_humidity": 0,
            "mars_base_external_illuminance": 0,
            "mars_base_internal_co2": 0,
            "mars_base_internal_oxygen": 0
        }

    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = round(random.uniform(18, 30), 2)
        self.env_values["mars_base_external_temperature"] = round(random.uniform(0, 21), 2)
        self.env_values["mars_base_internal_humidity"] = round(random.uniform(50, 60), 2)
        self.env_values["mars_base_external_illuminance"] = round(random.uniform(500, 715), 2)
        self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 2)
        self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4, 7), 2)

    def get_env(self):
        return self.env_values
#파이썬은 클래스에 속성(변수)과 메소드를 정의할 수 있음.
class MissionComputer:
    #파이썬의 생성자에 해당
    #파이썬에서는 인스턴스 변수를 사용하기 위해서는 self.을 붙여야함
    def __init__(self):
        self.env_values = {}
        # 더미클래스 -> ds로 인스턴스
        self.ds = DummySensor()

    def get_sensor_data(self):
        while True:
            self.env_values = self.ds.read_sensor_data()
            print(json.dumps(self.env_values, indent=4))
            time.sleep(5)

if __name__ == "__main__":
    run_computer = MissionComputer()
    run_computer.get_sensor_data()
