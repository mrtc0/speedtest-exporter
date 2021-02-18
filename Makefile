build:
	docker build -t mrtc0/speedtest_exporter:latest .

push:
	docker push mrtc0/speedtest_exporter:latest
