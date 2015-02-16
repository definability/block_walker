#!/bin/bash

coverage run -m tests.classes.game.point
mv .coverage .coverage.point
coverage run -m tests.classes.util.singleton
mv .coverage .coverage.singleton
coverage run -m tests.classes.graphics.drawer
mv .coverage .coverage.abstract_drawer
coverage run -m tests.classes.game.game_object
mv .coverage .coverage.game_object
coverage combine
#coverage html
coverage report --show-missing
