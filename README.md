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

## Production deployment

- Configure cluster: `ecs-cli up --cluster-config licensing-cluster`
- Use ECS CLI to start the server: `ecs-cli compose --project-name licensing-cluster service up --create-log-groups --cluster-config licensing-cluster`
    - Note: Use cloud formation to allocation resources: VPC, Subnet(s), Security group(s) and load balancer as defined in `ecs-params.yml`
    - AWS Log group(s) and task definitions are defined in `docker-compose.yml`
    
- Check the status of the service: `ecs-cli compose --project-name licensing-cluster service ps --cluster-config licensing-cluster`
- Additionally, configure other resources in `cloud-formation.yml` and update the existing stack or create a new stack in cloud formation console.
    


