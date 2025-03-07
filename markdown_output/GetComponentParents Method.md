Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentParents Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) : GetComponentParents Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentHandle_
    A handle to the component for which to find all parents.

_includeDeleted_
    Whether to include deleted components.

Glossary Item Box

Gets all parents that holds references the given component. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetComponentParents( _
       ByVal _componentHandle_ As ComponentHandle, _
       ByVal _includeDeleted_ As Boolean _
    ) As ComponentHandle()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim componentHandle As ComponentHandle
    Dim includeDeleted As Boolean
    Dim value() As ComponentHandle
     
    value = instance.GetComponentParents(componentHandle, includeDeleted)  
  
C#|   
---|---  
      
    
    ComponentHandle[] GetComponentParents( 
       ComponentHandle _componentHandle_ ,
       bool _includeDeleted_
    )  
  
#### Parameters

 _componentHandle_
    A handle to the component for which to find all parents.
_includeDeleted_
    Whether to include deleted components.

#### Return Value

An array of all parents that holds a reference to the given component.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)


