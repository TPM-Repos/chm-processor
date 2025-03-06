![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProxyReportWriter Constructor(IReportWriter)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10442.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [ProxyReportWriter Class](topic10434.md) > [ProxyReportWriter Constructor](topic10440.md) : ProxyReportWriter Constructor(IReportWriter)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_writer_
    The writer to which to proxy reporting calls (may be null).

Glossary Item Box

Initializes a new instance of the [ProxyReportWriter](topic10434.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _writer_ As [IReportWriter](topic10344.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim writer As [IReportWriter](topic10344.md)
     
    Dim instance As New [ProxyReportWriter](topic10434.md)(writer)  
  
C#|   
---|---  
      
    
    public ProxyReportWriter( 
       [IReportWriter](topic10344.md) _writer_
    )  
  
#### Parameters

 _writer_
    The writer to which to proxy reporting calls (may be null).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProxyReportWriter Class](topic10434.md)   
[ProxyReportWriter Members](topic10435.md)   
[Overload List](topic10440.md)

©2024 DriveWorks Ltd. All Rights Reserved.
