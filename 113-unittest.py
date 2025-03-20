import unittest

from testando_func import formando_nome

class TesteNome(unittest.TestCase):
    """usando ferramente de testes"""
    def test_first_last_name(self):
        """nomes como Janis Joplin funcionam?"""
        formated_name = formando_nome('Janis', 'Joplin')
        self.assertEqual(formated_name, 'Janisgfnhhfgdnfgdnfg Joplin')

unittest.main()