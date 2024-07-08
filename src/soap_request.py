import requests

def create_soap_request(contributor_code, date_number):
    soap_request = f"""
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:wcf="http://wcf.dian.colombia">
        <soap:Header/>
        <soap:Body>
            <wcf:GetDocIdentifierWithEvents>
                <wcf:contributorCode>{contributor_code}</wcf:contributorCode>
                <wcf:dateNumber>{date_number}</wcf:dateNumber>
            </wcf:GetDocIdentifierWithEvents>
        </soap:Body>
    </soap:Envelope>
    """
    return soap_request

def send_soap_request(contributor_code, date_number):
    url = "https://api.dian.gov.co/soap-endpoint"
    headers = {
        'Content-Type': 'application/soap+xml; charset=utf-8',
        'Authorization': 'Bearer TU_TOKEN_DE_ACCESO'
    }

    soap_request = create_soap_request(contributor_code, date_number)
    response = requests.post(url, headers=headers, data=soap_request)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None
