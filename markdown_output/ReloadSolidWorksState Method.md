![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReloadSolidWorksState Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13372.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ICaptureViewHost Interface](topic13363.md) : ReloadSolidWorksState Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_switchDefaultTab_
    Whether to switch the default tab.

Glossary Item Box

Reloads the SolidWorks state. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub ReloadSolidWorksState( _
       ByVal _switchDefaultTab_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ICaptureViewHost](topic13363.md)
    Dim switchDefaultTab As Boolean
     
    instance.ReloadSolidWorksState(switchDefaultTab)  
  
C#|   
---|---  
      
    
    void ReloadSolidWorksState( 
       bool _switchDefaultTab_
    )  
  
#### Parameters

 _switchDefaultTab_
    Whether to switch the default tab.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICaptureViewHost Interface](topic13363.md)   
[ICaptureViewHost Members](topic13364.md)

©2024 DriveWorks Ltd. All Rights Reserved.
