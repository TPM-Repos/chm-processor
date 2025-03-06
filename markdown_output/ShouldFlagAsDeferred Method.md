![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ShouldFlagAsDeferred Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14523.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectDrawing Class](topic14516.md) : ShouldFlagAsDeferred Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_deferredComponentNames_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Function ShouldFlagAsDeferred( _
       ByVal _deferredComponentNames_ As IEnumerable(Of String) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectDrawing](topic14516.md)
    Dim deferredComponentNames As IEnumerable(Of String)
    Dim value As Boolean
     
    value = instance.ShouldFlagAsDeferred(deferredComponentNames)  
  
C#|   
---|---  
      
    
    protected override bool ShouldFlagAsDeferred( 
       IEnumerable<string> _deferredComponentNames_
    )  
  
#### Parameters

 _deferredComponentNames_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectDrawing Class](topic14516.md)   
[ProjectDrawing Members](topic14517.md)

©2024 DriveWorks Ltd. All Rights Reserved.
