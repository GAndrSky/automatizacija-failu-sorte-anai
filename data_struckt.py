from dataclasses import dataclass, field
from typing import List, Dict
import os

@dataclass
class Fails:
    nosaukums: str
    cels: str
    kategorija: str

@dataclass
class Failsisteme:
    kategorijas: Dict[str, List[Fails]] = field(default_factory=dict)

    def pievienot(self, fails: Fails):
        if fails.kategorija not in self.kategorijas:
            self.kategorijas[fails.kategorija] = []
        self.kategorijas[fails.kategorija].append(fails)

    def paradit_kopsavilkumu(self):
        for kategorija, faili in self.kategorijas.items():
            print(f"{kategorija.upper()}: {len(faili)} faili")
            for f in faili:
                print(f"  - {f.nosaukums}")
