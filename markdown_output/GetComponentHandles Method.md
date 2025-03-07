Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentHandles Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) : GetComponentHandles Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sort_
    Whether to sort the list (based on master path).

Glossary Item Box

Gets an array of all known component handles. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetComponentHandles( _
       ByVal _sort_ As Boolean _
    ) As ComponentHandle()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim sort As Boolean
    Dim value() As ComponentHandle
     
    value = instance.GetComponentHandles(sort)  
  
C#|   
---|---  
      
    
    ComponentHandle[] GetComponentHandles( 
       bool _sort_
    )  
  
#### Parameters

 _sort_
    Whether to sort the list (based on master path).

#### Return Value

An array of handles to all known component.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)


