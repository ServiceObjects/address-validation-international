![Service Objects Logo](https://www.serviceobjects.com/wp-content/uploads/2021/05/SO-Logo-with-TM.gif "Service Objects Logo")

# AVI - Address Validation International

DOTS Address Validation International (AVI) can be used as a RESTful service or with SOAP. AVI is designed to take an international address, validate it and return a standardized international version of the address. Depending on the information available for a given address, AVI can return additional information about a given address. For example, it can return Delivery Point Validation (DPV) information for US addresses.

AVI can provide instant address verification and correction to websites or enhancement to contact lists. However, the output from AVI must be considered carefully before the existence or non-existence of an address is decided

## [Service Objects Website](https://serviceobjects.com)

# AVI - GetAddressInfo

Our real-time International Address Validation API service verifies and corrects global mailing addresses to the unique requirements of each country’s postal address formats and cultural idiosyncrasies. 

With continual updates from country-specific postal authorities, our data is always up-to-date with genuine and accurate addresses.

### [GetAddressInfo Developer Guide/Documentation](https://www.serviceobjects.com/docs/dots-address-validation-international/avi-operations/avi-getaddressinfo-recommended/)

## Library Usage

```
// 1. Build the input
//
//  Fields:
//        address1
//        address2
//        address3
//        address4
//        address5
//        locality
//        administrative_area
//        postal_code
//        country
//        output_language 
//        license_key
//        is_live 

from get_address_info_soap import GetAddressInfoSoap

address1 = "27 E Cota St"
address2 = "Ste 500"
address3 = ""
address4 = ""
address5 = ""
locality = "Santa Barbara"
administrative_area = "CA"
postal_code = "93101"
country = "USA"
output_language = "English"
timeout_seconds = 10
is_live = True
license_key = "YOUR LICENSE KEY"


// 2. Call the method.
service = GetAddressInfoSoap(license_key, is_live, timeout_seconds * 1000)
response = service.get_address_info(
    address1,
    address2,
    address3,
    address4,
    address5,
    locality,
    administrative_area,
    postal_code,
    country,
    output_language
)

// 3. Inspect results.
if not hasattr(response, 'Error') or not response.Error:
    print("\r\n* Address Info *\r\n")
    if hasattr(response, 'AddressInfo') and response.AddressInfo:
        print(f"Status            : {getattr(response.AddressInfo, 'Status', None)}")
        print(f"ResolutionLevel   : {getattr(response.AddressInfo, 'ResolutionLevel', None)}")
        print(f"Address1          : {getattr(response.AddressInfo, 'Address1', None)}")
        print(f"Address2          : {getattr(response.AddressInfo, 'Address2', None)}")
        print(f"Address3          : {getattr(response.AddressInfo, 'Address3', None)}")
        print(f"Address4          : {getattr(response.AddressInfo, 'Address4', None)}")
        print(f"Address5          : {getattr(response.AddressInfo, 'Address5', None)}")
        print(f"Address6          : {getattr(response.AddressInfo, 'Address6', None)}")
        print(f"Address7          : {getattr(response.AddressInfo, 'Address7', None)}")
        print(f"Address8          : {getattr(response.AddressInfo, 'Address8', None)}")
        print(f"Locality          : {getattr(response.AddressInfo, 'Locality', None)}")
        print(f"AdministrativeArea: {getattr(response.AddressInfo, 'AdministrativeArea', None)}")
        print(f"PostalCode        : {getattr(response.AddressInfo, 'PostalCode', None)}")
        print(f"Country           : {getattr(response.AddressInfo, 'Country', None)}")
        print(f"CountryISO2       : {getattr(response.AddressInfo, 'CountryISO2', None)}")
        print(f"CountryISO3       : {getattr(response.AddressInfo, 'CountryISO3', None)}")

        print("\r\n* Information Components *\r\n")
        if hasattr(response.AddressInfo, 'InformationComponents') and response.AddressInfo.InformationComponents:
            components = response.AddressInfo.InformationComponents.InformationComponent
            if not isinstance(components, list):
                components = [components]
            for component in components:
                print(f"{getattr(component, 'Name', None)}: {getattr(component, 'Value', None)}")
        else:
            print("No information components found.")
    else:
        print("No address info found.")
else:
    print("No address info found.")

if hasattr(response, 'Error') and response.Error:
    print("\r\n* Error *\r\n")
    print(f"Error Type    : {getattr(response.Error, 'Type', None)}")
    print(f"Error TypeCode: {getattr(response.Error, 'TypeCode', None)}")
    print(f"Error Desc    : {getattr(response.Error, 'Desc', None)}")
    print(f"Error DescCode: {getattr(response.Error, 'DescCode', None)}")
```
