# this is the topmost __init__.py file of the mrmustard package

import importlib
from rich.pretty import install  # NOTE: just for the looks
install()
from rich.table import Table
from rich import print as rprint

__version__ = "0.1.0"


class Settings:
    def __init__(self):
        self._backend = "tensorflow"
        self.HBAR = 2.0
        self.CHOI_R = 0.881373587019543  # np.arcsinh(1.0)
        self.DEBUG = False
        # mean + 5*std when estimating the Fock cutoff for a Gaussian state
        self.AUTOCUTOFF_STDEV_FACTOR = 5
        self.AUTOCUTOFF_MAX_CUTOFF = 100
        self.AUTOCUTOFF_MIN_CUTOFF = 1
        # using cutoff=5 for each mode when determining if two transformations or states in fock repr are equal
        self.EQ_CUTOFF = 5
        self.EQ_RTOL_FOCK = 1e-4
        self.EQ_RTOL_GAUSS = 1e-6

    @property
    def BACKEND(self):
        return self._backend

    @backend.setter
    def BACKEND(self, backend_name: str):
        if backend_name not in ["tensorflow", "pytorch"]:
            raise ValueError("Backend must be either 'tensorflow' or 'pytorch'")
        self._backend = backend_name

    def __repr__(self) -> str:
        table = Table(title="Settings")
        table.add_column("Setting", style="bold")
        table.add_column("Value", style="bold")
        table.add_row("Backend", self.BACKEND)
        table.add_row("HBAR", self.HBAR)
        table.add_row("CHOI_R", self.CHOI_R)
        table.add_row("DEBUG", self.DEBUG)
        table.add_row("AUTOCUTOFF_STDEV_FACTOR", self.AUTOCUTOFF_STDEV_FACTOR)
        table.add_row("AUTOCUTOFF_MAX_CUTOFF", self.AUTOCUTOFF_MAX_CUTOFF)
        table.add_row("AUTOCUTOFF_MIN_CUTOFF", self.AUTOCUTOFF_MIN_CUTOFF)
        table.add_row("EQ_CUTOFF", self.EQ_CUTOFF)
        table.add_row("EQ_RTOL_FOCK", self.EQ_RTOL_FOCK)
        table.add_row("EQ_RTOL_GAUSS", self.EQ_RTOL_GAUSS)
        rprint(table)
        return ""


settings = Settings()
settings.BACKEND = "tensorflow"
