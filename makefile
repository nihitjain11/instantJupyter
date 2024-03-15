notebook:
	docker-compose up -d
	sleep 10
	bash -c "echo -e '\nTo access the server, open one of these URLs in a browser:\n'"
	docker-compose logs | grep -Eo '(http|https)://.*'
	open -a 'Google Chrome' http://localhost:10000`docker-compose logs | grep -Eo '/lab\?.*' | uniq`
	echo "To stop the server, run 'make stop'"
stop:
	docker-compose down --remove-orphans