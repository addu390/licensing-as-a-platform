# licensing as a Platform `Work In Progress 🚧`

If you are an independent software vendor (ISV) or software publisher you will most likely want to monetize the software application you have developed. The terms under which you provide your software to a customer is defined by the software license — how much the customer has to pay, for how long, which versions of your application does their license apply to, etc 🚁

## Project goal 🚀:

- A profile store of users/customers (entities tagged to a license).
- Licensing as a Platform.

## Project set-up

- Install [Docker Engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/)
- Create a new file `.env` at the root of the project with the contents of `.env.example` with the correct values. 
- Start the application: `docker-compose -f docker-compose.dev.yml up`, which builds the local project instead of picking it from docker-hub.
- To run the latest build in docker hub, run: `docker-compose up`
