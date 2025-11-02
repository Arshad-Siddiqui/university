Make Assumptions!

Must state assumptions, interpretations and decisions while justifying them.


# Assumptions

Notes
I’m pretending to be a network designer and have been given several tasks by a fictional large healthcare institution called York General Hospital. This institution operates independently but still reports to the NHIS (National Health Information Service) digitally as well as the local health authority.
Campus is organised into a Central Control Room as well as a Secure Data Center. On top of that there are several specialised annex facilities. They all need to be connected reliably and securely. The infrastructure must also be tailored for each facility.
For some end devices ‘The hospital uses digital systems to monitor patient vitals, store and transmit medical records, manage diagnostic equipment, and support operational communications across departments. The facility also leverages advanced technologies, including IoT-connected medical sensors, cloud-integrated diagnostics, and mobile workstations used by clinical staff for bedside access to electronic health records (EHR).
‘
The Central Control Room and Data Centre are connected with a wired backbone while the annexes use wireless communication in order to keep costs down as well as make the equipment easier to use.

# Background

- I'm a netwok consultant working for York General Hospital.

- Campus consists of Central Control Room, Data Center and several annex facilities.

- Digital systems monitor patient vitals, keep medical records, manage diagnostic equipment and support operational communication across the departments.

- Internet of Things connected medical sensors, cloud integrated diagnostics and mobile workstations are used.

there is a hybrid infrastructure where the CCR and DC have a secure wired backbone and the annex facilities use wireless communications/mobile technologies to keep costs down and reduce disruption.

Because data is highly sensitive, and the large spread of the campus, there are robust solutions required in order to minimize signal degradation, interference and to enforce strict access control.

## CCR:

- Administrative nerve center of the hospital. Oversees patient movement, scheduling, security, emergency alerts and internal communication.

- I'm thinking a star topology as a lot of information needs to be flowing through here anyways. The CCR being the center with all the other departments connected up.

- This department is in charge of security so will need to be connected up to everything anyways. In order to avoid redundancy, data for the secure data center might as well come through here as well considering the departments are hooked up with a wire. For that crazy throughput requirement we are assuming that wire is fiber optic.

- Has a secure wired backbone that connects up to the Secure Data Center. Maybe look up fiber for high throughput communication between the two departments.

In order to communicate with the other departments wirelessly we can use ...

## Secure Data Center (IT Department)

Hosts electronic health records, diagnostic imaging archives and backend systems supporting data access, analytics and compliance.

Sounds like it has a database and runs a few programs in order for the other departments to access this data whilst being compliant to various standards.

## Annex 1 - Lab Services

A few different labs including pathology, haematology and microbiology. Staff process various biological samples here that gets sent off to the central database.

- I'm thinking connecting it up to the central database as there's probably specialised equipment ready to collect this data there.

How are y'all interpreting secure wired backbone? Is there a wire going between the CCR and SDC or are we saying those 2 departments are connected up with ethernet cables internally but with no physical linkage between them?

## Annex 2 - Diagnostics Imaging (X-Ray and MRI Units)

X-Ray and MRI machines generate very large files that need **high bandwidth** in order to transfer information to the data center

Worth looking at high bandwidth options.


## Annex 3 - Sensory Therapy Rooms:

These rooms use IoT devices for therapeutic modulation. IoT is where regular devices are fitted with network equipment so they can be controlled remotely.

## Restricted access area - Labour and Delivery Suite:

Only accessible by authorised maternity staff. Biometrics (face recognition) and end to end encryption is used for medical equipment, monitoring and patient record systems.

- Important thing here is that data flowing around here is encrypted. Also look into hooking up these face scanners.

# Network Requirements

- Staff must only have access to systems and data relevant to their job and department

- Sensitive data gets securely transmitted between annexes and the data center.

Maybe the data center should be the middle of the star topology

- IoT integration: The devices in the sensory room and whatever wireless medical equipment. Maybe a 4g network is required to adjust the sensory equipment or report data.

- Bandwidth management: Imaging department needs high capacity bandwidth to transfer x-ray and mri files

- Resilient wireless communication: Physical cabling between buildings is cost prohibitive. We're using wireless connectivity.

The wireless connectivity needs to overcome weatherbased interference as well as metal walls etc... hospital grade shielding, rain.

- Emergency Communication and monitoring: CCR must have **constant communication** with all annexes. (This is the center of the star topology!! Stop changing your mind on this bro)

- Network must adhere to national data protection regulations.

Worth looking into GDPR, NHS DSP Toolkit and other regulations.

# Notes on physical hardware

A requirement is that workstations are restricted by user job role.

---

CCR: 100 computers

IT department (DC): 25 computers

For the above computers they are in wired lan networks that are physically separate from each other.

---

Lab Services (Annex 1): 25 computers

Diagnostic imaging (Annex 2): 20 Mobile devices and 20 computers

All these devices are connected wirelessly and backed up to cloud storage in the IT department Data Center.

---

Labour and delivery suite: 20 mobile devices and 20 computers which are only accessible by authorised maternity staff. Assuming these are all wireless as well.

# Servers located in data center

## Authorisation server

- 1 machine which is physical and on site in the data center. Allows users to log into the internal company resources.

## Web Server (Cloud Based)

- 1 machine which is cloud based (somewhere else). Hospital needs internet to connect to it I guess..

- Has an analytics dashboard that shows the output of all IoT and sensor devices.

## Email, DNS and File Server

3 machines located on site in the data centre. Accessible by all company computers providing shared services for all the users.

## Server

1 machine which is physical and on site. Hosts the programs and stores the data needed. Might as well put this in the IT department or the CCR so all devices can access data.

## IoT device server

1 machine which is cloud based so the server is off site. It collects data from IoT devices and hosts apps used to present data back to the server room.

# Assessment Tasks

## Assessment Concerns
Concern 1: Make design diagram that follows the requirements of the scenario and maps out the physical layoute of the network system. Also include IP address design and the network components in order to get the job done.

(L3 switchesm routers etc)

Concern 2: Chief Information Security Officer (CISO) wants connectivity between the main office and the annexes. He's also concerned about the resilience/availability of remote devices and sensors.

Concern 3: CISO worried about impact, security and feasibility of proposed data centers, IoT devices, smart building sensors and mobile devices.

## Task 1

- Make network diagram that supports secure and scalable operations across the hospital and its annexes.

Perhaps think about what can change to the hospital and be ready for it. Maybe new tech and how easy it would be to switch over or ensure new buildings being built can still connect.

- Label the types of networking components used.

- Include appropriate design for each department's network and keep each department separated out.

- Indicate where internal and external network addresses are used per scenario.

- High level ip design showing submet ranges and allocations per department

- Relevant network protocols used in design including the routing and addressing protocols which should be in place including examples.

- Justification for designa nd all network component choices explaining how each is used to fulfil requirements.

## Task 2

Addressing concerns of CISO

- Propose and justify strategy to increase network resilience and availability

- Discuss how IoT, cloud based services may affect network traffic, latency and throughput

- Explanation of measures the CISO can use to identify potential network programs with examples

## Task 3

To do with legals and ethics etc..

- Evaluate different potential attacks on virtual proviate network and the implications. Include brief descriptions on how to mitigate attacks whilst justifying choices.

- Evaluation of legal and ethical considerations of implementing a secure network. IoT server, IoT enabled security, smart building sensors... all must be addressed and explain the possible implications if these are not properly managed.

# Deliverables

Referencing: IEEE refering style for books, articles, sources such as websites etc.

Good referencing: All sources must be acknowledged with or without direct quotes.

---

# Let's get down!!!

PTP vs PTMP: https://www.geeksforgeeks.org/computer-networks/differences-between-point-to-point-and-multi-point-communication/

In multipoint the channel gets shared among multiple devices. In terms of future proofing this means that there is fewer and fewer bandwidth for each annex as more get added over time.
