Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Arguments Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IScheduleConnectorTask Interface](topic1734.md) : Arguments Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The arguments to use in the task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Property Arguments As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IScheduleConnectorTask](topic1734.md)
    Dim value() As String
     
    instance.Arguments = value
     
    value = instance.Arguments  
  
C#|   
---|---  
      
    
    string[] Arguments {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IScheduleConnectorTask Interface](topic1734.md)   
[IScheduleConnectorTask Members](topic1735.md)


