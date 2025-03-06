![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RepeatDays Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6862.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Schedule Namespace](topic6848.md) > [ScheduleConnectorConfiguration Class](topic6851.md) : RepeatDays Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Get/Sets the days the schedule will be repeated on. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property RepeatDays As String()  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ScheduleConnectorConfiguration](topic6851.md)
    Dim value() As String
     
    instance.RepeatDays = value
     
    value = instance.RepeatDays  
  
C#|   
---|---  
      
    
    public string[] RepeatDays {get; set;}  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ScheduleConnectorConfiguration Class](topic6851.md)   
[ScheduleConnectorConfiguration Members](topic6852.md)

©2024 DriveWorks Ltd. All Rights Reserved.
