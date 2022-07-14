"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name


def test_add_observation():
    from inflammation.models import Patient
    
    p = Patient('alice')
    
    observation = 3
    
    obs = p.add_observation(observation)
    
    assert p.last_observation.value == observation

