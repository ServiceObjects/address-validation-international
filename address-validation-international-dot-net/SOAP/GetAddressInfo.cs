using System;
using System.Threading.Tasks;
using AVIReference;

namespace address_validation_international_dot_net.SOAP
{
    /// <summary>
    /// Provides functionality to call the ServiceObjects Address Validation International (AVI) SOAP service's GetAddressInfo operation,
    /// retrieving validated and corrected international address information with fallback to a backup endpoint for reliability in live mode.
    /// </summary>
    public class GetAddressInfoValidation
    {
        private const string LiveBaseUrl = "https://sws.serviceobjects.com/avi/soap.svc/SOAP";
        private const string BackupBaseUrl = "https://swsbackup.serviceobjects.com/avi/soap.svc/SOAP";
        private const string TrialBaseUrl = "https://trial.serviceobjects.com/avi/soap.svc/SOAP";

        private readonly string _primaryUrl;
        private readonly string _backupUrl;
        private readonly int _timeoutMs;
        private readonly bool _isLive;

        /// <summary>
        /// Initializes URLs, timeout, and IsLive.
        /// </summary>
        public GetAddressInfoValidation(bool isLive)
        {
            _timeoutMs = 10000;
            _isLive = isLive;

            _primaryUrl = isLive ? LiveBaseUrl : TrialBaseUrl;
            _backupUrl = isLive ? BackupBaseUrl : TrialBaseUrl;

            if (string.IsNullOrWhiteSpace(_primaryUrl))
                throw new InvalidOperationException("Primary URL not set.");
            if (string.IsNullOrWhiteSpace(_backupUrl))
                throw new InvalidOperationException("Backup URL not set.");
        }

        /// <summary>
        /// This operation returns validated and corrected international address information for a given address,
        /// including formatted address lines, locality, administrative area, postal code, country details, and additional information components.
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
        public async Task<AddressInfoResponse> GetAddressInfo(string Address1, string Address2, string Address3, string Address4, string Address5, string Locality, string AdministrativeArea, string PostalCode, string Country, string OutputLanguage, string LicenseKey)
        {
            AVISoapServiceClient clientPrimary = null;
            AVISoapServiceClient clientBackup = null;

            try
            {
                // Attempt Primary
                clientPrimary = new AVISoapServiceClient();
                clientPrimary.Endpoint.Address = new System.ServiceModel.EndpointAddress(_primaryUrl);
                clientPrimary.InnerChannel.OperationTimeout = TimeSpan.FromMilliseconds(_timeoutMs);

                AddressInfoResponse response = await clientPrimary.GetAddressInfoAsync(
                    Address1, Address2, Address3, Address4, Address5, Locality, AdministrativeArea, PostalCode, Country, OutputLanguage, LicenseKey).ConfigureAwait(false);

                if (_isLive && !ValidResponse(response))
                {
                    throw new InvalidOperationException("Primary endpoint returned null or a fatal TypeCode=3 error for GetAddressInfo");
                }
                return response;
            }
            catch (Exception primaryEx)
            {
                try
                {
                    clientBackup = new AVISoapServiceClient();
                    clientBackup.Endpoint.Address = new System.ServiceModel.EndpointAddress(_backupUrl);
                    clientBackup.InnerChannel.OperationTimeout = TimeSpan.FromMilliseconds(_timeoutMs);

                    return await clientBackup.GetAddressInfoAsync(
                        Address1, Address2, Address3, Address4, Address5, Locality, AdministrativeArea, PostalCode, Country, OutputLanguage, LicenseKey).ConfigureAwait(false);
                }
                catch (Exception backupEx)
                {
                    throw new InvalidOperationException(
                        $"Both primary and backup endpoints failed.\n" +
                        $"Primary error: {primaryEx.Message}\n" +
                        $"Backup error: {backupEx.Message}");
                }
                finally
                {
                    clientBackup?.Close();
                }
            }
            finally
            {
                clientPrimary?.Close();
            }
        }
        private static bool ValidResponse(AddressInfoResponse response)
        {
            return response?.Error == null || response.Error.TypeCode != "3";
        }
    }
}