Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRootComponent Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentsResults Class](topic6300.md) : GetRootComponent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentSetName_
    Gets the root component for the component set with the given name.

Glossary Item Box

Gets a root component based on the name of the component set 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetRootComponent( _
       ByVal _componentSetName_ As String _
    ) As [ReleasedComponent](topic6324.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentsResults](topic6300.md)
    Dim componentSetName As String
    Dim value As [ReleasedComponent](topic6324.md)
     
    value = instance.GetRootComponent(componentSetName)  
  
C#|   
---|---  
      
    
    public [ReleasedComponent](topic6324.md) GetRootComponent( 
       string _componentSetName_
    )  
  
#### Parameters

 _componentSetName_
    Gets the root component for the component set with the given name.

#### Return Value

A released component for the given component set, or a null reference if the component set

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentsResults Class](topic6300.md)   
[ReleaseComponentsResults Members](topic6301.md)


