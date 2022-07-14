from inflammation import models, serializers

def test_patients_json_serializers():
    """Test the serializers."""
    # Create fake data
    patients = [
        models.Patient('Adam', [models.Observation(i,i+1) for i in range(3)]),
        models.Patient('Luna', [models.Observation(i,i*i) for i in range(3)])
    ]
    
    # Write to file
    output_file = 'patients.json'
    serializers.PatientSerializerJSON.save(patients, output_file)
    
    # Read from file
    patients_new = serializers.PatientSerializerJSON.load(output_file)
    # Check that we loaded the same as we wrote
    for p1, p2 in zip(patients, patients_new):
        assert p1 == p2
