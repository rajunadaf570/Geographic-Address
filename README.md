# Geographic-Address
    Geographic-Address use Place specifications to define geographic entities that where you can located on map.
    
## How to use: 
### API 1.
 [ http://127.0.0.1:8000/api/v1/address/fileupload/ ]\
 Call the above api using post request.
 #### Input:
 key :  { API Key } locationiq api key.\
 file : { csv or excel file } with address field.\
 for example use above { address.xlsx } excel file for reference.
 #### response:
 detail : file uploaded successfully.
 ### API 2.
 [ http://127.0.0.1:8000/api/v1/address/getlistofaddress/ ]\
 Use the above api with Get request.\
 This Api use to get all the records.
 #### API 3.
 [ http://127.0.0.1:8000/api/v1/address/deletealladdress/ ]\
 Use the above api with delete request.\
 This can be used to delete all the records, address field latitude and longitude.
 #### API 4.
 [ http://127.0.0.1:8000/api/v1/address/downloadfile/ ]\
 Get request.\
 Download csv file which contain address filed with latitude and longitude fields.
 
 
 
