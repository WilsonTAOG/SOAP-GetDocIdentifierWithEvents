import xml.etree.ElementTree as ET

def parse_soap_response(response_xml):
    namespace = {'soap': 'http://www.w3.org/2003/05/soap-envelope', 'wcf': 'http://wcf.dian.colombia'}
    root = ET.fromstring(response_xml)

    track_id = root.find('.//wcf:TrackId', namespace)
    events = root.findall('.//wcf:Event', namespace)

    if track_id is not None:
        print(f"TrackId: {track_id.text}")

    for event in events:
        event_type = event.find('wcf:EventType', namespace).text
        event_date = event.find('wcf:EventDate', namespace).text
        event_details = event.find('wcf:EventDetails', namespace).text
        print(f"EventType: {event_type}, EventDate: {event_date}, EventDetails: {event_details}")
