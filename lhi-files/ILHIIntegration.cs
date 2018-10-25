using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace LawHelpInteractive.LHIIntegrationService
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the interface name "ILHIIntegration" in both code and config file together.
    [ServiceContract]
    public interface ILHIIntegration
    {
        [OperationContract]
        ReturnInfo GetAnswersAndDocuments(DownloadRequest request);
    }

    [MessageContract]
    public class DownloadRequest
    {
        [MessageBodyMember]
        public string CustomerKey;

        [MessageBodyMember]
        public string ProcessSet;

        [MessageBodyMember]
        public string TemplateId;


        [MessageBodyMember]
        public string DocID;

        [MessageBodyMember]
        public string HDInfo;

        [MessageBodyMember]
        public string PostBackUrl;
    }
 [MessageContract]
    public class ReturnInfo
    {
        [MessageBodyMember]
        public string ResponseString; 
    }
}
