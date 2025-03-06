![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentReferences(ComponentHandle,Boolean) Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) > [GetComponentReferences Method](topic13396.md) : GetComponentReferences(ComponentHandle,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentHandle_
    The component for which to find all references.

_includeDeleted_
    Whether to include deleted components.

Glossary Item Box

Gets all components that hold references to the given component. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function GetComponentReferences( _
       ByVal _componentHandle_ As ComponentHandle, _
       ByVal _includeDeleted_ As Boolean _
    ) As ComponentHandle()  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim componentHandle As ComponentHandle
    Dim includeDeleted As Boolean
    Dim value() As ComponentHandle
     
    value = instance.GetComponentReferences(componentHandle, includeDeleted)  
  
C#|   
---|---  
      
    
    ComponentHandle[] GetComponentReferences( 
       ComponentHandle _componentHandle_ ,
       bool _includeDeleted_
    )  
  
#### Parameters

 _componentHandle_
    The component for which to find all references.
_includeDeleted_
    Whether to include deleted components.

#### Return Value

An array of all components that holds a reference to the given component.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)   
[Overload List](topic13396.md)


