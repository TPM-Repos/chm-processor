![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentHandle Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13393.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) : GetComponentHandle Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fullPath_
    The path to the component for which to retrieve a handle.

Glossary Item Box

Gets the component handle for the component with the given path. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetComponentHandle( _
       ByVal _fullPath_ As String _
    ) As ComponentHandle  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim fullPath As String
    Dim value As ComponentHandle
     
    value = instance.GetComponentHandle(fullPath)  
  
C#|   
---|---  
      
    
    ComponentHandle GetComponentHandle( 
       string _fullPath_
    )  
  
#### Parameters

 _fullPath_
    The path to the component for which to retrieve a handle.

#### Return Value

A handle to the component with the given path.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)

©2024 DriveWorks Ltd. All Rights Reserved.
