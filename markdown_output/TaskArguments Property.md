       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TaskArguments Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6869.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Schedule Namespace](topic6848.md) > [ScheduleConnectorConfiguration Class](topic6851.md) : TaskArguments Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Get/Sets the TaskArguments that will be used. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property TaskArguments As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ScheduleConnectorConfiguration](topic6851.md)
    Dim value() As String
     
    instance.TaskArguments = value
     
    value = instance.TaskArguments  
  
C#|   
---|---  
      
    
    public string[] TaskArguments {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ScheduleConnectorConfiguration Class](topic6851.md)   
[ScheduleConnectorConfiguration Members](topic6852.md)

©2024 DriveWorks Ltd. All Rights Reserved.
