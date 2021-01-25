from nr_czmesh import get_tree_number


def test_get_tree_number():
    record_dict = {
        '001': 'D000002', '003': 'CZ-PrNML', '005': '20200331', '008': '990101#n#ancnnbaba###########a#ana#####d',
        '035': {'a': '(DNLM)D000002'}, '040': {'a': 'ABA008', 'b': 'cze'},
        '150': {'a': 'abat', 'x': 'zásobování a distribuce', '2': 'czmesh'},
        '450': [{'w': 'i', 'a': 'Abate', 'i': 'UF'}, {'w': 'i', 'a': 'Difos', 'i': 'UF'},
                {'w': 'i', 'a': 'Temephos', 'i': 'UF'}], '550': [{'w': 'g', 'a': 'organothiofosfáty', '7': 'D063086'}, {
            'w': 'i', 'a': 'insekticidy', 'i': 'PA', '7': 'D007306'
        }], '667': {
            'a': 'for use to kill or control insects, use no qualifiers on the insecticide or the insect;'
                 ' appropriate qualifiers may be used when other aspects of the insecticide are discussed such as the '
                 'effect on a physiologic process or behavioral aspect of the insect; for poisoning, coordinate with '
                 'ORGANOPHOSPHATE POISONING'
        }, '680': {'i': 'An organothiophosphate insecticide.'},
        '686': [{'a': 'D02.705.400.625.800'}, {'a': 'D02.705.539.345.800'}, {'a': 'D02.886.300.692.800'}],
        '688': {'a': '96; was ABATE 1972-95 (see under INSECTICIDES, ORGANOTHIOPHOSPHATE 1972-90)'},
        '750': {'a': 'Temefos', '7': 'D000002'}, 'BAS': {'a': 'MeSH2020'}, 'MSH': {
            'a': '1', 'b': 'M0000002', 'd': 'Y', 'i': 'Insecticides (1966-1971)',
            'p': '96; was ABATE 1972-95 (see under INSECTICIDES, ORGANOTHIOPHOSPHATE 1972-90)', 'r': 'ONP3ME32DL',
            's': "Phosphorothioic acid, O,O'-(thiodi-4,1-phenylene) O,O,O',O'-tetramethyl ester"
        }
    }
    assert get_tree_number(record_dict) == (
    ['TreeNumberList_0', 'TreeNumberList_1', 'TreeNumberList_2', 'TreeNumberList_3', 'TreeNumberList_4',
     'TreeNumberList_5', 'TreeNumberList_6', 'TreeNumberList_7', 'TreeNumberList_8', 'TreeNumberList_9',
     'TreeNumberList_10', 'TreeNumberList_11', 'TreeNumberList_12', 'TreeNumberList_13', 'TreeNumberList_14'],
    ['D02', 'D02.705', 'D02.705.400', 'D02.705.400.625', 'D02.705.400.625.800', 'D02', 'D02.705', 'D02.705.539',
     'D02.705.539.345', 'D02.705.539.345.800', 'D02', 'D02.886', 'D02.886.300', 'D02.886.300.692',
     'D02.886.300.692.800'])
