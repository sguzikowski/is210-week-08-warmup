#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A wonderful docstring."""

BP_STATUS = raw_input('What is your blood pressure? ')
BP_STATUS = int(BP_STATUS)

if BP_STATUS == 89:
	STATUS = 'Low'
elif 90 <= BP_STATUS <= 119:
	STATUS = 'Ideal'
elif 120 <= BP_STATUS <= 139:
	STATUS = 'Warning'
elif 140 <= BP_STATUS <= 159:
	STATUS = 'High'
else:
        BP_STATUS == 160
        STATUS = 'Emergency'

BLOOD_STATUS = 'Your status is currently: {} !'.format(STATUS)
print BLOOD_STATUS
