_T_
    A version of SolidWorks.Interop.Component2

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetModelChildComponents<T> Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISolidWorksState Interface](topic13419.md) : GetModelChildComponents<T> Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all the features and referenced components in the current model. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetModelChildComponents(Of T)() As T()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksState](topic13419.md)
    Dim value() As T
     
    value = instance.GetModelChildComponents(Of T)()  
  
C#|   
---|---  
      
    
    T[] GetModelChildComponents<T>()  
  
#### Type Parameters

_T_
    A version of SolidWorks.Interop.Component2

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISolidWorksState Interface](topic13419.md)   
[ISolidWorksState Members](topic13420.md)


