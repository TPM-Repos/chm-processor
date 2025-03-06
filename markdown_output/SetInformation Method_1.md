       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetInformation Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1868.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [GroupConnectorBase<T> Class](topic1857.md) : SetInformation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_info_
    The information to set.

Glossary Item Box

Sets the connector's information. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetInformation( _
       ByVal _info_ As [GroupConnectorInformation](topic3084.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupConnectorBase(Of T)](topic1857.md)
    Dim info As [GroupConnectorInformation](topic3084.md)
     
    instance.SetInformation(info)  
  
C#|   
---|---  
      
    
    public void SetInformation( 
       [GroupConnectorInformation](topic3084.md) _info_
    )  
  
#### Parameters

 _info_
    The information to set.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupConnectorBase<T> Class](topic1857.md)   
[GroupConnectorBase<T> Members](topic1858.md)

©2024 DriveWorks Ltd. All Rights Reserved.
