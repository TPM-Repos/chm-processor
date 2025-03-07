Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponent Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : GetComponent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The unique identifier of the component.

Glossary Item Box

Gets the released component with the specified identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetComponent( _
       ByVal _componentId_ As Guid _
    ) As [ReleasedComponent](topic6324.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentId As Guid
    Dim value As [ReleasedComponent](topic6324.md)
     
    value = instance.GetComponent(componentId)  
  
C#|   
---|---  
      
    
    public [ReleasedComponent](topic6324.md) GetComponent( 
       Guid _componentId_
    )  
  
#### Parameters

 _componentId_
    The unique identifier of the component.

#### Return Value

The component with the specified identifier if it is registered, otherwise a null reference.

# Exceptions

Exception| Description  
---|---  
System.NotSupportedException| The component type is not supported.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


