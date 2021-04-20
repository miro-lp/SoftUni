from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        h_n_l = [h for h in System._hardware if hardware_name == h.name]
        if len(h_n_l) == 0:
            return "Hardware does not exist"
        express_soft = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            h_n_l[0].install(express_soft)
            System._software.append(express_soft)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        h_n_l = [h for h in System._hardware if hardware_name == h.name]
        if len(h_n_l) == 0:
            return "Hardware does not exist"
        express_soft = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            h_n_l[0].install(express_soft)
            System._software.append(express_soft)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        h_n_l = [h for h in System._hardware if hardware_name == h.name]
        s_n_l = [s for s in System._software if software_name == s.name]
        if len(h_n_l) == 0 or len(s_n_l) == 0:
            return "Some of the components do not exist"
        h_n_l[0].uninstall(s_n_l[0])
        System._software.remove(s_n_l[0])

    @staticmethod
    def analyze():
        text_analyze = "System Analysis" + "\n"
        text_analyze += f"Hardware Components: {len(System._hardware)}" + "\n"
        text_analyze += f"Software Components: {len(System._software)}" + "\n"
        text_analyze += f"Total Operational Memory: {sum([s.memory_consumption for s in System._software])} / {sum([h.memory for h in System._hardware])}" + "\n"
        text_analyze += f"Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])} / {sum([h.capacity for h in System._hardware])}"
        return text_analyze

    @staticmethod
    def system_split():
        sys_split_text = ""
        for h in System._hardware:
            sys_split_text += f"Hardware Component - {h.name}" + "\n"
            sys_split_text += f"Express Software Components: {len([s for s in h.software_components if s.__class__.__name__ == 'ExpressSoftware'])}" + "\n"
            sys_split_text += f"Light Software Components: {len([s for s in h.software_components if s.__class__.__name__ == 'LightSoftware'])}" + "\n"
            sys_split_text += f"Memory Usage: {sum([s.memory_consumption for s in h.software_components])} / {h.memory}" + "\n"
            sys_split_text += f"Capacity Usage: {sum([s.capacity_consumption for s in h.software_components])} / {h.capacity}" + "\n"
            sys_split_text += f"Type: {h.type}" + "\n"
            sft_comp = [s.name for s in h.software_components]
            if len(sft_comp) == 0:
                sys_split_text += "Software Components: None"
            else:
                sys_split_text += f"Software Components: {', '.join(sft_comp)}"
        return sys_split_text

