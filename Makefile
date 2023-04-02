static:
	docker compose up -d --build
	docker exec eshop-api python -m manage collectstatic
	docker compose down
upd:
	docker compose up -d
up:
	docker compose up
down:
	docker compose down