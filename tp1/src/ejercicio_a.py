# -*- coding: utf-8 -*-
#!/usr/bin/python
from non_deterministic_finite_automata import *

def afd_minimo(archivo_regex, archivo_automata):
	NonDeterministicFiniteAutomata.from_file(archivo_regex).determinize().print_automata(archivo_automata)
