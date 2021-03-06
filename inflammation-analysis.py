#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse

from inflammation import models, views


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    in_files = args.infiles
    if not isinstance(in_files, list):
        in_files = [args.infiles]

    for filename in in_files:
        inflammation_data = models.load_csv(filename)
        
        if args.view == 'visualize':

            view_data = {'average': models.daily_mean(inflammation_data),
                        'max': models.daily_max(inflammation_data),
                        'min': models.daily_min(inflammation_data)
                        }

            views.visualize(view_data)
        
        elif args.view == 'record':
            record = inflammation_data[args.patient]
            observations = [models.Observation(day, value) for day,value in enumerate(record)]
            patient = models.Patient('UNKNOWN', observations)
            
            views.display_patient_record(patient)
        
        elif args.view == 'export':
            record = inflammation_data[args.patient]
            observations = [models.Observation(day, value) for day,value in enumerate(record)]
            patient = models.Patient('UNKNOWN', observations)
            
            views.export([patient], 'patient_{}.{}'.format(args.patient,args.serializer), serializer=args.serializer)
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    parser.add_argument('--view', type=str, choices=['visualize', 'record', 'export'], default='visualize', help="What kind of view shoud be used?")

    parser.add_argument('--patient', type=int, default=0, help='Which patient to display.')

    parser.add_argument('--serializer', type=str, choices=['json','csv'], default='json')

    args = parser.parse_args()

    main(args)
