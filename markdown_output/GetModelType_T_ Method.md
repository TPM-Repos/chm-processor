_T_
    A version of SolidWorks.Interop.swconst.swDocumentTypes_e.

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetModelType<T> Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISolidWorksState Interface](topic13419.md) : GetModelType<T> Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The type of the Model currently loaded in SolidWorks. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetModelType(Of T)() As T  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksState](topic13419.md)
    Dim value As T
     
    value = instance.GetModelType(Of T)()  
  
C#|   
---|---  
      
    
    T GetModelType<T>()  
  
#### Type Parameters

_T_
    A version of SolidWorks.Interop.swconst.swDocumentTypes_e.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISolidWorksState Interface](topic13419.md)   
[ISolidWorksState Members](topic13420.md)


