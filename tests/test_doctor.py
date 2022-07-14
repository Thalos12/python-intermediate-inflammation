
def test_create_doctor():
    from inflammation.models import Doctor
    name = 'Lucas'
    d = Doctor(name, None)
    assert d.name == name


def test_doctor_day_observation():
    from inflammation.models import Doctor, Patient
    p1 = Patient('Alice')
    p1.add_observation(3)
    p1.add_observation(4)
    p1.add_observation(2)
    p1.add_observation(2)
    
    p2 = Patient('Anthony')
    p2.add_observation(1)
    p2.add_observation(1)
    p2.add_observation(3)
    
    d = Doctor('Lucas', [p1,p2])
    observations = d.get_day_observations(2)
    assert [o.value for o in observations] == [4,1]
    

def test_doctor_day_observation_missing():
    from inflammation.models import Doctor, Patient
    p1 = Patient('Alice')
    p1.add_observation(3)
    p1.add_observation(4)
    p1.add_observation(2)
    p1.add_observation(2)
    
    p2 = Patient('Anthony')
    p2.add_observation(1)
    p2.add_observation(1)
    p2.add_observation(3)
    
    d = Doctor('Lucas', [p1,p2])
    observations = d.get_day_observations(4)
    assert [o.value for o in observations] == [2,None]