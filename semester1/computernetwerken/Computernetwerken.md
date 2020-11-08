*Auteur:  Tuur Vanhoutte*
# Chapter 1: Communication, local networks and simple network

|Word|Definition|
|--|--|
|Data|A value that represents something|
|Volunteered data|Explicitly created and shared by individuals, like social media profiles|
|Inferred data|Data based on analysis of volunteered/observed data|
|Observed data|Recorded data about the user, like location data on a smartphone|
|Bit|0 or 1|
|Byte|8 bits|


Bits are transferred using:
* Copper wires (electrical pulses)
* Fiber-optic cabling (light pulses/optic signals)
* Wireless (radio waves)

|Word|Definition|
|--|--|
|Bandwidth|The amount of data that can flow from one place to another in a given amount of time measured  in the number of bits that can **theoretically** be sent across the media in 1 second
|Throughput|The **actual** measure of the transfer of bits across the media over a given period of time|
|Latency|Measurement of the amount of time that it takes for a specific piece of data to travel across the network from source to destination|
|Network media|The wires, optical fibres and electromagnetic waves that are used to transmit data signals from a source to a destination|

## Networkcomponents
|Word|Definition|
|--|--|
|Servers|Hosts that have software installed that enable them to **provide** information, like email or web pages, to other hosts on the network|
|Clients|Computer hosts that have software installed that enable them to **request and display** the information obtained from a server|

The network infrastructure contains **3 categories of hardware components**:
1) **Intermediate devices**: router, switch, access points, firewall, call manager, ...
2) **End devices**: laptop, printer, tablet, smartphone, server, ...
3) **Network media**: LAN media, WAN media, Wireless media, the cloud

## Peer-to-peer networking
= network in which a host can be **both** a client and a server for other hosts.

**Advantages**
* Easy to set up
* Less complex
* Lower cost
* For simple tasks

**Disadvantages**:
* No centralized administration
* Not as secure
* Not scalable 
* All devices may act as both clients and servers which can slow their performance

# Chapter 2: Networks in our daily lives
## Getting online
3 things that must be correct before a device can send and receive information on a network: 
1) **IP Address**: identifies the host on the network
2) **Subnet mask**: identifies the network on which the host is connected
3) **Default gateway**: identifies the networking device that the host uses to access the internet or another remote network.

**Different types of networks:**
* GPS
* Wi-Fi
* NFC
* Bluetooth

**Different types of network components:**
* **Hosts**: Laptop, server, network printer, PC, ...
* **Peripherals**: Webcam, ...
* **Network devices**: Routers, switches, ...
* **Network media**: Cabling between hosts and network devices

## Keeping track of it all

|Word|Definition|
|--|--|
|Physical topology|Shows where each host is located and how it is connected to the network|
|Logical topology|Illustrates the device names, IP addressing, configuration information, and network designations|

### Types of network cabling
* Twisted-Pair (TP): 
	* Type of copper cable
	* Unshielded (UTP) or shielded (STP)
	* Most common type of network cabling
* Coaxial cable:
	* Copper or aluminium
	* Better shielding than UTP and can carry more data.
	* Used by cable television companies to provide service, and for sattelite communication systems
* Fiber-optic: 
	* Glass or plastic
	* Very high bandwidth
	* Immune to EMI & RFI
	* Used in backbone networks, large enterprise environments, and large data centers
	* Single-mode fiber-optic:
		* small diametral core that allows only one mode of light to propagate: signal can travel further, but less data at a time.
	* Multi-mode fiber-optic:
		* bigger diamteral core that allows multiple modes of light to propagate: signal can travel less far, but more data at a time.

|Word|Definition|
|--|--|
|Electromagnetic interference (EMI)| Happens in copper cabling, can reduce data throughput rate|
|Crosstalk|Occurs when long lengths of cables are bundled together. The electrical impulses from one cable may cross over to an adjecent cable.|
|Network Interface Card (NIC)|Hardware that enables the device to connect to the network medium, either wired or wireless|

### Two wiring schemes
= T568A & T568B. Each wiring scheme defines the pinout on the end of the cable.![enter image description here](https://i.imgur.com/lLzZPNw.png)
|Word|Definition|
|--|--|
|Pinout|The pattern/order of the wire connections at the end of the cable|
|Unlike devices|Devices that use different wires for transmit and receive. Needs straight-through cabling|
|Like devices|Devices that use the same wires for transmit and receive. Needs crossover cabling|
|Straight-through cables| Cables with the same color pattern on both ends of the cable|
|Crossover cables|Cables with different color pattern on the ends of the cable|


# Chapter 3: Communicating on a local network

## Principles of communication
The three elements: 
1) Source
2) Destination
3) Transmission medium

|Word|Definition|
|--|--|
|Communication  protocols|rules/agreements to govern the conversation|
|Standard|Set of rules that determines how something must be done|
|Network standards organizations|Organizations that develop, publish and maintain Internet standards: IEEE, ICANN, IETF|
|Protocol stack|Used to help seperate the function of each protocol. Each layer operates independantly of others|
|Layered model|Visualization of how the protocols work together to enable network communications|
|Encapsulation|The process of adding additional information to the pieces of data that make up the message in order to ensure that it is delivered to the correct application on the correct destination host|

**Network protocols define many aspects of communication:**
* Message format
* Message size
* Timing
* Encoding
* Message patterns
* Encapsulation


|Model|Example|Definition|
|--|--|--|
|Protocol Model|TCP/IP|Closely matches the structure of a particular protocol suite, which includes the set of related protocols that typically provide all the functionality required for people to communicate with the data network|
|Reference Model|OSI Model|Describes the functions that must be completed at a particular layer, but does not specify exactly how a function should be accomplished|

* All = Application Layer
* People= Presentation Layer
* Seem = Session Layer
* To = Transport Layer
* Need = Network Layer
* Data = Data Link Layer
* Processing = Physical Layer

![enter image description here](https://i.imgur.com/AMVJdYH.png)
### TCP/IP Model
|Layer|Definition|
|--|--|
|Application|Represents data to the user, plus encoding and dialog control|
|Transport|Supports communication between diverse devices across diverse networks|
|Internet|Determines the best path through the network|
|Network Access|Controls the hardware devices and media that make up the network|


### Open System Interconnection (OSI) Model
|Layer|Definition|
|--|--|
|Application|Means for end-to-end connectivity between individuals|
|Presentation|Provides common representation of the data transferred between application layer services|
|Session|Provides services to the presentation layer to organize its dialogue and to manage data exchange|
|Transport|Defines services to segment, transfer, and reassemble the data for individual communications between end devices|
|Network|Provides services to exchange the individual pieces of data over the network between identified end devices|
|Data link|Describes methods for exchanging data frames between devices over a common medium|
|Physical|Describes the mechanical, electrical, functional and procedural means to activate, maintain, and de-activate physical connectionsfor a bit transmission to and from a network device|


## Layers of the OSI Model

The OSI Model breaks network communications down into multiple processes: 
![enter image description here](https://i.imgur.com/IaUHxa6.png)

## Ethernet

* Ethernet has become the standard: used by almost all wired local area networks
* Maintained by the **Institute of Electrical and Electronic Engineers (IEEE)**, constantly evolving.
* Each host connected to an Ethernet Network has a unique physical address (=Media Access Controll or MAC-address), assigned to a NIC when it was manufactured. **MAC-address = 48bit**

|Word|Definition|
|--|--|
|Encapsulation|The process of placing one message inside another message|
|De-encapsulation|The reverse process of encapsulation|

#### IEEE 802.3 Ethernet Frame
|# bytes|Field name|Definition|
|---|---|---|
|7|Preamble|Defined pattern of alternating bits used to synchronize timing
|1|Start frame delimiter|Marks the end of the timing information and start of the frame
|6|Destination MAC Address|MAC-Address of the destination, can be unicast (one host), multicast (a group of hosts) or broadcast (all hosts on the local network)|
|6|Host MAC Address|MAC-Address of the source (sender), always unicast|
|2|Length/type|Type: which protocol will receive the data. <br>Length= number of bytes of data that follows this field|
|46-1500|Encapsulated data|The packet of information being sent. Ethernet requires each field from the Destination MAC address to the FCS to be between 64 and 1518 bytes|
|4|Frame Check Sequence (FCS)|CRC Checksum: created by the device that sends data and is recalculated by the destination device to check for damaged frames|

### Hierarchial design

* Needed because a MAC-address identifies a specific host on a local network, but it cannot be used to reach remote hosts networks.
* Require logical addressing schemes (IPv4 or IPv6) to reach remote hosts.
* Both the physical MAC and logical IP addresses are required for a computer to communicate on a hierarchial network.
* 3 basic layers
	* **Access Layer:** 
		* Provides connections to hosts in a local network
		* Typically connected using Layer 2 switches
		* If message is destined for a local host: message remains local
		* If message is destined for a different network: message is passed up to the distribution layer
	* **Distribution layer:** 
		* Provides a connection point for seperate networks and controls the flow of information between the networks
		* Routers for routing between the networks and more powerful switches than the access layer
	* **Core layer:** 
		* High-speed backbone layer with redundant (backup) connections
		* Responsible for transporting large amounts of data between multiple end networks.
		* Very powerful, high-speed switches and routers. 
		* Main goal: transport data quickly 

|Word|Definition|
|--|--|
|Ethernet hubs|Legacy access layer device that broadcasts frames to all ports|
|Ethernet switch|Accepts and decodes the frames to read the physical (MAC) address portion of the message. Uses a MAC Address table to send messages to one host|
|Broadcast message|A message that is simultaniously sent by a host to all other hosts|
|Broadcast MAC Address|In hexadecimal notation: FFFF.FFFF.FFFF|
|Broadcast domain|A local area network / a network with one or more Ethernet switches <br> When a broadcast message is sent, all switches forward the message to every connected host within the same local network|

### Address Resolution Protocol (ARP)
Uses a 3 step process to discover and store the MAC-address of a host on the local network when only the IPv4 address is known.
1) The sending hosts creates and sends a frame addressed to a broadcast MAC address. Contained in the frame: the IPv4 address of the intended destination host
2) Each host on the network receives the broadcast frame. The host with the matching IPv4 address sends its MAC address back to the original sending host.
3) The sending host receives and stores the MAC address and IPv4 address information in an **ARP table**.


### Dividing the network
Many ways to divide a network, based on different criteria:

* **Broadcast containment:**
	* Routers in the distribution layer can limit broadcasts to the local network where they need to be heard. Too many hosts connected to the same local network can generate excessive broadcast traffic and slow down the network. 
* **Security requirement:**
	* Routers in the distribution layer can seperate and protect certain groups of computers where confidential information resides. 
	* Routers can also hide the addresses of internal computers from the outside world to help prevent attacks, and control who can get into or out of the local network.
* **Physical locations:**
	* Routers in the distribution network can be used to interconnect local networks at various locations of an organization that are geographically seperated.
* **Logical grouping:**
	* Routers in the distribution layer can be used to logically group users, such as departments within a company.

### Routing
= The process of identifying the best path to a destination.

* Selecting a path
	* Router creates a routing table containing all locally-connected and remote networks and the interfaces that connect to them.
	* Routers use their routing tables and forward packets to either a directly connected network containing the actual destination host, or to another router on the path to reach the destination host.
* Building the tables
	* Routers build their routing tables by first adding their locally connected networks, and then learning about other networks using routing protocols.

### Local Area Network

|Word|Definition|
|--|--|
|Local Area Network (LAN)|Local network or a group of interconnected local networks that are under the same administrative control|
|Intranet|Private LAN that belongs to an organization|

#### Placing all hosts in One local network segment:
Advantages:
* Appropriate for simpler networks
* Less complexity
* Lower network cost
* Allows devices to be seen by other devices
* Faster data transfer -- more direct communication
* Ease of device access

Disadvantages: 
* All hosts are in one broadcast domain $\Rightarrow$ more traffic on the segment $\Rightarrow$ may slow network performance
 
---

#### Placing all hosts in Remote Network segments:
Advantages: 
* More appropriate for larger, more complex networks
* Splits up broadcast domains and decreases traffic
* Can improve performance on each segment
* Makes the machine invisible to those on other local network segments
* Can provide increased security
* Can improve network organization

Disadvantages:
* Requires the use of routing (distribution layer)
* Router can slow traffic between segments
* More complexity and expense (requires router)

# Chapter 4: Network Addressing

## IPv4 address
* = logical network address that identifies a particular host
* unique
* associated with a Network Interface Card (NIC)
* 32bits, 4 8-bit bytes called **octets**, made up of a Network part and Host part
* Number of hosts: $2^x - 2$, where $x =$ amount of host bits

### Classes

|Address Class|Addresses|# Host addresses|Type of networks|
|--|--|--|--|
|A| 0.0.0.0/8 to 127.0.0.0/8|$\approx$ 16 million host addresses|Extremely large networks|
|B|128.0.0.0/16 to 191.255.0.0/16|$\approx$ 65000 host addresses|Moderate to large sized networks|
|C|192.0.0.0/24 to 223.255.255.0/24|254 host addresses|Small networks



### Classless addressing
* Classful addressing was abandoned in the late 90s for the newer classless system:
* Customers receive an IPv4 address and any size subnet mask appropriate to the number of hosts required
* Delays the depletion and exhaustion of IPv4 addresses
* Classless Inter-Domain Routing (CIDR)


### Private IPv4 addressing
* Does not connect directly to the internet
* Visibile on local network only
* Loopback address = 127.0.0.1

|Address Class|Number of network numbers reserved|Network addresses|Subnet mask|
|--|--|--|--|
|A|1|10.x.x.x|255.0.0.0|
|B|16|172.16.0.0 - 172.31.0.0|255.240.0.0|
|C|256|192.168.0.0 - 192.168.255.0|255.255.0.0|

Another range of private IP addresses is **169.254.0.0 to 169.254.255.255**, but those addresses are for Automatic Private IP Addressing (APIPA) use only.

### Unicast, Broadcast and Multicast Addresses

|Type|IP Address|Mac Address|
|--|--|--|
|Unicast|0.0.0.0 - **223**.255.255.255|Unique|
|Broadcast|Host portion all 1s|FFFF:FFFF:FFFF|
|Multicast|224.0.0.0 - 239.255.255.255, on local network: 224.0.0.0 - 224.0.0.255|Unique group MAC address|

### Assigning addresses
* Static
	* For hosts like servers or printers that need a particular address
	* Can be time consuming or error prone
	* Need to maintain accurate list
* Dynamic
	* Uses Dynamic Host Configuration Protocol (DHCP): automatic assignment of addressing information
	* Preferred method of assignment for large networks
	* IP addresses can be reallocated when they become available

DHCP servers:
|Medium - Large networks|Home network|
|--|--|
Usually a local dedicated PC-based server|A wireless router can serve as a client to receive IP information from the ISP, and can act as a DHCP server for the hosts in the local network|

How does IPv4 DHCP work?
1) Client sends a **DHCP discover message**
	* Destination IPv4 address: 255.255.255.255 (32 1s)
	* Destination MAC address: FF-FF-FF-FF-FF-FF (48 1s)
2) DHCP server responds with a **DHCP offer**, suggesting an IPv4 address for the client
3) The host sends a **DHCP Request** to that server asking to use the suggested IPv4 address
4) The server responds with a **DHCP acknowledgment**

#### Gateways to other networks
Each host uses a default gateway (= IPv4 address of the router interface connected to the network where the host is attached). The default gateway device serves as a boundary between the local internal network and the external internet.

### Network address Translation
* Translate private addresses into unique Internet-routable public addresses for outgoing packets
* Process is reversed for incoming packets
* The router can translate many internal IPv4 addresses to the same public address

## IPv6 addressing
* Problem:
	* An IPv4 address is 32bits (4 bytes) long
	* Too many devices to keep in 32bits
* Solution:
	* An IPv6 addres is 128bits (16 bytes) long $\Rightarrow$ more IP addresses
	* No need for NAT because each device can have its own globally routable address
	* Autoconfiguration capabilities
		* Stateless Address Autoconfiguration (SLAAC) allows a host to create its own Internet Routable address without the need for a DHCP server.
	* Link-local address
		* For communicating within the same network

**Address formatting**
* Compressing IPv6 addresses:
	* Omit leading zeros
	* Omit 1 'all-zero' segment
	* 2001:0DB8:0000:1111:0000:0000:0000:0200, compressed:
* No subnet masks, but network prefixes instead

||IPv6 address|
|--|--|
|Fully expanded|2001:0DB8:0000:1111:0000:0000:0000:0200|
|No leading 0s|2001:DB8:0:1111:0:0:0:200|
|Compressed|2001:DB8:0:1111::200|


# Chapter 5: Providing Network Services
## The client server relationship
= A client sends a request to a server, and the server responds by carrying out a function, such as sending a  requested document back to the client.

### URL
= Uniform Resource Locator, used to locate the server and a specific resource. The URL identifies:
* The protocol being used (usually HTTPS)
* Domain name of the server (example.com)
* Location of the resource on the server (example1)
* The resource (index.html)

https://example.com/example1/index.html

### Protocols used for Internet services
|Protocol|Function|
|--|--|
|Domain Name System (**DNS**) | Resolves Internet names to IP addresses|
|Secure shell (**SSH**)|Used to provide remote access to servers and networking devices|
|Simple Mail Transfer Protocol (**SMTP**)|Sends email messages and attachments from clients to servers and from servers to other email servers|
|Post Office Protocol (**POP**)|Used by email clients to retrieve email and attachments from a remote server|
|Internet Message Access Protocol (**IMAP**)|Used by email clients to retrieve email and attachments from a remote server|
|Dynamic Host Configuration Protocol (**DHCP**)|Used to automatically configure devices with IP addressing and other necessary information to enable them to communicate over the Internet|
|Web Server|Transfers the files that make up the web pages of the World Wide Web using HyperText Transfer Protocol (**HTTP**)|
|File Transfer Protocol (**FTP**)|Used for interactive file transfer between systems|


## The TCP/IP Protocol Suite
The various protocols necessary to deliver a web page function at the four different levels of the TCP/IP model:
|Layer|Protocol|
|--|--|
|Application Layer Protocol|HTTP, FTP, DNS, SMTP, Telnet, DHCP|
|Transport Layer Protocol|TCP, UDP|
|Internetwork Layer Protocol|Internet Protocol (IP)|
|Network access protocol|Depends on the type of media and transmission methods used in the physical network

|Word|Definition|
|--|--|
|TCP|Transmission Control Protocol: for when an application requires acknowledgment that a message is delivered|
|UDP|User Datagram Protocol: a 'best effort' delivery system that does not require acknowledgment of receipt|
|Port|Numeric identifier within each segment that is used to keep track of specific conversations between a client and server|
|Socket|The combination of IP address and port number that identifies a specific conversation between two devices on the network|
|Source port|A randomly generated port number that identifies the process or client on the device that is making the request tot he destination device|
|Destination port|The port assigned to the application on the server. Example: port 80 is the well-known port for the HTTP web server application|
|Well-known port|A port that is registered on the Internet for common TCP/IP applications to use by default|
|Acknowledgment|Message sent from the destination host to the source to confirm that the transmitted segments were received|
|Transport Layer Segments|The pieces of data that are formatted with source and destination port numbers|



### Ports
Categorized in 3 groups:
* Well-known:
	* 1 - 1023
* Registered:
	* 1024 - 49151
* Private
	* 49152 - 65535

Every message that a host sends contains both a ...
* **source port**:
	* Dynamically generated by the sending device to identify a conversation between 2 devices
* **destination port**:
	* The client places a destination port number in the segment to tell the destination server what server is being requested.

|Service|Port|Function|
|--|--|--|
|HTTP|80|Web traffic|
|HTTPS|443|Secure web traffic|
|FTP|20, 21|File transfer|
|DNS|53|Name resolution|
|SMTP|25|Internet mail|
|POP3|110|Post Office Protocol (POP) mailbox|
|IMAP|143|Internet Message Access Protocol (IMAP) mailbox|
|Telnet|23|Remote login|
|SSH|22|Secure remote login|


## Domain Name System (DNS)
The DNS names are registered and organized on the Internet within specific high level groups (=domains). Some of the most high level domains on the internet are: .com, .edu, .net, ...
A DNS server contains a table that associates hostnames in a domain with corresponding IP addresses. When the DNS server receives a request, it checks its table to determine the IP address associated with that server.

## Web clients and servers
When a web client receives the IP address of a web server, the client browser uses that IP address and port 80 to request web services using HTTP. HTTP tells the browser how to format the web page and what graphics and fonts to use.

## FTP clients and servers
FTP = File Transfer Protocol:
* An easy method to transfer file from one computer to another
* Enables clients to manage files remotely by sending file management commands (delete/rename/..)
* 2 different ports to communicate between client and server
	* Control connection (port 21): to open the connection
	* Data connection (port 20): to transfer files

## Virtual terminals
* Telnet:
	* Uses software to create a virtual device that provides the same features of a terminal session with access to the server's command line interface (CLI)
* SSH:
	* Provides for secure remote login and other secure network services.
	* Provides stronger authentication than Telnet and supports the transport of session data using encryption. 
	* Network professionals should always use SSH in place of Telnet, when possible.

## Email and messaging
* Email clients and servers:
	* Each mail server receives and stores mail for users who have mailboxes configured on that mail server. 
	* Each user with a mailbox must then use an email client to access the mail server and read these messages.
* Email protocols:
	* SMPT
		* Used by an email client to send messages to its local email server. The local server then decides if the message is destined for a local mailbox or if the message is addressed to a mailbox on another server.
	* POP3
		* Mails get deleted from the server after they have been accessed by a client
	* IMAP4
		* Mails are kept on the server even if they have been access by a client
* Instant Messaging (IM)
	* IM applications require minimal configuration to operate.
	* Supports transfer of text messages, documents, video, music, audio, ...
* Internet Phone calls
	* Uses Voice over IP (VoIP) technology which converts analog voice signals into digital data. The voice data is encapsulated into IP packets which carry the phone call through the network.


# Chapter 6: Building a Home Network
## Home network basics

* Home network = a small LAN with devices that connect to an integrated router. The router is connected to the Internet.
* Wireless technologies use electromagnetic waves to carry information between devices. 

|Frequency Range|Devices|
|--|--|
|902-928 MHz|Cordless phones|
|2.400-2.4835 GHz|IEEE 802.11 b/g/n/ad|
|5.725-5.850 GHz|IEEE 802.11 a/n/ac/ad|

## Wireless settings
|Settings|Options|Description|
|--|--|--|
|Network Mode|Mixed, b, g, n,...|Determines the type of techology that must be supported|
|Network Name|case-sensitive, alpha-numeric string up to 32 characters|Used to identify the network|
|Standard Channel|A number or *Auto*|The channel over which communication will occur|
|SSID Broadcast|Enabled (default) / Disabled|Determines if the SSID will be broadcast to all devices within range|

## Controlling wireless traffic
* Wireless devices that transmit over the same frequency range create interference in a Wi-Fi network. Channels are created by dividing up the available RF spectrum.
* Wireless technology uses an access method called **Carrier Sense Multiple Access with Collision Avoidance** (CSMA/CA). It creates a reservation on the channel for a specific conversation between devices.

## Accessing the wireless router
* Many wireless routers designed for home use have an automatic setup utility.
* The decision regarding who can access your home network should be determined by how you plan to use the network. Many routers support *MAC address filtering*.

## Internet Service Providers (ISPs)
* An ISP provides a link between the home network and the global internet. ISPs are critical to communications across the internet. Each ISP connects to other ISPs to form a network of links that interconnect users all over the world.
* A router is required to securely connect a computers to an ISP. The router includes:
	*  a switch to connect wired hosts
	* a wireless AP to connect wireless hosts
* The router also provides client addresses and security for inside hosts.

## ISP Connectivity Options
* The two most common  methods to connect to an ISP are **Cable** and **Digital Subscriber Line (DSL)**.
* Other ISP connectivity options are:
	* Sattelite
	* Cellular
	* Dial-Up Telephone

## ISP connection terms
|Word|Definition|
|--|--|
|Request To Send (RTS)|A signal sent by a wireless client requesting time to transmit on the network|
|Clear To Send (CTS)|A signal sent by the access point or wireless router indicating that a device may transmit on the wireless channel|
|Acknowledgement (ACK)|A message from the wireless client indicating that it has completed it's data transmission on the network.
|Guest Access|A special SSID coverage area that allows open access, but restricts that access to using the internet only|
|Cable Internet|Typically offered by television service providers, the Internet data signal is carried on the same coaxial cable that delivers broadcast television and phone|
|Digital Subscriber Line (DSL)|A high bandwidth, always on, connection that uses existing land-line telephone wires|
|Cellular Data Plan|Internet service that uses the carrier cell phone network to transmit data|
|Ethernet LAN Port|Ports that connect to the internal switch portion of the home integrated router|
|Internet Port|This port is used to connect the device to another network, usually of the home network|
|Wi-Fi Alliance|An organization that tests wireless LAN devices from different manufacturers in order to ensure the equipment meets the IEEE 802.11 standards|
|Mixed mode|A wireless network mode that provides connectivity to devices that use any of the existing Wi-Fi standards (b/g/n/ac..)|
|Service Set Identifier (SSID)|A case-sensitive, alpha-numeric string that is used to identify a specific wireless network|
|Wireless Channel|A division of the wireless frequency range that his capable of carrying a single data conversation, similar to the way that the signals from each individual television station are transmitted across a single medium|
|Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA)|The method of creating a reservation on a wireless network in order to ensure each client gets time to transmit on the network|
 

## Security considerations in a Home Network
### Ways to secure your network
* It's possible for an attacker to tune into signals from your wireless network, much like tuning into a radio station.
* SSID broadcast can be turned off, making it more difficult for intruders to connect to your network.
* Changing the default settings
	* SSID
	* Usernames
	* Passwords
* MAC address filtering uses the MAC address to identify which devices are allowed to connect to the wireless network.
* Configure encryption
* Configure authentication

### Authenticating users
= the process of permitting entry to a network based on a set of credentials. It is used to verify that the device attempting to connect to the network is trusted.
* After authentication is enabled, the client must successfully pass authentication before it can associate with the AP and join the network
* When authentication is successful, the AP will then check the MAC address against the MAC address table. When verified, the AP adds the host MAC address into its host table.

### Encrypting data so it cannot be read
* An advanced and secure form of encryption is **Wi-Fi Protected Access (WPA)**.
* WPA2 uses encryption keys from 64 bits up to 256 bits. However, unlike **Wired Equivalency Protocol (WEP)**, WPA2 generates new, dynamic keys each time a client establishes a connection with the AP. 

# Chapter 7: Network Security
## Hackers & Intruders
### Types of threats
1. Information theft
2. Identify theft
3. Data loss / manipulation
4. Disruption of service

### Where do they come from?
* External threats arise from individuals working outside of an organization
* Internal threats occur when someone has authorized access to thet network through a user account or has physical access to the network equipment

## Types of hacking
### Social engineering
= a collection of techniques used to deceive internal users into performing specific actions or revealing confidential information
* **Pretexting**
	* an invented scenario (the pretext) is used on a victim in order to get the victim to release information or perform an action, typically over the phone. 
* **Phishing**
	* the phisher pretends to be a legitimate outside organization in order to get information from someone, typically via email or text messaging
* **Vishing / phone phishing**
	* uses Voice over IP (VoIP) to send a voice mail instructing a victim to call a number which appears to be a legitimate telephone-banking service.


### Software
* **Virus**
	* a program that spreads by modifying other programs or files
* **Worm**
	* similar to a virus, but does not need to attach itself to an existing program. Uses the network to send copies of itself to any connected hosts.
* **Trojan Horse**
	* a program thats written to appear like a legitimate program, when in fact it is an attack tool.

### Denial of Service (DoS)
* To flood a system or network with traffic to prevent legitimate network traffic from flowing
* Disrupt connections between a client and server to prevent access to a service
* DDoS = Distributed DoS = a more sophisticated and potentially damaging form of the DoS attack. It is designed to saturate and overwhelm network links with useless data.

### Brute Force
= a fast computer is used to try to guess passwords or to decipher an encryption code

### Spyware
= any program that gathers personal information from your computer without your permission or knowledge. This information is sent to advertisers or others on the Internet and can include passwords and account numbers.

### Adware
= form of spyware used to collect information about a user based on websites the user visits. That information is then used for targeted advertising.

### Botnets and zombies
= the infected 'zombie' computer contacts servers managed by the botnet creator. These servers act as a command and control (C&C) center for an entire network of compromised devices, or 'botnet'.

## Security tools
* Security Practices
	* Maintaining up-to-date software releases
	* Firewalls
	* Intrusion detection systems
* Security Tools
	* Many tools are available to network users to protect the devices from attacks and to help remove malicious software from infected machines.
* Patch
	* Small piece of code that fixes a specific problem.
* Update
	* May include additional functionality to the software package as wel as patches for specific issues
* Antivirus software
	* Relies on 'virus signatures' in order to find and prevent new viruses from infecting the computer
	* Email checking: scans incoming & outgoing emails for spam and suspicious attachments
	* Resident dynamic scanning: checks files when they are accessed
	* Scheduled scans: to check files periodically
	* Automatic updates: to get the latest virus signatures
* Antispam software
	* Protects hosts by identifying spam and performing an action, such as placing it into a junk folder or deleting it.
* Antispyware, Adware, Popup blockers 

## Firewalls
* Prevents undesirable traffic from entering protected areas of the network
* Usually installed between two or more networks
* Can be implemented in software, can also be hardware devices (= freestanding unit)
* Firewalls often perform Network Address Translation (NAT)

### DMZ (demilitarized zone)
= an area of the network that is accessible to both internal and external users.
* With the wireless router, a simple DMZ can be set up that allows an internal server to be accessible by outside hosts. 
* The wireless router isolates traffic destined to the IP address specified. This traffic is then forwarded only to the switch port where the server is connected.

### Port forwarding
* A rule-based method of directing traffic between devices on seperate networks. This method of exposing your devices to the internet is much safer than using a DMZ.

### Port Triggering
* Allows the router to temporarily forward data through inbound TCP or UDP ports to a specific device. You can use port triggering to forward data to a computer only when a designated port range is used to make an outbound request.


# Chapter 8: Configuring Cisco devices
|Word|Definition|
|--|--|
|Switch|Device used to connect devices on the same network|
|Router|Device to connect multiple networks to each other|

## Switches

### Choosing a switch
* Types of ports
* Number of ports
* Speed required
* Expandability
* Manageability


### Connecting the switch
* When the switch is on , the Power-On Self-Test (POST) begins
* During POST, the LEDs blink while a series of tests determine that the switch is functioning properly.
* POST is completed once the SYST LED rapidly blinks green.
* If POST fails, the SYST LED turns amber
* When booted, a Cisco device loads two files into RAM:
	* Internetwork Operating System (IOS) image file
	* Startup configuration file

## Routers
### Components
* Operating System (OS)
* Central Processing Unit (CPU)
* Random-Access Memory (RAM)
* Read-Only Memory (ROM)
* NonVolatile Random-Access Memory (NVRAM)
* Console ports
* 2 LAN interfaces
* Enhanced High Speed WAN Interface Card (EHWIC) slots

### Setting up the router
1. Mount and ground the device chassis
2. Seat the external compact flash card
3. Connect the power cable
4. Configure the terminal emulation software on the PC and connect the PC to the console port
5. Turn on the router
6. Observe the startup messages on the PC as the router boots up

*  The two most common methods to access the command line interface are:
	* console
	* SSH

## Navigate the IOS
* Cisco IOS command line interface (CLI) is a text-based program that enables entering and executing Cisco IOS commands to configure, monitor and maintain Cisco devices
* As a security feature, the IOS software is seperated into two modes:
1. user EXEC mode
	* Allows access to only a limited number of basic monitoring commands
	* 'view only'
	* Prompt is displayed as `Switch>` or `Router>`
2. priviliged EXEC mode
	* Allows all commands: can monitor and execute configuration and management commands
	* Prompt is displayed as `Switch#` or `Router#`

### The command structure: syntax in IOS
![enter image description here](https://image.slidesharecdn.com/nbinstructorpptchapter2-140924020854-phpapp01/95/ccna-rsnb-chapter-2-17-638.jpg?cb=1411524984)
#### Syntax:
1. Prompt
	* Shows in which mode the user is working, and with which device.
2. Command
3. Argument

### Using show commands
* show running-config
* show interfaces
* show arp
* show ip route
* show protocols
* show version
	* shows useful summary information about the device you are connected to

## Configuring a Cisco network
### Basic switch configuration
1. Configure the device name
2. Secure the user EXEC mode
3. Secure remote Telnet/SSH access
4. Secure priviliged EXEC mode
5. Secure all passwords in the config file
6. Provide legal notification
7. **Configure the management SVI (Switch Virtual Interface)**
8. Save the configuration

### Basic router configuration
1. Configure the device name
2. Secure the user EXEC mode
3. Secure remote Telnet/SSH access
4. Secure priviliged EXEC mode
5. Secure all passwords in the config file
6. Provide legal notification
7. Save the configuration

* Configure the interface:
	* **interface** *type-and-number*
	* **description** *description-text*
	* **ip address** *ipv4-address subnet-mask*
	* **no shutdown** (to activate the interface)

#### Verifying the interface
* **show ip interface brief**:
	* displays all interfaces, their IPv4 address, and their current status
* **show ip route**:
	* displays the contents of the IPv4 routing table stored in RAM
* **show interfaces**:
	* displays statistics for all interfaces on the device
* **show ip interface**:
	* displays the IPv4 statistics for all interfaces on a router

## Securing the devices
* As a good practice, use different authentication passwords for each level of access
* Setting a password:
	* **Switch(config)#** line console 0
	* **Switch(config)#** password [password]
	* **Switch(config)#** login

1. Verify SSH support
2. Configure the IP domain
3. Generate RSA key pairs
4. Configure user authentication
5. Configure the vty lines
6. Enable SSH version 2

* **show ip ssh**:
	* To display the version and configuration data for SSH on the device that you configured as an SSH server

## Connecting the switch to the router
* The default gateway address is generally the router interface address attached to the local network of the host
	* The IP address of the host device and the router interface address must be in the same network
* To configure a default gateway on a switch, use the **ip default-gateway** global configuration command.
	* The IP address configured is that of the router interface of the connected switch

# Chapter 9: Troubleshooting
## Network troubleshooting
* Process of identifying, locating and correcting the problems
* Mantain good documentation when troubleshooting

### Gathering information
* Question everyone who reported the problem
* Collect information about any equipment that may be affected

### Choose a troubleshooting approach
* Top-down
	* Starts at the Application Layer and works its way down to the Phycial Layer
	* For simpler problems
* Divide-and-conquer
	* Based on the circumstances (reported issues) and your experience, you might decide to start at any layer and work up or down the OSI layers
	* More suitable if you are experienced and the problem has precise symptoms
* Bottom-up
	* Starts at the Physical Layer and works its way up to the Application Layer
	* More suited for complex cases

### Other approaches
* Trial and error
	* Relies on invidivual knowledge to determine the most probable cause of a problem. 
	* Making educated guesses to find the cause of the problem
* Substitution
	* Subsituting hardware components or configuration file, to see if that fixes the problem
	* 'spot the difference'-method
	* Can save time and quickly restore network functionality

## Detecting Physical layer problems
### Using your senses
* Sight
* Smell
* Touch
* Hear

### Using software tools and utilities
* ipconfig
	* Display IP configuration information to check if IP address and subnet mask are correct
* ping
	* Test connections to other clients
* netstat, to list...
	* ...the protocols in use
	* ...the local address and port number
	* ...the foreign address and port number
	* ...the state of the connection
* tracert
	* provides connectivity information about the path a packet takes to reach the destination and about every other router (hop) along the way
* nslookup
	* nslookup utility allows and end-user to look up information about a particular DNS name in the DNS server
	* directly queries the name server for information on a destination domain

### Windows IP information
* ipconfig (/all)
* ipconfig /release
	* releases the current DHCP bindings
* ipconfig /renew
	* request fresh DHCP configuration 

### What do ping results tell us?
* If pings to both name and IP address are successful, but the user is still unable to access the application, then the problem most likely resides in the application on the destination host
* If neither ping is successful, then network connectivity along the path to the destination is likely the problem
* If the ping to the default gateway is successful, the problem is not local
* If the ping to the default gateway is sucessful, the problem resides on the local network
* A ping may fail due to firewall on the sending or receiving device, or a router along the path blocking the pings

## Identifying and fixing connectivity issues
### Divide-and-conquer
* Ping from a wireless client to the default gateway
* Ping from a wired client to the default gateway
* Ping from the wireless client to a wired client

### Bottom up
* Examine the LEDs
* LEDs may change color or flash to convey information

### Cabling problems
* Correct type of cable, ending with T568A/B
* Do not exceed maximum cable lengths
* Verify that the correct ports are being used
* Protect cables and connectors from physical damage

### Cause of wireless issues
* Not all wireless standards are compatible
* Each wireless conversation must occur on a seperate, non-overlapping channel
* Check distance to router
* Check interference
* APs share the available bandwidth between devices

### Authentication and Association errors
* The SSID must match on both the AP and client
* Both the client and AP must be configured with the same authentication key
* The same encryption key must be configured on both the AP and the client

### DHCP Server configuration errors
* The client table information should match the local host information
* Check to make sure that the router has an IP address
* The LAN interface of the wireless router should be set as the default gateway
* Examine the router status page
* Check all physical connections and LED indicators
* Try to re-establish connectivity

### Firewall
* Check that the application TCP or UDP port is open and no filter lists are blocking traffic to that port
* Check all settings on the router to ensure no security restrictions could be causing the issue


<!--stackedit_data:
eyJoaXN0b3J5IjpbODQyNTcwNDU4LDEwNjI3NTM5ODYsMTYyNz
k5MjAxNCw5Njc3MjMwMTEsMTIyNTYyNTE0NCwtODk2Mzc2MzUz
LDE3NTAwMzY0ODUsMTI0MDgyNzI1OCwxNTQ2MTgwMjk3LC0xMz
I2NjE3ODYyLDEzODUyMTg1OTMsLTEwODA3MTI0MTIsMzY1ODM2
NzI3LC0xMzIyNjQzOTY5LC0yMjAxNzc4MzYsMTg0MTIwMDM1My
wtMTYyNzQwODExMiwxMjYxMzc1ODAyLDI1ODQ0NTgxNSwtMjk3
MzA1NTgyXX0=
-->
