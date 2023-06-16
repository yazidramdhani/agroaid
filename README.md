# agroaid
penjelasan singkat

## Training the Model
ini di isi anak ml aja

## Creating VM instances 
step2 kita buat vm di gcp. Kita buat 2 vm ada yang e2-small buat nodejs dan mysql, terus tambahin tag allow-9000 & e2-standard-2 buat flask (aplikasi machine learning), terus tambahin tag allow-5000 <br /> 
(disini kalo mau cek https://console.cloud.google.com/compute/instances?authuser=2&project=agroaid )

## Creating Firewall Ruke
step2 buat firewall allow-5000 & allow-9000 <br /> 
(disini kalo mau cek  https://console.cloud.google.com/networking/firewalls/list?authuser=2&project=agroaid )

## Creating Cloud Storage
step2 buat bucket di cloud storage, abis itu buat service-account namanya "cloud-storage-admin" kasih role object storage admin terus di generate key <br /> 
(ini bucket https://console.cloud.google.com/storage/browser?authuser=2&project=agroaid)<br /> 
(ini service account https://console.cloud.google.com/iam-admin/serviceaccounts/details/109685645670431171558?authuser=2&project=agroaid)
