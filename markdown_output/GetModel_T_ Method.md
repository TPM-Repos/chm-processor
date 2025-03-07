_T_
    A version of SolidWorks.Interop.ModelDoc2

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetModel<T> Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISolidWorksState Interface](topic13419.md) : GetModel<T> Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the model currently open in SolidWorks. The type of it is one of the derivatives of ModelDoc2, AssemblyDoc/PartDoc/DrawingDoc. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetModel(Of T As Class)() As T  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksState](topic13419.md)
    Dim value As T
     
    value = instance.GetModel(Of T)()  
  
C#|   
---|---  
      
    
    T GetModel<T>()
    where T: class  
  
#### Type Parameters

_T_
    A version of SolidWorks.Interop.ModelDoc2

#### Return Value

A reference to the open model as the given type, or a null reference (Nothing in Visual Basic) if the active model is not of the given type, or if no model is currently open.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISolidWorksState Interface](topic13419.md)   
[ISolidWorksState Members](topic13420.md)


