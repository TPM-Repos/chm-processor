![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ScheduleType Enumeration   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6850.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Schedule Namespace](topic6848.md) : ScheduleType Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The type of schedule to use for the connector. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum ScheduleType 
       Inherits System.Enum  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ScheduleType](topic6850.md)  
  
C#|   
---|---  
      
    
    public enum ScheduleType : System.Enum   
  
# ![](dotnetimages/collapse.gif)Members

Member| Description  
---|---  
**Advanced**|  The schedule uses a Cron expression.  
**Basic**|  The schedule is a basic run once schedule.  
**Repeating**|  The schedule repeats, for example, every 10 seconds.  
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Connectors.Schedule.ScheduleType**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorks.Connectors.Schedule Namespace](topic6848.md)

©2024 DriveWorks Ltd. All Rights Reserved.
