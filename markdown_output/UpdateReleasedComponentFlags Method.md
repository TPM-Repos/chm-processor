UpdateReleasedComponentFlags Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : UpdateReleasedComponentFlags Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The Id of the component for which to change the flags.

_newFlags_
    The new flags to apply to the component.

Glossary Item Box

Updates the specified released component's flags. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function UpdateReleasedComponentFlags( _
       ByVal _componentId_ As Guid, _
       ByVal _newFlags_ As [ReleasedComponentFlags](topic6145.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentId As Guid
    Dim newFlags As [ReleasedComponentFlags](topic6145.md)
    Dim value As Boolean
     
    value = instance.UpdateReleasedComponentFlags(componentId, newFlags)  
  
C#|   
---|---  
      
    
    public bool UpdateReleasedComponentFlags( 
       Guid _componentId_ ,
       [ReleasedComponentFlags](topic6145.md) _newFlags_
    )  
  
#### Parameters

 _componentId_
    The Id of the component for which to change the flags.
_newFlags_
    The new flags to apply to the component.

#### Return Value

True if the flags were successfully updated, otherwise False.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


