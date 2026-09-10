# Experiment 16 Containerize Flask To Do App

## Aim

Containerize a Flask To Do application.

## Procedure and result

The app adds, completes, reopens and deletes tasks. SQLite and a named Docker volume preserve records.

```bash
docker compose up --build -d
docker compose ps
```

1. Open `http://localhost:5016`. Add, complete and reopen a task.
2. Run `docker compose restart`; confirm the task remains.
3. Delete the task. Check that blank and overlong tasks are rejected.
4. To publish, build with `docker build -t YOUR_DOCKER_USER/flask-todo-app:v1 .`, run `docker login`, then push that tag.
5. Save app, container and persistence evidence. `docker compose down` retains data; `down -v` deletes the volume.

Observed: application tests passed, including persistence and HTML escaping. Docker execution and publication are pending. This is a single-user loopback lab app, not a public authentication service.

[All experiments](../../README.md) · [Execution status](../../STATUS.md)
