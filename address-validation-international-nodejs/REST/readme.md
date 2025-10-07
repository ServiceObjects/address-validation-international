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
//        administrativeArea
//        postalCode
//        country
//        outputLanguage 
//        licenseKey
//        isLive
//        timeoutSeconds

import { GetAddressInfoClient } from '../address-validation-international-nodejs/REST/get_address_info_rest.js';

const address1 = "27 E Cota St";
const address2 = "Ste 500";
const address3 = "";
const address4 = "";
const address5 = "";
const locality = "Santa Barbara";
const administrativeArea = "CA";
const postalCode = "93101";
const country = "USA";
const outputLanguage = "English";
const isLive = true;
const licenseKey = "YOUR LICENSE KEY";
const timeoutSeconds = 15;

// 2. Call the sync Invoke() method.
const response = await GetAddressInfoClient.invoke(
    address1,
    address2,
    address3,
    address4,
    address5,
    locality,
    administrativeArea,
    postalCode,
    country,
    outputLanguage,
    licenseKey,
    isLive,
    timeoutSeconds
);

// 3. Inspect results.
if (response.Error) 
{
    console.log("\n* Error *\n");
    console.log(`Error Type    : ${response.Error.Type}`);
    console.log(`Error TypeCode: ${response.Error.TypeCode}`);
    console.log(`Error Desc    : ${response.Error.Desc}`);
    console.log(`Error DescCode: ${response.Error.DescCode}`);
    return;
}

console.log("\n* Address Info *\n");
if (response && response.AddressInfo) 
{
    console.log(`Status            : ${response.AddressInfo.Status}`);
    console.log(`ResolutionLevel   : ${response.AddressInfo.ResolutionLevel}`);
    console.log(`Address1          : ${response.AddressInfo.Address1}`);
    console.log(`Address2          : ${response.AddressInfo.Address2}`);
    console.log(`Address3          : ${response.AddressInfo.Address3}`);
    console.log(`Address4          : ${response.AddressInfo.Address4}`);
    console.log(`Address5          : ${response.AddressInfo.Address5}`);
    console.log(`Address6          : ${response.AddressInfo.Address6}`);
    console.log(`Address7          : ${response.AddressInfo.Address7}`);
    console.log(`Address8          : ${response.AddressInfo.Address8}`);
    console.log(`Locality          : ${response.AddressInfo.Locality}`);
    console.log(`AdministrativeArea: ${response.AddressInfo.AdministrativeArea}`);
    console.log(`PostalCode        : ${response.AddressInfo.PostalCode}`);
    console.log(`Country           : ${response.AddressInfo.Country}`);
    console.log(`CountryISO2       : ${response.AddressInfo.CountryISO2}`);
    console.log(`CountryISO3       : ${response.AddressInfo.CountryISO3}`);

    console.log("\n* Information Components *\n");
    if (response.AddressInfo.InformationComponents && response.AddressInfo.InformationComponents.length > 0)
    {
        response.AddressInfo.InformationComponents.forEach((component) => {
            console.log(`${component.Name}: ${component.Value}`);
        });
    }
    else
    {
        console.log("No information components found.");
    }
} 
else
{
    console.log("No address info found.");
}
```
