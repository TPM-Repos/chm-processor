![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ClipboardContains Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13514.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ClipboardSupport Class](topic13507.md) : ClipboardContains Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_clipboardType_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ClipboardContains( _
       ByVal _clipboardType_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim clipboardType As String
    Dim value As Boolean
     
    value = [ClipboardSupport](topic13507.md).ClipboardContains(clipboardType)  
  
C#|   
---|---  
      
    
    public static bool ClipboardContains( 
       string _clipboardType_
    )  
  
#### Parameters

 _clipboardType_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ClipboardSupport Class](topic13507.md)   
[ClipboardSupport Members](topic13508.md)

©2024 DriveWorks Ltd. All Rights Reserved.
