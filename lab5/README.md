# Lab 5 - Schema Design and EC2 

## Schema Design
This section contains exercises for week 4. Some refresher:

+ <a href="https://www.codecogs.com/eqnedit.php?latex=A&space;\to&space;B" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A&space;\to&space;B" title="A \to B" /></a> means that for any two records, if they have the
same values for A, they will have the same values for B.  
+ Given an initial set of functional dependencies (FDs), we can compute the closure, by deriving more FDs
using [Armstrong's axioms](https://en.wikipedia.org/wiki/Armstrong%27s_axioms).
+ 1st normal form (1NF): flat relation, with all atomic attributes (i.e., no composite fields).
+ 2nd normal form (2NF): all non-key attributes are fully functional dependent to the candidate key.
+ BCNF: for any non-trivial functional dependency<a
href="https://www.codecogs.com/eqnedit.php?latex=A&space;\to&space;B" target="_blank"><img
src="https://latex.codecogs.com/gif.latex?A&space;\to&space;B" title="A \to B" /></a>, A
is a super key. BCNF does not preserve all functional dependencies decomposed relations. 
+ 3rd normal form (3NF): for any non-trivial functional dependency <a
href="https://www.codecogs.com/eqnedit.php?latex=A&space;\to&space;B" target="_blank"><img
src="https://latex.codecogs.com/gif.latex?A&space;\to&space;B" title="A \to B" /></a>, A is a super key or B is a part of a candidate key. 3NF
may contain redundancy. 
+ There is an algorithm to construct BCNF. BCNF and 3NF are lossless decomposition.  

### Exercise 1
Given the relation <a href="https://www.codecogs.com/eqnedit.php?latex=R(A,B,C,D,E)&space;"
target="_blank"><img src="https://latex.codecogs.com/gif.latex?R(A,B,C,D,E)&space;" title="R(A,B,C,D,E)" /></a> with the following FDs: 

<a href="https://www.codecogs.com/eqnedit.php?latex=C&space;\to&space;E" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C&space;\to&space;E" title="C \to E" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=BD&space;\to&space;AE" target="_blank"><img src="https://latex.codecogs.com/gif.latex?BD&space;\to&space;AE" title="BD \to AE" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=A&space;\to&space;BC" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A&space;\to&space;BC" title="A \to BC" /></a>

**[Q1]** Show that <img src="https://latex.codecogs.com/gif.latex?BD"/> is a candidate key. 

### Exercise 2
Given the relation <a href="https://www.codecogs.com/eqnedit.php?latex=R(A,B,C,D,E)&space;"
target="_blank"><img src="https://latex.codecogs.com/gif.latex?R(A,B,C,D,E)&space;" title="R(A,B,C,D,E)" /></a> with the following FDs: 

<a href="https://www.codecogs.com/eqnedit.php?latex=A&space;\to&space;C" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A&space;\to&space;C" title="A \to C" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=C&space;\to&space;DE" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C&space;\to&space;DE" title="C \to DE" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=B&space;\to&space;AE" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B&space;\to&space;AE" title="B \to AE" /></a>

**[Q1]** Is R in 2NF? Why?

**[Q2]** Is R in BCNF? Why?

### Exercise 3
Given the relation <a href="https://www.codecogs.com/eqnedit.php?latex=R(A,B,C,D,E,F,G)&space;"
target="_blank"><img src="https://latex.codecogs.com/gif.latex?R(A,B,C,D,E,F,G)&space;" title="R(A,B,C,D,E,F,G)" /></a> with the following FDs:

<a href="https://www.codecogs.com/eqnedit.php?latex=E&space;\to&space;C" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E&space;\to&space;C" title="E \to C" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=G&space;\to&space;AD" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G&space;\to&space;AD" title="G \to AD" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=B&space;\to&space;E" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B&space;\to&space;E" title="B \to E" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=C&space;\to&space;BF" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C&space;\to&space;BF" title="C \to BF" /></a>

**[Q1]** Compute the closure of E. 

**[Q2]** Decompose R into BCNF.


### Exercise 4

Given the relation <a href="https://www.codecogs.com/eqnedit.php?latex=R(A,B,C,D,E)&space;"
target="_blank"><img src="https://latex.codecogs.com/gif.latex?R(A,B,C,D,E)&space;" title="R(A,B,C,D,E)" /></a> with the following FDs:

<a href="https://www.codecogs.com/eqnedit.php?latex=A&space;\to&space;C" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A&space;\to&space;C" title="A \to C" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=B&space;\to&space;AE" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B&space;\to&space;AE" title="B \to AE" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=E&space;\to&space;D" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E&space;\to&space;D" title="E \to D" /></a>

**[Q1]** Is the relation in BCNF? Why? If not, decompose it to BCNF?

## EC2
This section include sample scripts for interacting with EC2. Some refreshers:

* EC2 offers virtual machines to user. An **image** (or Amazon Machine Image) is a virtual machine image. An
**instance** is a running image. An instance has:
  + One associated image. 
  + An instance **type**: CPU, RAM, and network configurations.
  + A **volume**: a storage attached to it. 
  + Security group: firewall policy.
  + Public IP address and DNS address.
  + Private IP address and DNS address.

* Three ways to interact with EC2
  + Web GUI: log in to EC2 through Amazon website. 
  + Command line interface (CLI)
  + Boto3: Python library

## Setup
**This is very important**

This step stores **your AWS private key** at a location that `boto3` can access. The key is used for all
interaction with the AWS service. 

* Step 1: install AWS tools `awscli` via pip
  ```
  pip install awscli --upgrade --user
  ```

* Step 2: run `aws configure`. This will ask you for:
  + Your Access Key ID: the **public** part of your key. You can see it from your EC2 GUI. 
  + Your Secrete Access Key: the **private** part of your key. You will **see it only once** when you created
  the key using EC2 GUI. Make sure to write that down (then burn the paper!).
  
  If successful, your credentials will be stored at `~/.aws` directory (unless you specified otherwise). **If
  anyone gets a copy of that directory, he/she can use your account.**

## Start connection
Before doing anything, you need to establish a connection to EC2 service. In Python

```
import boto3
ec2 = boto3.client('ec2')
```
If there are errors, this means your setup is wrong. Perhaps your keys didn't match. 

After this, `ec2` is a handle for interacting with EC2 service. To see what interactions are available, do

```
dir(ec2)
```

## Getting instance information
Checkout the `list_ec2_instances` method in `fabfile.py`. 

`ec2.describe_instances()` returns [detailed
information](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances) about **your** instances. Some important properties
are. Response is in JSON format. Some important properties are: 
+ `Reservations`: list of instances.
+ `State`: can be running, stopped or terminated. 
+ `PublicIPAddress`: public IP address.
+ `PublicDnsName`: DNS name. 

## Creating new image from running one
One common EC2 usage is as follows. You create one instance from scratch, then install all software needed for
your tasks. Next, you want to save this instance as a new image, so that afterward you can spawn many many
more instances from the new image. These new instances will contain all the software. 

See `save_instance` method in `fabfile.py`. It does the following:

1. Create a new image from a running instance using `ec2.create_image`. 
  + `ins`: the running instance ID. You can get it from `list_ec2_instances`. 
  + `name`: unique name for your image. 
  + `desc`: description. 
2. Wait for the image to be up, by keep checking the image status using `ec2.describe_images`. 

Once created, you can check that the image is available, using either your GUI, or `list_images` method in
`fabfile.py`. 

# S3 and boto3
We can also use `boto3` to access S3 service. Recall that S3 is a storage service that exposes bucket
key-value interface. There is no notion of *machine* or *instance* in S3. 

Like with EC2, we need to establish a connection to S3. In Python

```
import boto3
s3 = boto3.client('s3')
```

### Create a bucket
AWS enforces [strict rules](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html) on bucket names. Make sure you know the rules first. 

We use the following to create a new, private bucket name `istd50043` at the `ap-southeast-1` region. 
```
s3.create_bucket(ACL='private', Bucket='istd50043', CreateBucketConfiguration={'LocationConstraint':
'ap-southeast-1'})
```

### Put and get data
* To insert a new data into your S3 bucket:
  ```
  data={}
  // populate data with value
  s3.put_object(Bucket='istd50043', Key='key0', Body=json.dumps(data))
  ```

* To list your objects:
  ```
  s3.list_objects(Bucket='istd50043')
  ```

