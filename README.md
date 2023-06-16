# Agroaid
Agroaid, a groundbreaking mobile application designed to revolutionize plant disease detection in Indonesia. Agroaid is not just another generic plant disease detection app. It is a locally-built solution tailored specifically to the needs of Indonesian farmers and gardening enthusiasts, leveraging the power of deep learning and the familiarity of the Indonesian language.

## Training the Model
This project consist of 9 different models. To train the model, you can use [apple-corn-tomato](https://github.com/farreljordan80/agroaid/blob/main/Machine%20Learning/apple-corn-tomato/Apple%2CCorn%2CTomato.ipynb) notebook, [cherry-peach-strawberry](https://github.com/farreljordan80/agroaid/blob/main/Machine%20Learning/cherry-peach-strawberry/cherry-peach-strawberry.ipynb) notebook, and [grape-pepperbell-potato](https://github.com/farreljordan80/agroaid/blob/main/Machine%20Learning/grape-pepperbell-potato/grape-peperbell-potato-model.ipynb) notebook.

## Creating VM Instances
1. Open the GCP console and log in to the desired project.
2. In the left panel, select "Compute Engine" -> "VM Instances".
3. Click the "Create" button to create the first instance:
   - On the "Create an instance" page, give a name to your first instance, for example "agroaid-vm".
   - In the "Machine configuration" section, select the instance type "e2-small" by selecting from the list.
   - In the "Boot disk" section, select a disk that suits your needs, select "Debian 11-Bullseye".
   - In the "Firewall" section, add the "allow-9000" tag by clicking "Add firewall rule", then enter "allow-9000" as the tag.
   - Click the "Create" button to create the first instance.

4. Click the "Create" button again to create the second instance:
   - On the "Create an instance" page, give a name to your second instance, for example "agroaid-ml-vm".
   - In the "Machine configuration" section, select the instance type "e2-standard-2" by selecting from the list.
   - In the "Boot disk" section, select a disk that suits your needs, for example "Debian 11-Bullseye".
   - In the "Firewall" section, add the tags "allow-5000" and "allow-9000" by clicking "Add firewall rule", then enter "allow-5000" and "allow-9000" as tags.
   - Click the "Create" button to create the second instance.

## Creating Firewall Rule
1. Open the GCP console and log in to the desired project.
2. In the left panel, select "VPC Network" -> "Firewall".
3. Click the "Create Firewall Rule" button to create the first firewall rule:
   - On the "Create Firewall Rule" page, give a name to your first firewall rule, for example "allow-5000".
   - In the "Targets" section, make sure the "Specified target tags" option is selected.
   - In the "Target tags" field, enter the tags of the VMs that you want to grant access to port 5000.
   - In the "Source IP ranges" section, leave the value as "0.0.0.0/0" to allow access from all IP addresses.
   - In the "Protocols and ports" section, select the "Specified protocols and ports" option.
   - In the "Protocols and ports" field, enter "tcp:5000" to allow TCP connections to port 5000.
   - Click the "Create" button to create the first firewall rule.

4. Click the "Create Firewall Rule" button again to create the second firewall rule:
   - On the "Create Firewall Rule" page, give a name to your second firewall rule, for example "allow-9000".
   - In the "Targets" section, make sure the "Specified target tags" option is selected.
   - In the "Target tags" field, enter the tags of the VMs that you want to grant access to port 9000. 
   - In the "Source IP ranges" section, leave the value as "0.0.0.0/0" to allow access from all IP addresses.
   - In the "Protocols and ports" section, select the "Specified protocols and ports" option.
   - In the "Protocols and ports" field, enter "tcp:9000" to allow TCP connections to port 9000.
   - Click the "Create" button to create the second firewall rule.

## Creating Cloud Storage
1. Open the GCP console and log in to the desired project.
2. In the left panel, select "Storage" -> "Storage".
3. Click the "Create Bucket" button to create a bucket:
   - On the "Create a bucket" page, name it "agroaid-bucket".
   - Select the storage location "asia-southeast2".
   - Select the "Standard" storage class.
   - Leave the "Fine-grained" option under "Access control" unchecked, unless you need more detailed access settings.
   - Click the "Create" button to create the bucket.

5. Create a service account and assign it the Object Storage Admin role:

   - Go back to the GCP console.
   - In the left pane, select "IAM & Admin" -> "Service Accounts".
   - Find the service account with the name "cloud-storage-admin" or create a new service account with that name.
   - Click on the relevant service account name.
   - On the "Permissions" tab, click the "Add Member" button.
   - Enter the service account email into the "New members" field.
   - Select the "Object Storage Admin" role from the list of available roles.
   - Click the "Save" button to assign the role to the service account.

6. Generate keys for the service account:
   - In the "Keys" tab, click the "Add Key" button and select the "Create new key" option.
   - Select the desired key format, for example "JSON".
   - Click the "Create" button to generate the key.
   - The JSON key will be downloaded to your device. Keep this key safe, as it will be used for authentication when accessing Cloud Storage through the service account.
