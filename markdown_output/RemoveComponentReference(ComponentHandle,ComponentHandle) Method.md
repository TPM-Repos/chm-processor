![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveComponentReference(ComponentHandle,ComponentHandle) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13405.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) > [RemoveComponentReference Method](topic13404.md) : RemoveComponentReference(ComponentHandle,ComponentHandle) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_parentHandle_
    The parent from which to remove the reference.

_childHandle_
    The child to remove from the parent.

Glossary Item Box

Uncaptures the specified child from the parent and returns the number of places where the child is still used. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function RemoveComponentReference( _
       ByVal _parentHandle_ As ComponentHandle, _
       ByVal _childHandle_ As ComponentHandle _
    ) As Integer  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim parentHandle As ComponentHandle
    Dim childHandle As ComponentHandle
    Dim value As Integer
     
    value = instance.RemoveComponentReference(parentHandle, childHandle)  
  
C#|   
---|---  
      
    
    int RemoveComponentReference( 
       ComponentHandle _parentHandle_ ,
       ComponentHandle _childHandle_
    )  
  
#### Parameters

 _parentHandle_
    The parent from which to remove the reference.
_childHandle_
    The child to remove from the parent.

#### Return Value

The number of parents which still hold a reference to the child after it is removed.

# ![](dotnetimages/collapse.gif)Remarks

If the reference count drops to zero, then the child is completely removed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)   
[Overload List](topic13404.md)

©2024 DriveWorks Ltd. All Rights Reserved.
