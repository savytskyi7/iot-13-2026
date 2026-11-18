from enum import Enum
from typing import List


# 1. Створення Enum для типу атома
class AtomType(Enum):
    ISOTYPE = "ISOTYPE"
    RADIOACTIVE = "RADIOACTIVE"
    ION = "ION"
    ANTIMATTER = "ANTIMATTER"
    STABLE = "STABLE"


# 2. Клас Atom
class Atom:
    def __init__(
        self,
        name: str = "Unknown",
        atomic_mass_unit: float = 0.0,
        neutrons_number: int = 0,
        protons_number: int = 0,
        electrons_number: int = 0,
        atom_type: AtomType = AtomType.STABLE
    ):
        self.__name = name
        self.__atomic_mass_unit = atomic_mass_unit
        self.__neutrons_number = neutrons_number
        self.__protons_number = protons_number
        self.__electrons_number = electrons_number
        self.__atom_type = atom_type

    def __del__(self):
        # Деструктор (викликається автоматично під час видалення об'єкта з пам'яті)
        pass

    # --- Функції доступу (Getters & Setters) ---
    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_atomic_mass_unit(self) -> float:
        return self.__atomic_mass_unit

    def set_atomic_mass_unit(self, mass: float) -> None:
        if mass >= 0:
            self.__atomic_mass_unit = mass

    def get_neutrons_number(self) -> int:
        return self.__neutrons_number

    def set_neutrons_number(self, neutrons: int) -> None:
        if neutrons >= 0:
            self.__neutrons_number = neutrons

    def get_protons_number(self) -> int:
        return self.__protons_number

    def set_protons_number(self, protons: int) -> None:
        if protons >= 0:
            self.__protons_number = protons

    def get_electrons_number(self) -> int:
        return self.__electrons_number

    def set_electrons_number(self, electrons: int) -> None:
        if electrons >= 0:
            self.__electrons_number = electrons

    def get_atom_type(self) -> AtomType:
        return self.__atom_type

    def set_atom_type(self, atom_type: AtomType) -> None:
        self.__atom_type = atom_type

    # --- Методи за умовою завдання ---
    def isNeutral(self) -> bool:
        """
        Перевіряє умову з завдання: чи рівна кількість нейтронів та електронів.
        """
        return self.__neutrons_number == self.__electrons_number

    # --- Виведення інформації на екран ---
    def __str__(self) -> str:
        return (
            f"Атом: {self.__name:<10} | Маса: {self.__atomic_mass_unit:<7.3f} а.о.м. | "
            f"p+: {self.__protons_number:<2}, n0: {self.__neutrons_number:<2}, e-: {self.__electrons_number:<2} | "
            f"Тип: {self.__atom_type.value:<11} | isNeutral: {self.isNeutral()}"
        )

    def display_info(self) -> None:
        print(self.__str__())


# 3. Клас Molecule
class Molecule:
    def __init__(self, name: str = "Unknown Molecule", atoms: List[Atom] = None):
        self.__name = name
        self.__atoms = atoms if atoms is not None else []

    def __del__(self):
        self.__atoms.clear()

    # --- Функції доступу ---
    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_atoms(self) -> List[Atom]:
        return self.__atoms

    def set_atoms(self, atoms: List[Atom]) -> None:
        self.__atoms = atoms

    def add_atom(self, atom: Atom) -> None:
        self.__atoms.append(atom)

    # --- Сортування атомів за масою ---
    def sort_atoms_by_mass(self, descending: bool = False) -> None:
        self.__atoms.sort(key=lambda atom: atom.get_atomic_mass_unit(), reverse=descending)

    # --- Виведення інформації на екран ---
    def display_info(self) -> None:
        print(f"\n=== Молекула: {self.__name} (Кількість атомів: {len(self.__atoms)}) ===")
        if not self.__atoms:
            print("Молекула не містить атомів.")
            return
        for atom in self.__atoms:
            atom.display_info()


# 4. Функція знаходження середньої маси атомів
def findAverageMass(atoms: List[Atom]) -> float:
    """
    Аналог findAverageMass(Atom*) з C++: приймає список об'єктів Atom
    та повертає їхню середню атомну масу.
    """
    if not atoms:
        return 0.0
    total_mass = sum(atom.get_atomic_mass_unit() for atom in atoms)
    return total_mass / len(atoms)


# 5. Демонстрація роботи у функції main
def main():
    # Створення окремих атомів (на прикладі глюкози та ізотопів)
    h1 = Atom("Hydrogen-1", 1.008, neutrons_number=0, protons_number=1, electrons_number=1, atom_type=AtomType.STABLE)
    h2 = Atom("Deuterium", 2.014, neutrons_number=1, protons_number=1, electrons_number=1, atom_type=AtomType.ISOTYPE)
    c12 = Atom("Carbon-12", 12.011, neutrons_number=6, protons_number=6, electrons_number=6, atom_type=AtomType.STABLE)
    c14 = Atom("Carbon-14", 14.003, neutrons_number=8, protons_number=6, electrons_number=6, atom_type=AtomType.RADIOACTIVE)
    o16_ion = Atom("Oxygen-16", 15.999, neutrons_number=8, protons_number=8, electrons_number=10, atom_type=AtomType.ION)

    # Формування молекули та додавання атомів
    molecule = Molecule("Експериментальна сполука", [c14, h1, o16_ion, c12])
    molecule.add_atom(h2)

    # Виведення початкового стану молекули
    print("--- До сортування ---")
    molecule.display_info()

    # Сортування атомів за зростанням маси
    molecule.sort_atoms_by_mass()
    print("\n--- Після сортування за масою (за зростанням) ---")
    molecule.display_info()

    # Обчислення середньої маси атомів
    avg_mass = findAverageMass(molecule.get_atoms())
    print(f"\nСередня маса атомів у молекулі: {avg_mass:.3f} а.о.м.")

    # Демонстрація роботи сетерів та перевірки isNeutral()
    print("\n--- Перевірка методів доступу та isNeutral() ---")
    print(f"Початковий стан {o16_ion.get_name()}: електронів = {o16_ion.get_electrons_number()}, isNeutral = {o16_ion.isNeutral()}")
    o16_ion.set_electrons_number(8)
    o16_ion.set_atom_type(AtomType.STABLE)
    print(f"Після зміни {o16_ion.get_name()}: електронів = {o16_ion.get_electrons_number()}, isNeutral = {o16_ion.isNeutral()}")


if __name__ == "__main__":
    main()