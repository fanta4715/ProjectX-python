import time
import json
import platform
import psutil

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
            self.env_values = self.ds.get_env()
            print(json.dumps(self.env_values, indent=4))
            time.sleep(5)
    # 가져온 시스템 정보를 JSON으로 출력하는 함수
    # 운영체계, 버전, CPU타입, CPU코어 수, 메모리 크기
    def get_mission_computer_info(self):
        system_info = {
            "운영체계": platform.system(),
            "운영체계 버전": platform.release(),
            "CPU 타입": platform.machine(),
            "CPU 코어 수": psutil.cpu_count(logical=False),
            "메모리 크기 (bytes)": psutil.virtual_memory().total,
        }
        return json.dumps(system_info, indent=4,ensure_ascii = False)

    # 실시간 CPU사용량과 메모리 사용량 -> JSON으로 출력하는 함수
    def get_mission_computer_load(self):
        try:
            import psutil
            cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
            memory_percent = psutil.virtual_memory().percent

            load_info = {
                "CPU 실시간 사용량": cpu_percent,
                "메모리 실시간 사용량": memory_percent
            }
            return json.dumps(load_info, indent=4, ensure_ascii = False)
        except ImportError:
            return "파이썬 라이브러리 'psutil'을 설치해야 합니다."


if __name__ == "__main__":
    run_computer = MissionComputer()
    # 시스템 정보 출력
    system_info = run_computer.get_mission_computer_info()
    print("시스템 정보:")
    print(system_info)

    # 부하 정보 출력
    load_info = run_computer.get_mission_computer_load()
    print("\n부하 정보:")
    print(load_info)
