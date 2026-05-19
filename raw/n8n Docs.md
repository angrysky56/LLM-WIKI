---
title: "n8n Docs"
source: "https://docs.n8n.io/hosting/installation/docker/#n8n-with-tunnel"
author:
published:
created: 2026-05-19
description: "Documentation for n8n, a workflow automation platform."
tags:
  - "clippings"
---
## Docker Installation

n8n recommends using [Docker](https://www.docker.com/) for most self-hosting needs. It provides a clean, isolated environment, avoids operating system and tooling incompatibilities, and makes database and environment management simpler.

You can also use n8n in Docker with [Docker Compose](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/). You can find Docker Compose configurations for various architectures in the [n8n-hosting repository](https://github.com/n8n-io/n8n-hosting).

> [!note] Self-hosting knowledge prerequisites
> Self-hosting n8n requires technical knowledge, including:
> 
> - Setting up and configuring servers and containers
> - Managing application resources and scaling
> - Securing servers and applications
> - Configuring n8n
> 
> n8n recommends self-hosting for expert users. Mistakes can lead to data loss, security issues, and downtime. If you aren't experienced at managing servers, n8n recommends [n8n Cloud](https://n8n.io/cloud/).

You can also follow along with our video guide here:

![](https://www.youtube.com/watch?v=6ET3G7GiqZA)

## Prerequisites

Before proceeding, install Docker:

- [Docker Desktop](https://docs.docker.com/get-docker/) is available for Mac, Windows, and Linux. Docker Desktop includes the Docker Engine and Docker Compose.
- [Docker Engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/linux/) are also available as separate packages for Linux. Use this for Linux machines without a graphical environment or when you don't want the Docker Desktop UI.

> [!note] Stable and Beta versions
> n8n releases a new minor version most weeks. The `stable` version is for production use. `beta` is the most recent release. The `beta` version may be unstable. To report issues, use the [forum](https://community.n8n.io/c/questions/12).
> 
> Current `stable`: 2.20.9 Current `beta`: 2.21.3

## Starting n8n

From your terminal, run the following commands, replacing the `<YOUR_TIMEZONE>` placeholders with [your timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List):

```js
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
```

This command creates a volume to store persistent data, downloads the required n8n image, and starts the container with the following settings:

- Maps and exposes port `5678` on the host.
- Sets the timezone for the container:
	- the `TZ` environment variable sets the system timezone to control what scripts and commands like `date` return.
		- the [`GENERIC_TIMEZONE` environment variable](https://docs.n8n.io/hosting/configuration/environment-variables/timezone-localization/) sets the correct timezone for schedule-oriented nodes like the [Schedule Trigger node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/).
- Enforces secure file permissions for the n8n configuration file.
- Enables [task runners](https://docs.n8n.io/hosting/configuration/task-runners/), the recommended way of executing tasks in n8n.
- Mounts the `n8n_data` volume to the `/home/node/.n8n` directory to persist your data across container restarts.

Once running, you can access n8n by opening: [http://localhost:5678](http://localhost:5678/)

## Using with PostgreSQL

By default, n8n uses SQLite to save [credentials](https://docs.n8n.io/glossary/#credential-n8n), past executions, and workflows. n8n also supports PostgreSQL, configurable using environment variables as detailed below.

When using PostgreSQL, n8n doesn't need to use the `.n8n` directory for the SQLite database file. However, the directory still contains other important data like encryption keys, instance logs, and source control feature assets. While you can work around some of these requirements, (for example, by setting the [`N8N_ENCRYPTION_KEY` environment variable](https://docs.n8n.io/hosting/configuration/environment-variables/deployment/)), it's best to continue mapping a persistent volume for the directory to avoid potential issues.

To use n8n with PostgreSQL, execute the following commands, replacing the placeholders (depicted within angled brackets, for example `<POSTGRES_USER>`) with your actual values:

```js
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
```

You can find a complete `docker-compose` file for PostgreSQL in the [n8n hosting repository](https://github.com/n8n-io/n8n-hosting/tree/main/docker-compose/withPostgres).

## Updating

To update n8n, in Docker Desktop, navigate to the **Images** tab and select **Pull** from the context menu to download the latest n8n image:

[![Docker Desktop](https://docs.n8n.io/_images/hosting/installation/docker/docker_desktop.png)](https://docs.n8n.io/_images/hosting/installation/docker/docker_desktop.png)

You can also use the command line to pull the latest, or a specific version:

```js
1
2
3
4
5
6
7
8
```

After pulling the updated image, stop your n8n container and start it again. You can also use the command line. Replace `<container_id>` in the commands below with the container ID you find in the first command:

```js
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
```

### Updating Docker Compose

If you run n8n using a Docker Compose file, follow these steps to update n8n:

```js
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
```

## n8n with tunnel

> [!danger] Danger
> Use this for local development and testing. It isn't safe to use it in production.

> [!warning] Development tooling
> The tunnel feature is a convenience tool for local development. The underlying implementation may change between n8n versions.

To use webhooks for trigger nodes of external services like GitHub, n8n has to be reachable from the web. n8n provides a tunnel service using [cloudflared](https://github.com/cloudflare/cloudflared) that redirects requests from the web to your local n8n instance. Docker must be installed for the tunnel to work.

There are two ways to use the tunnel, depending on how you run n8n:

### Full stack

This runs n8n and cloudflared together in containers. The tunnel URL prints on startup and everything is wired automatically:

```js
1
```

### Services only

If you prefer to run n8n locally with `pnpm dev` or `pnpm start`, you can start cloudflared as a standalone service:

```js
1
2
3
4
5
```

The `services` command:

1. Starts cloudflared pointing at `host.docker.internal:5678` (your local n8n).
2. Fetches the public tunnel URL from cloudflared's metrics endpoint.
3. Writes a `.env` file to `packages/cli/bin/.env` with `WEBHOOK_URL` and `N8N_PROXY_HOPS=1`.
4. `pnpm dev` and `pnpm start` pick up that `.env` automatically via dotenv.

Clean up when done:

```js
1
```

## Next steps

- Find more information about Docker setup in the README file for the [Docker image](https://github.com/n8n-io/n8n/tree/master/docker/images/n8n).
- Learn more about [configuring](https://docs.n8n.io/hosting/configuration/environment-variables/) and [scaling](https://docs.n8n.io/hosting/scaling/overview/) n8n.
- Or explore using n8n: try the [Quickstarts](https://docs.n8n.io/try-it-out/).