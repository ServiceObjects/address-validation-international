using address_validation_international_dot_net_examples;

//Your license key from Service Objects.
//Trial license keys will only work on the
//trail environments and production license
//keys will only work on production environments.
string LicenseKey = "LICENSE KEY";

bool IsProductionKey = true;

//Address Validation International - GetAddressInfo - REST SDK
GetAddressInfoRestSdkExample.Go(LicenseKey, IsProductionKey);

//Address Validation International - GetAddressInfo - SOAP SDK
GetAddressInfoSoapSdkExample.Go(LicenseKey, IsProductionKey);