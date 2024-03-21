# Assignment 4: Containerization & Continuous Integration

## Due 28 Mar 2024

- Containerization: Create a docker container for the flask app created in Assignment 3
  - Create a Dockerfile which contains the instructions to build the container, which include
    - [x] installing the dependencies
    - [x] Copying `app.py` and `score.py`
    - [x] launching the app by running “python app.py” upon entry
  - [x] Build the docker image using Dockerfile
  - [x] Run the docker container with appropriate port bindings
  - In `test.py` write `test_docker(..)` function which does the following:
    - [ ] Launches the docker container using commandline (e.g. `os.sys(..)`, docker build and docker run)
    - [ ] Sends a request to the localhost endpoint `/score` (e.g. using requests library) for a sample text
      - [ ] Checks if the response is as expected
    - [ ] Close the docker container
  - In `coverage.txt`, produce the coverage report using pytest for the tests in `test.py`
- Continuous Integration:
  - Write a pre-commit git hook that will run the `test.py` automatically every time you try to commit the code to your local ‘main’ branch
  - Copy and push this pre-commit git hook file to your git repo

## References

- <https://docker-curriculum.com/>
- <https://www.tutorialspoint.com/docker/docker_overview.htm>
- <https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/>
- <https://githooks.com/>
- <https://www.giacomodebidda.com/posts/a-simple-git-hook-for-your-python-projects/>
