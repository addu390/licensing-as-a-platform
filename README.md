# licensing-as-a-platform `Work In Progress 🚧`
licensing-as-a-service/licensing-as-a-platform (LaaS)

#### Project goal 🚀:
- A profile store of users/customers.
- Licensing as a service.

If you are an independent software vendor (ISV) or software publisher you will most likely want to monetize the software application you have developed. The terms under which you provide your software to a customer is defined by the software license — how much the customer has to pay, for how long, which versions of your application does their license apply to, etc 🚁

Disclaimer 🚔: I had built a similar service back in 2018 at ClearTax India, in my role as a Software Engineer 1. However I roughly remember having more features such as dynamic addition of addons, licensing specific features and tons for dashboards for Sales, Business and developers. Maybe they will make the repository public someday! 

#### Licensing Schema
- Dark Blue: Master table for storing License, Package, Inclusion
- Light Blue: Mapping tables, to link License with Packages and Package with Inclusions (one-to-many)
<img src="https://pyblog.xyz/wp-content/uploads/2020/10/licensing_schema.png?raw=true" width="850"/>


