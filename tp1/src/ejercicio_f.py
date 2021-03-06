# -*- coding: utf-8 -*-
#!/usr/bin/python
from non_deterministic_finite_automata import *

def equivalentes(archivo_automata1, archivo_automata2, file = sys.stdout):
    auto1 = DeterministicFiniteAutomata.from_automata_file(archivo_automata1)
    auto2 = DeterministicFiniteAutomata.from_automata_file(archivo_automata2)

    file.write('TRUE' if auto1.equivalent(auto2) else 'FALSE')
