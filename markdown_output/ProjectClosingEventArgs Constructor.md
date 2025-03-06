![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectClosingEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4092.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectClosingEventArgs Class](topic4086.md) : ProjectClosingEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_isSaving_
    The value to determine if the project is being saved or not.

Glossary Item Box

Creates a new instance of the [ProjectClosingEventArgs](topic4086.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _isSaving_ As Boolean _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim isSaving As Boolean
     
    Dim instance As New [ProjectClosingEventArgs](topic4086.md)(isSaving)  
  
C#|   
---|---  
      
    
    public ProjectClosingEventArgs( 
       bool _isSaving_
    )  
  
#### Parameters

 _isSaving_
    The value to determine if the project is being saved or not.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectClosingEventArgs Class](topic4086.md)   
[ProjectClosingEventArgs Members](topic4087.md)

©2024 DriveWorks Ltd. All Rights Reserved.
