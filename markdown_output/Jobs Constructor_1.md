![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Jobs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3622.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Jobs Class](topic3615.md) : Jobs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_inProgressJobs_
    The jobs currently being processed.

_pendingJobs_
    The jobs in the pool waiting to be processed.

Glossary Item Box

Creates an instance of the [Jobs](topic3615.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _inProgressJobs_() As [Job](topic3582.md), _
       ByVal _pendingJobs_() As [Job](topic3582.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim inProgressJobs() As [Job](topic3582.md)
    Dim pendingJobs() As [Job](topic3582.md)
     
    Dim instance As New [Jobs](topic3615.md)(inProgressJobs, pendingJobs)  
  
C#|   
---|---  
      
    
    public Jobs( 
       [Job](topic3582.md)[] _inProgressJobs_ ,
       [Job](topic3582.md)[] _pendingJobs_
    )  
  
#### Parameters

 _inProgressJobs_
    The jobs currently being processed.
_pendingJobs_
    The jobs in the pool waiting to be processed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Jobs Class](topic3615.md)   
[Jobs Members](topic3616.md)

©2024 DriveWorks Ltd. All Rights Reserved.
