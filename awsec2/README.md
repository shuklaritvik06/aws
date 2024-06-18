# EC2 Concepts

Burstable performance instances in AWS (such as T2, T3, T3a, and T4g) are a type of virtual server that can handle
variable workloads efficiently. These instances can burst, or temporarily increase their CPU performance, above the
baseline when needed.

When the instance operates below its baseline performance, it earns CPU credits.
CPU credits are used to burst above the baseline. One CPU credit allows the instance to run at full CPU capacity for a
short time (e.g., one minute).

The Instance Metadata Service (IMDS) is an AWS feature that allows instances to securely access metadata about
themselves, such as instance ID, IP addresses, and security credentials, without needing external network access.

A **snapshot** in AWS EC2 is a backup of an EBS (Elastic Block Store) volume at a specific point in time.

## Virtual Private Cloud (VPC)

A VPC is a secure, isolated section of a cloud provider's network where you can deploy your resources.

### 1. Public Subnet

**Technical:**
- A subnet that is accessible from the internet.
- Resources in this subnet can be directly reached by the internet.

**Layman Example: The Lobby**
- Think of it as the lobby of an apartment building where anyone with the address can enter.

### 2. Private Subnet

**Technical:**
- A subnet that is not accessible from the internet.
- Resources in this subnet can only be accessed through a secure, internal network.

**Layman Example: Residents' Apartments**
- Similar to the private apartments in a building where only the residents can go, not visitors.

### 3. Load Balancer

**Technical:**
- A device that distributes incoming network traffic across multiple servers to ensure no single server becomes overwhelmed.
- Helps in improving the availability and reliability of your application.

**Layman Example: Receptionist in the Lobby**
- Like a receptionist who directs visitors to the correct apartment, ensuring no single resident is overwhelmed with too many visitors.

### 4. Internet Gateway

**Technical:**
- A gateway that connects your VPC to the internet.
- Allows resources in your VPC to communicate with the internet.

**Layman Example: Main Entrance Door**
- The main entrance where visitors enter and exit the apartment building.

### 5. NAT Gateway

**Technical:**
- A device that allows resources in a private subnet to access the internet while remaining unreachable from the internet.
- Translates private IP addresses to public IP addresses for outgoing traffic.

**Layman Example: Secure Back Door for Residents**
- A secure back door residents use to go out and come back in without letting strangers into their apartments.

### 6. Network ACL (Access Control List)

**Technical:**
- A set of rules that control inbound and outbound traffic at the subnet level.
- Acts as a stateless firewall.

**Layman Example: Building Security Rules**
- Security rules that decide who can enter or leave different parts of the building at various times.

### 7. Security Groups

**Technical:**
- Virtual firewalls that control inbound and outbound traffic at the instance level.
- Acts as a stateful firewall.

**Layman Example: Apartment Door Locks**
- Each resident has their own door lock, which they control who can enter their apartment.

### 8. Bastion Host (Jump Server)

**Technical:**
- A special-purpose instance that provides secure access to instances in a private subnet.
- Acts as a secure gateway for administrators to manage resources in the private subnet.

**Layman Example: Security Guard Station**
- A security guard station where authorized personnel check in before being allowed to access private apartments.

### Stateless Firewall

**Technical:**
- A stateless firewall filters packets based solely on predefined rules, without keeping track of the state of network connections.
- Each packet is evaluated independently against the rules, meaning it doesn't consider previous packets.

**Layman Example:**
- Imagine a security guard at a gate who checks each visitor's ID without remembering who they are or why they came in earlier.
- Every time someone wants to enter, they need to present their ID, and the guard verifies it against a list of allowed IDs.

### Stateful Firewall

**Technical:**
- A stateful firewall keeps track of the state of active connections and makes decisions based on the context of the traffic.
- It maintains a table of active connections and uses this information to allow or deny packets.

**Layman Example:**
- Imagine a security guard who not only checks IDs but also keeps a log of who has entered, why they are there, and their expected duration of stay.
- If someone leaves and tries to come back, the guard remembers their previous entry and the context, making it easier to decide if they should be allowed in again.
