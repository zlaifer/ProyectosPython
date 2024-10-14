import xml.etree.ElementTree as ET

# El XML proporcionado
xml_data = '''<Envelope>
  <Header />
  <Body>
   <getAccountDetailsByIdRq>
     <HeaderRequest>
      <MessageHeader>
        <MessageKey>
         <integrationId>?</integrationId>
         <requestVersion>?</requestVersion>
         <requestUUID>?</requestUUID>
        </MessageKey>
        <MessageInfo>
         <dateTime>?</dateTime>
         <systemId>?</systemId>
         <originatorName>?</originatorName>
         <originatorType>?</originatorType>
         <terminalId>?</terminalId>
         <terminalType>?</terminalType>
         <bankIdType>?</bankIdType>
         <bankId>?</bankId>
         <trnType>?</trnType>
        </MessageInfo>
        <TrnInfoList>
         <TrnInfo>
           <trnCode>?</trnCode>
           <trnSrc>?</trnSrc>
         </TrnInfo>
        </TrnInfoList>
      </MessageHeader>
      <User>
        <userName>?</userName>
        <userToken>?</userToken>
        <employeeIdentlNum>?</employeeIdentlNum>
      </User>
     </HeaderRequest>
     <custId>
      <SPName>?</SPName>
      <custPermId>?</custPermId>
      <custLoginId>?</custLoginId>
      <custType>?</custType>
     </custId>
     <acctType>?</acctType>
     <acctSubType>?</acctSubType>
     <acctId>?</acctId>
     <branchId>?</branchId>
   </getAccountDetailsByIdRq>
  </Body>
</Envelope>'''

# Parse the XML
root = ET.fromstring(xml_data)

# Recursively get element structure
def get_structure(element, indent=0):
    structure = "  " * indent + element.tag + "\n"
    for child in element:
        structure += get_structure(child, indent + 1)
    return structure

# Get the structure of the XML
structure = get_structure(root)

# Write the structure to a file
with open("xml_structure.txt", "w") as file:
    file.write(structure)

print("Estructura de XML exportada a 'xml_structure.txt'")
