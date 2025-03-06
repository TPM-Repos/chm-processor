UpdateReleasedComponentTags Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : UpdateReleasedComponentTags Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The Id of the component for which to change the tags.

_newTags_
    The new tags to apply to the component.

Glossary Item Box

Updates the specified released component's tags. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function UpdateReleasedComponentTags( _
       ByVal _componentId_ As Guid, _
       ByVal _newTags_() As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentId As Guid
    Dim newTags() As String
    Dim value As Boolean
     
    value = instance.UpdateReleasedComponentTags(componentId, newTags)  
  
C#|   
---|---  
      
    
    public bool UpdateReleasedComponentTags( 
       Guid _componentId_ ,
       string[] _newTags_
    )  
  
#### Parameters

 _componentId_
    The Id of the component for which to change the tags.
_newTags_
    The new tags to apply to the component.

#### Return Value

True if the tags were successfully updated, otherwise False.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


