import abc
import csv
import json

from inflammation import models


class Serializer(abc.ABC):
    @abc.abstractclassmethod
    def serialize(cls, instances):
        pass

    @abc.abstractclassmethod
    def save(cls, instances, path):
        pass

    @abc.abstractclassmethod
    def deserialize(cls, data):
        pass

    @abc.abstractclassmethod
    def load(cls, path):
        pass
    

class ObservationSerializer(Serializer):
    model = models.Observation
    
    @classmethod
    def serialize(cls, instances):
        return [
            {'day':instance.day, 'value':instance.value}
            for instance in instances
        ]
    
    @classmethod
    def deserialize(cls, data):
        return [cls.model(**d) for d in data]


class PatientSerializer(Serializer):
    model = models.Patient

    @classmethod
    def serialize(cls, instances):
        return [
            {"name": instance.name, "observations": ObservationSerializer.serialize(instance.observations)}
            for instance in instances
        ]

    @classmethod
    def deserialize(cls, data):
        instances = []
        
        for item in data:
            item['observations'] = ObservationSerializer.deserialize(item.pop('observations'))
            # instances.append(cls.model(**item))
        return [cls.model(**d) for d in data]


class PatientSerializerJSON(PatientSerializer):
    model = models.Patient

    @classmethod
    def save(cls, instances, path):
        with open(path, 'w') as f:
            json.dump(cls.serialize(instances), f)

    @classmethod
    def load(cls, path):
        with open(path, 'r') as f:
            data = json.load(f)
        return cls.deserialize(data)


class PatientSerializerCSV(PatientSerializer):
    model = models.Patient

    @classmethod
    def save(cls, instances, path):
        with open(path, 'w') as f:
            writer = csv.writer(f, doublequote=True)
            for elem in cls.serialize(instances):
                writer.writerow([elem['name']] + [o['value'] for o in elem['observations']])

    @classmethod
    def load(cls, path):
        with open(path, 'r') as f:
            reader = csv.reader(f)
            patients = []
            for line in reader:
                name = line.pop(0)
                observations = []
                for i,v in enumerate(line):
                    observation = models.Observation(day=i, value=int(v))
                    observations.append(observation)
                patient = models.Patient(name, observations)
                patients.append(patient)
        return patients
