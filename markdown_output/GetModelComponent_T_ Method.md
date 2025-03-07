_T_
    A version of SolidWorks.Interop.Component2

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetModelComponent<T> Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISolidWorksState Interface](topic13419.md) : GetModelComponent<T> Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the root component for the current model. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetModelComponent(Of T)() As T  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksState](topic13419.md)
    Dim value As T
     
    value = instance.GetModelComponent(Of T)()  
  
C#|   
---|---  
      
    
    T GetModelComponent<T>()  
  
#### Type Parameters

_T_
    A version of SolidWorks.Interop.Component2

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISolidWorksState Interface](topic13419.md)   
[ISolidWorksState Members](topic13420.md)


