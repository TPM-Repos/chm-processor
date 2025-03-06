![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StayOnSchedule Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12674.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [StartSpecificationTimerTask Class](topic12661.md) : StayOnSchedule Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether the timer should stay on schedule or not. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property StayOnSchedule As [FlowProperty(Of Boolean)](topic10978.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [StartSpecificationTimerTask](topic12661.md)
    Dim value As [FlowProperty(Of Boolean)](topic10978.md)
     
    instance.StayOnSchedule = value
     
    value = instance.StayOnSchedule  
  
C#|   
---|---  
      
    
    public [FlowProperty<bool>](topic10978.md) StayOnSchedule {get; set;}  
  
# ![](dotnetimages/collapse.gif)Remarks

If True, the timer will not be halted during macro execution meaning that if execution carries on into the next interval of the timer, that interval will be skipped. If False, the timer will be paused during macro execution and resumed upon completion, meaning every interval is respected.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[StartSpecificationTimerTask Class](topic12661.md)   
[StartSpecificationTimerTask Members](topic12662.md)

©2024 DriveWorks Ltd. All Rights Reserved.
