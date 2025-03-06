![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentParents Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13395.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetComponentParents( _
       ByVal _componentHandle_ As ComponentHandle, _
       ByVal _includeDeleted_ As Boolean _
    ) As ComponentHandle()  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)

©2024 DriveWorks Ltd. All Rights Reserved.
