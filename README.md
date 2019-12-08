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
 [ http://127.0.0.1:8000/api/v1/address/getlistofaddress/ ]
 Use the above api with Get request.
