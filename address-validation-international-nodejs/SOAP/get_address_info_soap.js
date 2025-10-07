import { soap } from 'strong-soap';

/**
 * <summary>
 * A class that provides functionality to call the ServiceObjects Address Validation International (AVI) SOAP service's GetAddressInfo endpoint,
 * retrieving validated and corrected international address information with fallback to a backup endpoint for reliability in live mode.
 * </summary>
 */
class GetAddressInfoSoap {
    /**
     * <summary>
     * Initializes a new instance of the GetAddressInfoSoap class with the provided input parameters,
     * setting up primary and backup WSDL URLs based on the live/trial mode.
     * </summary>
     * @param {string} Address1 - Address line 1 of the international address.
     * @param {string} Address2 - Address line 2 of the international address. Optional.
     * @param {string} Address3 - Address line 3 of the international address. Optional.
     * @param {string} Address4 - Address line 4 of the international address. Optional.
     * @param {string} Address5 - Address line 5 of the international address. Optional.
     * @param {string} Locality - The city, town, or municipality of the address. Required if postal code is not provided.
     * @param {string} AdministrativeArea - The state, region, or province of the address. Required if postal code is not provided.
     * @param {string} PostalCode - The postal code of the address. Required if locality and administrative area are not provided.
     * @param {string} Country - The country name or ISO 3166-1 Alpha-2/Alpha-3 code.
     * @param {string} OutputLanguage - The language for service output (e.g., "ENGLISH", "BOTH", "LOCAL_ROMAN", "LOCAL").
     * @param {string} LicenseKey - Your license key to use the service.
     * @param {boolean} isLive - Value to determine whether to use the live or trial servers.
     * @param {number} timeoutSeconds - Timeout, in seconds, for the call to the service.
     * @throws {Error} Thrown if LicenseKey is empty or null.
     */
    constructor(Address1, Address2, Address3, Address4, Address5, Locality, AdministrativeArea, PostalCode, Country, OutputLanguage, LicenseKey, isLive = true, timeoutSeconds = 15) {
        if (!LicenseKey) {
            throw new Error('LicenseKey cannot be empty or null.');
        }

        this.args = {
            Address1,
            Address2,
            Address3,
            Address4,
            Address5,
            Locality,
            AdministrativeArea,
            PostalCode,
            Country,
            OutputLanguage,
            LicenseKey
        };

        this.isLive = isLive;
        this.timeoutSeconds = timeoutSeconds;

        this.LiveBaseUrl = 'https://sws.serviceobjects.com/avi/soap.svc?wsdl';
        this.BackupBaseUrl = 'https://swsbackup.serviceobjects.com/avi/soap.svc?wsdl';
        this.TrialBaseUrl = 'https://trial.serviceobjects.com/avi/soap.svc?wsdl';

        this._primaryWsdl = this.isLive ? this.LiveBaseUrl : this.TrialBaseUrl;
        this._backupWsdl = this.isLive ? this.BackupBaseUrl : this.TrialBaseUrl;
    }

    /**
     * <summary>
     * Asynchronously calls the GetAddressInfo SOAP endpoint, attempting the primary endpoint
     * first and falling back to the backup if the response is invalid (Error.TypeCode == '3') in live mode
     * or if the primary call fails.
     * </summary>
     * @returns {Promise<Object>} A promise that resolves to an object containing validated address details or an error.
     * @throws {Error} Thrown if both primary and backup calls fail, with detailed error messages.
     */
    async invokeAsync() {
        try {
            const primaryResult = await this._callSoap(this._primaryWsdl, this.args);

            if (this.isLive && !this._isValid(primaryResult)) {
                console.warn("Primary returned Error.TypeCode == '3', falling back to backup...");
                const backupResult = await this._callSoap(this._backupWsdl, this.args);
                return backupResult;
            }

            return primaryResult;
        } catch (primaryErr) {
            try {
                const backupResult = await this._callSoap(this._backupWsdl, this.args);
                return backupResult;
            } catch (backupErr) {
                throw new Error(`Both primary and backup calls failed:\nPrimary: ${primaryErr.message}\nBackup: ${backupErr.message}`);
            }
        }
    }

    /**
     * <summary>
     * Performs a SOAP service call to the specified WSDL URL with the given arguments,
     * creating a client and returning the raw SOAP response data.
     * </summary>
     * @param {string} wsdlUrl - The WSDL URL of the SOAP service endpoint (primary or backup).
     * @param {Object} args - The arguments to pass to the GetAddressInfo method.
     * @returns {Promise<Object>} A promise that resolves to the raw SOAP response data.
     * @throws {Error} Thrown if the SOAP client creation fails, the service call fails, or the response cannot be parsed.
     */
    _callSoap(wsdlUrl, args) {
        return new Promise((resolve, reject) => {
            soap.createClient(wsdlUrl, { timeout: this.timeoutSeconds * 1000 }, (err, client) => {
                if (err) return reject(err);

                client.GetAddressInfo(args, (err, result) => {
                    const response = result?.GetAddressInfoResult;
                    try {
                        if (!response) {
                            return reject(new Error("SOAP response is empty or undefined."));
                        }
                        resolve(response);
                    } catch (parseErr) {
                        reject(new Error(`Failed to parse SOAP response: ${parseErr.message}`));
                    }
                });
            });
        });
    }

    /**
     * <summary>
     * Checks if a SOAP response is valid by verifying that it exists and either has no Error object
     * or the Error.TypeCode is not equal to '3'.
     * </summary>
     * @param {Object} response - The response object to validate.
     * @returns {boolean} True if the response is valid, false otherwise.
     */
    _isValid(response) {
        return response && (!response.Error || response.Error.TypeCode !== '3');
    }
}

export { GetAddressInfoSoap };