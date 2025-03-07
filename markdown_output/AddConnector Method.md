Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddConnector Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupConnectors Class](topic3097.md) : AddConnector Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name to give the new connector.

_connectorDataType_
    The type of the connector's data storage class.

Glossary Item Box

Adds a connector of the specified type to the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddConnector( _
       ByVal _name_ As String, _
       ByVal _connectorDataType_ As Type _
    ) As [GroupConnectorInformation](topic3084.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupConnectors](topic3097.md)
    Dim name As String
    Dim connectorDataType As Type
    Dim value As [GroupConnectorInformation](topic3084.md)
     
    value = instance.AddConnector(name, connectorDataType)  
  
C#|   
---|---  
      
    
    public [GroupConnectorInformation](topic3084.md) AddConnector( 
       string _name_ ,
       Type _connectorDataType_
    )  
  
#### Parameters

 _name_
    The name to give the new connector.
_connectorDataType_
    The type of the connector's data storage class.

#### Return Value

The created connector.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupConnectors Class](topic3097.md)   
[GroupConnectors Members](topic3098.md)


