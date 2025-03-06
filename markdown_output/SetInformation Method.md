SetInformation Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IGroupConnector Interface](topic1706.md) : SetInformation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_info_
    The new group connect details for this connector.

Glossary Item Box

Used to inform this connector of it's connector details. This will be called after connector creation and whenever the details are updated. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetInformation( _
       ByVal _info_ As [GroupConnectorInformation](topic3084.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupConnector](topic1706.md)
    Dim info As [GroupConnectorInformation](topic3084.md)
     
    instance.SetInformation(info)  
  
C#|   
---|---  
      
    
    void SetInformation( 
       [GroupConnectorInformation](topic3084.md) _info_
    )  
  
#### Parameters

 _info_
    The new group connect details for this connector.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupConnector Interface](topic1706.md)   
[IGroupConnector Members](topic1707.md)


