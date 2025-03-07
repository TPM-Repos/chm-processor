Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetStatus(Guid) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupCapturedComponents Class](topic3022.md) > [GetStatus Method](topic3043.md) : GetStatus(Guid) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The component identifier for which to get details.

Glossary Item Box

Gets the status of a component in the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetStatus( _
       ByVal _componentId_ As Guid _
    ) As [CapturedComponentStatus](topic2459.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupCapturedComponents](topic3022.md)
    Dim componentId As Guid
    Dim value As [CapturedComponentStatus](topic2459.md)
     
    value = instance.GetStatus(componentId)  
  
C#|   
---|---  
      
    
    public [CapturedComponentStatus](topic2459.md) GetStatus( 
       Guid _componentId_
    )  
  
#### Parameters

 _componentId_
    The component identifier for which to get details.

# Remarks

A valid captured component status instance is always returned, even if a component with the specified identifier does not exist in the group.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupCapturedComponents Class](topic3022.md)   
[GroupCapturedComponents Members](topic3023.md)   
[Overload List](topic3043.md)


