import xml.etree.ElementTree as ET

# El XML proporcionado
xml_data = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://itau.com.co/services/accounts/accountdetailsbyid/v1/schemas" xmlns:sch1="http://itau.com.co/commoncannonical/v2/schemas">
  <soapenv:Header/>
  <soapenv:Body>
   <sch:getAccountDetailsByIdRq>
     <sch:HeaderRequest>
      <sch1:MessageHeader>
        <sch1:MessageKey>
         <sch1:integrationId>?</sch1:integrationId>
         <sch1:requestVersion>?</sch1:requestVersion>
         <sch1:requestUUID>?</sch1:requestUUID>
        </sch1:MessageKey>
        <sch1:MessageInfo>
         <sch1:dateTime>?</sch1:dateTime>
         <sch1:systemId>?</sch1:systemId>
         <sch1:originatorName>?</sch1:originatorName>
         <sch1:originatorType>?</sch1:originatorType>
         <sch1:terminalId>?</sch1:terminalId>
         <sch1:terminalType>?</sch1:terminalType>
         <sch1:bankIdType>?</sch1:bankIdType>
         <sch1:bankId>?</sch1:bankId>
         <sch1:trnType>?</sch1:trnType>
        </sch1:MessageInfo>
        <sch1:TrnInfoList>
         <sch1:TrnInfo>
           <sch1:trnCode>?</sch1:trnCode>
           <sch1:trnSrc>?</sch1:trnSrc>
         </sch1:TrnInfo>
        </sch1:TrnInfoList>
      </sch1:MessageHeader>
      <sch1:User>
        <sch1:userName>?</sch1:userName>
        <sch1:userToken>?</sch1:userToken>
        <sch1:employeeIdentlNum>?</sch1:employeeIdentlNum>
      </sch1:User>
     </sch:HeaderRequest>
     <sch:custId>
      <sch1:SPName>?</sch1:SPName>
      <sch1:custPermId>?</sch1:custPermId>
      <sch1:custLoginId>?</sch1:custLoginId>
      <sch1:custType>?</sch1:custType>
     </sch:custId>
     <sch:acctType>?</sch:acctType>
     <sch:acctSubType>?</sch:acctSubType>
     <sch:acctId>?</sch:acctId>
     <sch:branchId>?</sch:branchId>
   </sch:getAccountDetailsByIdRq>
  </soapenv:Body>
</soapenv:Envelope>'''

# Parse the XML
root = ET.fromstring(xml_data)

# Function to remove namespaces
def remove_namespace(element):
    for elem in element.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]  # Remove namespace
        for attr in elem.attrib:
            if '}' in attr:
                new_attr = attr.split('}', 1)[1]
                elem.attrib[new_attr] = elem.attrib.pop(attr)

# Remove namespaces from the XML
remove_namespace(root)

# Get the modified XML as a string
xml_str = ET.tostring(root, encoding='unicode')

# Write the modified XML to a file
with open("xml_without_namespaces.xml", "w") as file:
    file.write(xml_str)

print("XML sin namespaces exportado a 'xml_without_namespaces.xml'")
