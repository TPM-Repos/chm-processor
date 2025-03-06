Remove Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupConnectors Class](topic3097.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_connector_
    The connector to remove.

Glossary Item Box

Removes the specified connector from the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Remove( _
       ByVal _connector_ As [GroupConnectorInformation](topic3084.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupConnectors](topic3097.md)
    Dim connector As [GroupConnectorInformation](topic3084.md)
    Dim value As Boolean
     
    value = instance.Remove(connector)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [GroupConnectorInformation](topic3084.md) _connector_
    )  
  
#### Parameters

 _connector_
    The connector to remove.

#### Return Value

True if the specified connector was removed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupConnectors Class](topic3097.md)   
[GroupConnectors Members](topic3098.md)


