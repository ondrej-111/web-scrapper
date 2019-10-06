working_dir = echo pwd

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages:
	sudo apt install python-pip -y
	pip install virtualenv --user

activate:
	source ./venv/bin/activate

python-packages:
	activate
	pip install -r requirements.txt

install:
	system-packages python-packages
    Working direction: $PWD


run:
	gunicorn --bind 127.0.0.1:5000 wsgi:app --workers 4 --threads=4 --worker-connections=100


wd: $(working_dir)

deploy:
	gcloud app deploy