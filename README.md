![Service Objects Logo](https://www.serviceobjects.com/wp-content/uploads/2021/05/SO-Logo-with-TM.gif "Service Objects Logo")

# AVI - Address Validation International

DOTS Address Validation International (AVI) can be used as a RESTful service or with SOAP. AVI is designed to take an international address, validate it and return a standardized international version of the address. Depending on the information available for a given address, AVI can return additional information about a given address. For example, it can return Delivery Point Validation (DPV) information for US addresses.

AVI can provide instant address verification and correction to websites or enhancement to contact lists. However, the output from AVI must be considered carefully before the existence or non-existence of an address is decided

## [Service Objects Website](https://serviceobjects.com)
## [Developer Guide/Documentation](https://www.serviceobjects.com/docs/)

# AVI - GetAddressInfo

Our real-time International Address Validation API service verifies and corrects global mailing addresses to the unique requirements of each country’s postal address formats and cultural idiosyncrasies. With continual updates from country-specific postal authorities, our data is always up-to-date with genuine and accurate addresses.

## [GetAddressInfo Developer Guide/Documentation](https://www.serviceobjects.com/docs/dots-address-validation-international/avi-operations/avi-getaddressinfo-recommended/)

## GetAddressInfo Request URLs (Query String Parameters)

>[!CAUTION]
>### *Important - Use query string parameters for all inputs.  Do not use path parameters since it will lead to errors due to optional parameters and special character issues.*


### JSON
#### Trial

https://trial.serviceobjects.com/AVI/api.svc/json/GetAddressInfo?Address1=27+E+Cota+St&Address2=Ste+500&Address3=&Address4=&Address5=&Locality=Santa+Barbara&AdministrativeArea=CA&PostalCode=93101&Country=USA&OutputLanguage=ENGLISH&LicenseKey={LicenseKey}

#### Production

https://sws.serviceobjects.com/AVI/api.svc/json/GetAddressInfo?Address1=27+E+Cota+St&Address2=Ste+500&Address3=&Address4=&Address5=&Locality=Santa+Barbara&AdministrativeArea=CA&PostalCode=93101&Country=USA&OutputLanguage=ENGLISH&LicenseKey={LicenseKey}

#### Production Backup

https://swsbackup.serviceobjects.com/AVI/api.svc/json/GetAddressInfo?Address1=27+E+Cota+St&Address2=Ste+500&Address3=&Address4=&Address5=&Locality=Santa+Barbara&AdministrativeArea=CA&PostalCode=93101&Country=USA&OutputLanguage=ENGLISH&LicenseKey={LicenseKey}

### XML
#### Trial

https://trial.serviceobjects.com/AVI/api.svc/xml/GetAddressInfo?Address1=27+E+Cota+St&Address2=Ste+500&Address3=&Address4=&Address5=&Locality=Santa+Barbara&AdministrativeArea=CA&PostalCode=93101&Country=USA&OutputLanguage=ENGLISH&LicenseKey={LicenseKey}

#### Production

https://sws.serviceobjects.com/AVI/api.svc/xml/GetAddressInfo?Address1=27+E+Cota+St&Address2=Ste+500&Address3=&Address4=&Address5=&Locality=Santa+Barbara&AdministrativeArea=CA&PostalCode=93101&Country=USA&OutputLanguage=ENGLISH&LicenseKey={LicenseKey}

#### Production Backup

https://swsbackup.serviceobjects.com/AVI/api.svc/xml/GetAddressInfo?Address1=27+E+Cota+St&Address2=Ste+500&Address3=&Address4=&Address5=&Locality=Santa+Barbara&AdministrativeArea=CA&PostalCode=93101&Country=USA&OutputLanguage=ENGLISH&LicenseKey={LicenseKey}
