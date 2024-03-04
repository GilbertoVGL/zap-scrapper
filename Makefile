build_and_run:
	docker container rm scrapper
	docker build -t zap-scrapper .
	docker run --name scrapper zap-scrapper

build:
	docker build -t zap-scrapper .

run:
	docker run --name scrapper zap-scrapper

start:
	docker start scrapper
