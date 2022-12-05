import pytest
from fe_gui_beta import *


def test_get_uibc_variable_results():
    '''
        Verify that the get_uibc_variable_results function works correctly.
        Parameters: none
        Return: uibc, control_uibc
    '''
    assert get_uibc_variable_results(0.296,0.360,0.436) == (321,174)
    assert get_uibc_variable_results(0.307,0.380,0.447) == (313,150)


def test_get_iron_variable_results():
    '''
        Verify that the get_iron_variable_results function works correctly.
        Parameters: none
        Return: total_serum_iron, control_total_serum_iron
    '''
    assert get_iron_variable_results(0.245,0.024,0.399) == (614,60)
    assert get_iron_variable_results(0.283,0.055,0.519) == (545,106)



pytest.main(["-v", "--tb=line", "-rN", __file__])