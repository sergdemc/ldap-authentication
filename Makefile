ldap-start:
	docker stop my-openldap-container || true && \
    docker rm my-openldap-container || true && \
	docker run --name my-openldap-container -p 389:389 -p 636:636 -d osixia/openldap:1.5.0

ldap-stop:
	docker stop my-openldap-container

start:
	poetry run python run.py

add-user:
	ldapadd -x -D "cn=admin,dc=example,dc=org" -w admin -f new_user.ldif

install:
	poetry install
