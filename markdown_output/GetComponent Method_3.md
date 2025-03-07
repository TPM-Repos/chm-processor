Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponent Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentsResults Class](topic6300.md) : GetComponent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The unique identifier of the released component to retrieve.

Glossary Item Box

Gets a released component based on it's unique identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetComponent( _
       ByVal _componentId_ As Guid _
    ) As [ReleasedComponent](topic6324.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentsResults](topic6300.md)
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
    The unique identifier of the released component to retrieve.

#### Return Value

The component with the given identifier, or a null reference if no component exists with the given identifier.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentsResults Class](topic6300.md)   
[ReleaseComponentsResults Members](topic6301.md)


