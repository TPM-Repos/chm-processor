       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Store(GroupConnectorInformation) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3107.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupConnectors Class](topic3097.md) > [Store Method](topic3106.md) : Store(GroupConnectorInformation) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_connector_
    The details to update.

Glossary Item Box

Adds or updates the specified details to the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub Store( _
       ByVal _connector_ As [GroupConnectorInformation](topic3084.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupConnectors](topic3097.md)
    Dim connector As [GroupConnectorInformation](topic3084.md)
     
    instance.Store(connector)  
  
C#|   
---|---  
      
    
    public void Store( 
       [GroupConnectorInformation](topic3084.md) _connector_
    )  
  
#### Parameters

 _connector_
    The details to update.

# Remarks

This will also perform name validation to ensure that the name of the connector is distinct.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupConnectors Class](topic3097.md)   
[GroupConnectors Members](topic3098.md)   
[Overload List](topic3106.md)

©2024 DriveWorks Ltd. All Rights Reserved.
