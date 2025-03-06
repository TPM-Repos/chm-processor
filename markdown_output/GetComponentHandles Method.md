![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentHandles Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13394.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) : GetComponentHandles Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sort_
    Whether to sort the list (based on master path).

Glossary Item Box

Gets an array of all known component handles. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetComponentHandles( _
       ByVal _sort_ As Boolean _
    ) As ComponentHandle()  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)

©2024 DriveWorks Ltd. All Rights Reserved.
