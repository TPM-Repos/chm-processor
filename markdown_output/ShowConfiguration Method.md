![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ShowConfiguration Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2048.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [IHasConfiguration Interface](topic2043.md) : ShowConfiguration Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_owner_
    The parent window for any dialogs.

Glossary Item Box

Shows the configuration user interface. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub ShowConfiguration( _
       ByVal _owner_ As IWin32Window _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IHasConfiguration](topic2043.md)
    Dim owner As IWin32Window
     
    instance.ShowConfiguration(owner)  
  
C#|   
---|---  
      
    
    void ShowConfiguration( 
       IWin32Window _owner_
    )  
  
#### Parameters

 _owner_
    The parent window for any dialogs.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IHasConfiguration Interface](topic2043.md)   
[IHasConfiguration Members](topic2044.md)

©2024 DriveWorks Ltd. All Rights Reserved.
