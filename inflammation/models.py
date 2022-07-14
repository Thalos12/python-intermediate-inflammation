"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: A Numpy array containing inflammation data.
    :returns: An array of daily mean values."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: A Numpy array containing inflammation data.
    :returns: An array of daily maximum values."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: A Numpy array containing inflammation data.
    :returns: An array of daily minimum values."""
    return np.min(data, axis=0)


def patient_normalize(data):
    """Normalize patients data from a 2D inflammation array."""
    if not isinstance(data, np.ndarray):
        raise TypeError("Inflammation data should be a Numpy array.")
    if np.any(data<0):
        raise ValueError("Inflammation data should not be nagative.")
    if not data.ndim == 2:
        raise ValueError("Inflammation data should be a 2D array.")
    data[~np.isfinite(data)] = 0
    max_data = np.max(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_data[:, np.newaxis]
    normalised[~np.isfinite(normalised)] = 0
    # normalised[np.isnan(normalised)] = 0
    normalised[normalised<0] = 0
    return normalised


def attach_names(data, names):
    """Assign patients' names to their inflammatory data.

    :param data: Inflammatory data provided as 2D Numpy array
    :param names: Iterable with the names of the patients.
    :raises ValueError: When the wrong number of names/patients' data is provided.
    :returns: A list of dictionaries containing patients' names and inflammatory data."""
    if len(data) != len(names):
        raise ValueError("The number of patients does not match that of the names.")
    patients = []
    for d,n in zip(data,names):
        patient = {'name':n, 'data':d}
        patients.append(patient)
    return patients


class Observation():
    def __init__(self, day, value) -> None:
        self.day=day
        self.value=value
    
    def __str__(self):
        return "On day {} inflammation value is {}".format(self.day, self.value)
    
    def __repr__(self):
        return "{}:{}".format(self.day, self.value)

    def __eq__(self, other):
        return self.day==other.day and self.value==other.value

class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    def __str__(self):
        return self.name

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name, observations=None):
        super().__init__(name)
        self.observations = []
        if observations is not None:
            self.observations = observations
    
    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1
            except IndexError:
                day = 0
        observation = Observation(day, value)
        self.observations.append(observation)
        return observation

    @property
    def last_observation(self):
        # return self.observations[-1]
        try:
            return self.observations[-1]
        except IndexError:
            print("No observations for", self.name)
    
    def __eq__(self,other):
        return self.name==other.name and self.observations==other.observations
    
    def __str__(self):
        return "{}: {}".format(self.name, self.observations)


class Doctor(Person):
    """A doctor with patients."""
    def __init__(self, name, patients) -> None:
        super().__init__(name)
        self.patients = patients
    
    def get_day_observations(self, day):
        """Get observations for all patients on the given day"""
        observations = []
        idx=day-1 # zero based indexing
        for patient in self.patients:
            try:
                o = patient.observations[idx]
            except IndexError:
                o = Observation(day, None)
            observations.append(o)
        return observations