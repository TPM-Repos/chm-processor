![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProcessBegun Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10342.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [IEventReportWriter Interface](topic10336.md) : ProcessBegun Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a process is begun. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event ProcessBegun As [ProcessEventHandler](topic10509.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IEventReportWriter](topic10336.md)
    Dim handler As [ProcessEventHandler](topic10509.md)
     
    AddHandler instance.ProcessBegun, handler  
  
C#|   
---|---  
      
    
    event [ProcessEventHandler](topic10509.md) ProcessBegun  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [ProcessEventArgs](topic10424.md) containing data related to this event. The following **ProcessEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[ProcessClass](topic10431.md)| Gets the process class.   
[ProcessDescription](topic10432.md)| Gets the process description.   
[ProcessTarget](topic10433.md)| Gets the process target.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IEventReportWriter Interface](topic10336.md)   
[IEventReportWriter Members](topic10337.md)

©2024 DriveWorks Ltd. All Rights Reserved.
