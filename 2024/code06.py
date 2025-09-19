
class LabMap():
    def __init__(self, file_name: str):
        self.map = self.parse_map(file_name)

    def parse_map(self, file_name: str) -> list[list[str]]:
        map: list[list[str]] = []
        with open(file_name, 'r') as file:
            for line in file:
                line = str(line).replace("\n","")
                map.append(list(line))
        return map

    def __repr__(self) -> str:
        display = self.map
        for line in display:
            line.append("\n")

        return "\n"+"".join(["".join(line) for line in display])
