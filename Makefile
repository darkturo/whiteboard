TARGET_DIR:=/opt/whiteboard
CONTAINER_NAME:=whiteboard

.PHONY: all clean clean_db
all: build
	docker run -v `pwd`:${TARGET_DIR} -p 8080:8080 ${CONTAINER_NAME} env PYTHONPATH=${TARGET_DIR}/lib python ${TARGET_DIR}/server.py

build: Dockerfile
	docker build . --tag ${CONTAINER_NAME}
	touch $@

clean:
	find . -name "*.pyc" -delete
	rm -f build
