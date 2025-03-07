Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentHandle Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) : GetComponentHandle Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fullPath_
    The path to the component for which to retrieve a handle.

Glossary Item Box

Gets the component handle for the component with the given path. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetComponentHandle( _
       ByVal _fullPath_ As String _
    ) As ComponentHandle  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim fullPath As String
    Dim value As ComponentHandle
     
    value = instance.GetComponentHandle(fullPath)  
  
C#|   
---|---  
      
    
    ComponentHandle GetComponentHandle( 
       string _fullPath_
    )  
  
#### Parameters

 _fullPath_
    The path to the component for which to retrieve a handle.

#### Return Value

A handle to the component with the given path.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)


