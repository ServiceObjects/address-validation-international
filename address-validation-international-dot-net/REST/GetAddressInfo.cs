
namespace address_validation_international_dot_net.REST
{
    /// <summary>
    /// Provides functionality to call the ServiceObjects Address Validation International (AVI) REST API's GetAddressInfo endpoint,
    /// retrieving validated and corrected international address information with fallback to a backup endpoint for reliability in live mode.
    /// </summary>
    public static class GetAddressInfoClient
    {
        // Base URL constants: production, backup, and trial
        private const string LiveBaseUrl = "https://sws.serviceobjects.com/avi/api.svc/json/";
        private const string BackupBaseUrl = "https://swsbackup.serviceobjects.com/avi/api.svc/json/";
        private const string TrialBaseUrl = "https://trial.serviceobjects.com/avi/api.svc/json/";

        /// <summary>
        /// Synchronously calls the GetAddressInfo REST endpoint to retrieve validated international address information,
        /// attempting the primary endpoint first and falling back to the backup if the response is invalid
        /// (Error.TypeCode == "3") in live mode.
        /// </summary>
        /// <param name="input">The input parameters including address lines, locality, administrative area, postal code, country, output language, and license key.</param>
        /// <returns>Deserialized <see cref="AddressInfoResponse"/> containing validated address data or an error.</returns>
        public static AddressInfoResponse Invoke(GetAddressInfoInput input)
        {
            // Use query string parameters so missing/optional fields don't break the URL
            string url = BuildUrl(input, input.IsLive ? LiveBaseUrl : TrialBaseUrl);
            AddressInfoResponse response = Helper.HttpGet<AddressInfoResponse>(url, input.TimeoutSeconds);

            // Fallback on error in live mode
            if (input.IsLive && !ValidResponse(response))
            {
                string fallbackUrl = BuildUrl(input, BackupBaseUrl);
                AddressInfoResponse fallbackResponse = Helper.HttpGet<AddressInfoResponse>(fallbackUrl, input.TimeoutSeconds);
                return fallbackResponse;
            }

            return response;
        }

        /// <summary>
        /// Asynchronously calls the GetAddressInfo REST endpoint to retrieve validated international address information,
        /// attempting the primary endpoint first and falling back to the backup if the response is invalid
        /// (Error.TypeCode == "3") in live mode.
        /// </summary>
        /// <param name="input">The input parameters including address lines, locality, administrative area, postal code, country, output language, and license key.</param>
        /// <returns>Deserialized <see cref="AddressInfoResponse"/> containing validated address data or an error.</returns>
        public static async Task<AddressInfoResponse> InvokeAsync(GetAddressInfoInput input)
        {
            // Use query string parameters so missing/optional fields don't break the URL
            string url = BuildUrl(input, input.IsLive ? LiveBaseUrl : TrialBaseUrl);
            AddressInfoResponse response = await Helper.HttpGetAsync<AddressInfoResponse>(url, input.TimeoutSeconds).ConfigureAwait(false);

            // Fallback on error in live mode
            if (input.IsLive && !ValidResponse(response))
            {
                string fallbackUrl = BuildUrl(input, BackupBaseUrl);
                AddressInfoResponse fallbackResponse = await Helper.HttpGetAsync<AddressInfoResponse>(fallbackUrl, input.TimeoutSeconds).ConfigureAwait(false);
                return fallbackResponse;
            }

            return response;
        }

        // Build the full request URL, including URL-encoded query string
        public static string BuildUrl(GetAddressInfoInput input, string baseUrl)
        {
            // Construct query string with URL-encoded parameters
            string qs = $"GetAddressInfo?" +
                        $"Address1={Helper.UrlEncode(input.Address1)}" +
                        $"&Address2={Helper.UrlEncode(input.Address2)}" +
                        $"&Address3={Helper.UrlEncode(input.Address3)}" +
                        $"&Address4={Helper.UrlEncode(input.Address4)}" +
                        $"&Address5={Helper.UrlEncode(input.Address5)}" +
                        $"&Locality={Helper.UrlEncode(input.Locality)}" +
                        $"&AdministrativeArea={Helper.UrlEncode(input.AdministrativeArea)}" +
                        $"&PostalCode={Helper.UrlEncode(input.PostalCode)}" +
                        $"&Country={Helper.UrlEncode(input.Country)}" +
                        $"&OutputLanguage={Helper.UrlEncode(input.OutputLanguage)}" +
                        $"&LicenseKey={Helper.UrlEncode(input.LicenseKey)}";
            return baseUrl + qs;
        }

        /// <summary>
        /// Validates the API response to determine if it is successful or requires a fallback.
        /// </summary>
        /// <param name="response">The API response to validate.</param>
        /// <returns>True if the response is valid (no error or TypeCode != "3"), false otherwise.</returns>
        private static bool ValidResponse(AddressInfoResponse response)
        {
            return response?.Error == null || response.Error.TypeCode != "3";
        }

        /// <summary>
        /// Input parameters for the GetAddressInfo API call. Represents an international address to validate and correct.
        /// </summary>
        /// <param name="Address1">Address line 1 of the international address.</param>
        /// <param name="Address2">Address line 2 of the international address. Optional.</param>
        /// <param name="Address3">Address line 3 of the international address. Optional.</param>
        /// <param name="Address4">Address line 4 of the international address. Optional.</param>
        /// <param name="Address5">Address line 5 of the international address. Optional.</param>
        /// <param name="Locality">The city, town, or municipality of the address. Required if postal code is not provided.</param>
        /// <param name="AdministrativeArea">The state, region, or province of the address. Required if postal code is not provided.</param>
        /// <param name="PostalCode">The postal code of the address. Required if locality and administrative area are not provided.</param>
        /// <param name="Country">The country name or ISO 3166-1 Alpha-2/Alpha-3 code.</param>
        /// <param name="OutputLanguage">The language for service output (e.g., "ENGLISH", "BOTH", "LOCAL_ROMAN", "LOCAL").</param>
        /// <param name="LicenseKey">The license key to authenticate the API request.</param>
        /// <param name="IsLive">Indicates whether to use the live service (true) or trial service (false).</param>
        /// <param name="TimeoutSeconds">Timeout duration for the API call, in seconds.</param>
        public record GetAddressInfoInput(
            string Address1 = "",
            string Address2 = "",
            string Address3 = "",
            string Address4 = "",
            string Address5 = "",
            string Locality = "",
            string AdministrativeArea = "",
            string PostalCode = "",
            string Country = "",
            string OutputLanguage = "",
            string LicenseKey = "",
            bool IsLive = true,
            int TimeoutSeconds = 15
        );
    }
}