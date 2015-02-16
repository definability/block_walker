#!/bin/bash

coverage run -m tests.classes.point
mv .coverage .coverage.point
coverage run -m tests.classes.game_object
mv .coverage .coverage.game_object
coverage run -m tests.classes.singleton
mv .coverage .coverage.singleton
coverage combine
#coverage html
coverage report --show-missing
