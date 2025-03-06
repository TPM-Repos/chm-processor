![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReleaseComponentReportTracker Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6298.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentReportTracker Class](topic6292.md) : ReleaseComponentReportTracker Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reportWriter_
    The report writer to use for the release component process.

Glossary Item Box

Create a new report tracker that reports release component information to the supplied report writer. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _reportWriter_ As [IReportWriter](topic10344.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim reportWriter As [IReportWriter](topic10344.md)
     
    Dim instance As New [ReleaseComponentReportTracker](topic6292.md)(reportWriter)  
  
C#|   
---|---  
      
    
    public ReleaseComponentReportTracker( 
       [IReportWriter](topic10344.md) _reportWriter_
    )  
  
#### Parameters

 _reportWriter_
    The report writer to use for the release component process.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleaseComponentReportTracker Class](topic6292.md)   
[ReleaseComponentReportTracker Members](topic6293.md)

©2024 DriveWorks Ltd. All Rights Reserved.
