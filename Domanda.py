from dataclasses import dataclass


@dataclass
class Domanda:
    testo: str
    difficolta: str
    rispcorretta: str
    errata1 : str
    errata2 : str
    errata3 : str

