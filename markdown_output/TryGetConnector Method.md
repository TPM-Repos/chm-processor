![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetConnector Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3109.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupConnectors Class](topic3097.md) : TryGetConnector Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_connectorName_
    The name of the connector to find.

_connector_
    Reference to set to the found connector, if it's found.

Glossary Item Box

Attempts to find a connector with the specified name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetConnector( _
       ByVal _connectorName_ As String, _
       ByRef _connector_ As [GroupConnectorInformation](topic3084.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupConnectors](topic3097.md)
    Dim connectorName As String
    Dim connector As [GroupConnectorInformation](topic3084.md)
    Dim value As Boolean
     
    value = instance.TryGetConnector(connectorName, connector)  
  
C#|   
---|---  
      
    
    public bool TryGetConnector( 
       string _connectorName_ ,
       ref [GroupConnectorInformation](topic3084.md) _connector_
    )  
  
#### Parameters

 _connectorName_
    The name of the connector to find.
_connector_
    Reference to set to the found connector, if it's found.

#### Return Value

True if the connector was found.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupConnectors Class](topic3097.md)   
[GroupConnectors Members](topic3098.md)

©2024 DriveWorks Ltd. All Rights Reserved.
