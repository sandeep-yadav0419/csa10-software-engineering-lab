# Sources and corrections

The experiment numbers, aims and required platforms follow the user supplied
`CSA10-Software Engineering Lab Exp List.docx`. Authored examples provide the
requirements, task descriptions, designs and code. No survey, team review,
deployment screenshot or cloud result is invented.

Implementation references:

- [Flask Gunicorn deployment](https://flask.palletsprojects.com/en/stable/deploying/gunicorn/)
- [GitHub publishing Docker images](https://docs.github.com/en/actions/tutorials/publish-packages/publish-docker-images)
- [Kubernetes probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
- [Figma prototype reactions](https://developers.figma.com/docs/plugins/api/Reaction/)

Corrections to the handout: removed literal Markdown asterisks from Python and YAML;
separated concatenated shell commands; standardized `Dockerfile` and `Jenkinsfile`
case; replaced unsupported Python 3.9 and MySQL 5.7 examples with Python 3.12 and
MySQL 8.4; used real automated tests; parameterized image names; corrected results
that incorrectly mentioned merge conflicts for unrelated experiments. `docker ps`
lists containers and `docker images` lists images; neither counts remote repositories.
Publishing an image is recorded separately from running a deployed application.
