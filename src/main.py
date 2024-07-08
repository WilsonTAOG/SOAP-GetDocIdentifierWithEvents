from src.soap_request import send_soap_request
from src.soap_response import parse_soap_response

def main():
    contributor_code = "123456"
    date_number = "20240101"

    response_xml = send_soap_request(contributor_code, date_number)
    if response_xml:
        parse_soap_response(response_xml)

if __name__ == "__main__":
    main()
