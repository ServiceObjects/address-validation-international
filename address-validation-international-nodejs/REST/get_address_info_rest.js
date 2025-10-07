import axios from 'axios';
import querystring from 'querystring';
import { AddressInfoResponse } from './avi_response.js';

/**
 * @constant
 * @type {string}
 * @description The base URL for the live ServiceObjects Address Validation International (AVI) API service.
 */
const LiveBaseUrl = 'https://sws.serviceobjects.com/avi/api.svc/json/';

/**
 * @constant
 * @type {string}
 * @description The base URL for the backup ServiceObjects Address Validation International (AVI) API service.
 */
const BackupBaseUrl = 'https://swsbackup.serviceobjects.com/avi/api.svc/json/';

/**
 * @constant
 * @type {string}
 * @description The base URL for the trial ServiceObjects Address Validation International (AVI) API service.
 */
const TrialBaseUrl = 'https://trial.serviceobjects.com/avi/api.svc/json/';

/**
 * <summary>
 * Checks if a response from the API is valid by verifying that it either has no Error object
 * or the Error.TypeCode is not equal to '3'.
 * </summary>
 * <param name="response" type="Object">The API response object to validate.</param>
 * <returns type="boolean">True if the response is valid, false otherwise.</returns>
 */
const isValid = (response) => !response?.Error || response.Error.TypeCode !== '3';

/**
 * <summary>
 * Constructs a full URL for the GetAddressInfo API endpoint by combining the base URL
 * with query parameters derived from the input parameters.
 * </summary>
 * <param name="params" type="Object">An object containing all the input parameters.</param>
 * <param name="baseUrl" type="string">The base URL for the API service (live, backup, or trial).</param>
 * <returns type="string">The constructed URL with query parameters.</returns>
 */
const buildUrl = (params, baseUrl) =>
    `${baseUrl}GetAddressInfo?${querystring.stringify(params)}`;

/**
 * <summary>
 * Performs an HTTP GET request to the specified URL with a given timeout.
 * </summary>
 * <param name="url" type="string">The URL to send the GET request to.</param>
 * <param name="timeoutSeconds" type="number">The timeout duration in seconds for the request.</param>
 * <returns type="Promise<AddressInfoResponse>">A promise that resolves to an AddressInfoResponse object containing the API response data.</returns>
 * <exception cref="Error">Thrown if the HTTP request fails, with a message detailing the error.</exception>
 */
const httpGet = async (url, timeoutSeconds) => {
    try {
        const response = await axios.get(url, { timeout: timeoutSeconds * 1000 });
        return new AddressInfoResponse(response.data);
    } catch (error) {
        throw new Error(`HTTP request failed: ${error.message}`);
    }
};

/**
 * <summary>
 * Provides functionality to call the ServiceObjects Address Validation International (AVI) API's GetAddressInfo endpoint,
 * retrieving validated and corrected international address information with fallback to a backup endpoint for reliability in live mode.
 * </summary>
 */
const GetAddressInfoClient = {
    /**
     * <summary>
     * Asynchronously invokes the GetAddressInfo API endpoint, attempting the primary endpoint
     * first and falling back to the backup if the response is invalid (Error.TypeCode == '3') in live mode.
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
     * @returns {Promise<AddressInfoResponse>} - A promise that resolves to an AddressInfoResponse object.
     */
    async invokeAsync(Address1, Address2, Address3, Address4, Address5, Locality, AdministrativeArea, PostalCode, Country, OutputLanguage, LicenseKey, isLive = true, timeoutSeconds = 15) {
        const params = {
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

        const url = buildUrl(params, isLive ? LiveBaseUrl : TrialBaseUrl);
        let response = await httpGet(url, timeoutSeconds);

        if (isLive && !isValid(response)) {
            const fallbackUrl = buildUrl(params, BackupBaseUrl);
            const fallbackResponse = await httpGet(fallbackUrl, timeoutSeconds);
            return fallbackResponse;
        }
        return response;
    },

    /**
     * <summary>
     * Synchronously invokes the GetAddressInfo API endpoint by wrapping the async call
     * and awaiting its result immediately.
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
     * @returns {AddressInfoResponse} - An AddressInfoResponse object with validated address details or an error.
     */
    invoke(Address1, Address2, Address3, Address4, Address5, Locality, AdministrativeArea, PostalCode, Country, OutputLanguage, LicenseKey, isLive = true, timeoutSeconds = 15) {
        return (async () => await this.invokeAsync(
            Address1, Address2, Address3, Address4, Address5, Locality, AdministrativeArea, PostalCode, Country, OutputLanguage, LicenseKey, isLive, timeoutSeconds
        ))();
    }
};

export { GetAddressInfoClient, AddressInfoResponse };