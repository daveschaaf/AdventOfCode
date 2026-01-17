import pytest

from day05 import parse_data, seed_to_soil

@pytest.fixture
def sample_data():
    return parse_data('sample_data.dat')

def test_parse_data(sample_data):
    data = sample_data
    assert len(data['seeds']) > 0 
    assert len(data['seed-to-soil']) > 0 
    assert len(data['soil-to-fertilizer']) > 0 
    assert len(data['fertilizer-to-water']) > 0 
    assert len(data['water-to-light']) > 0 
    assert len(data['light-to-temperature']) > 0 
    assert len(data['temperature-to-humidity']) > 0 
    assert len(data['humidity-to-location']) > 0
    assert data['seeds'] == [79, 14, 55, 13]
    assert data['seed-to-soil'] == [[50, 98, 2], [52, 50, 48]]
    assert data['humidity-to-location'] == [[60, 56, 37], [56, 93, 4]]

def test_seed_to_soil(sample_data):
    ratios = sample_data['seed-to-soil']
    assert seed_to_soil(79, ratios) == 81
    assert seed_to_soil(14, ratios) == 14
    assert seed_to_soil(55, ratios) == 57
    assert seed_to_soil(13, ratios) == 81

