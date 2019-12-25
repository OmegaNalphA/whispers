.PHONY: all

all: build

build:
	source venv/bin/activate;
	pip install --editable .

clean:
	rm -rf __pycache__
	rm -rf whispers.egg-info

requirements:
	pip freeze > requirements.txt