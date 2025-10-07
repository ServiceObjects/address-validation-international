import {GetAddressInfoRestGo} from './get_address_info_rest_sdk_example.js';
import {GetAddressInfoSoapGo} from './get_address_info_soap_sdk_example.js';

export async function main()
{
    //Your license key from Service Objects.
    //Trial license keys will only work on the
    //trail environments and production license
    //keys will only work on production environments.
    const licenseKey = "LICENSE KEY";
    const isLive = true;

    // Address Validation International - GetAddressInfo - REST SDK
    await GetAddressInfoRestGo(licenseKey, isLive);

    // Address Validation International - GetAddressInfo - SOAP SDK
    await GetAddressInfoSoapGo(licenseKey, isLive);

}
main().catch((error) => {
  console.error("An error occurred:", error);
  process.exit(1);
});