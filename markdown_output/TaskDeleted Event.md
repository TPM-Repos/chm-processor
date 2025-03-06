       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TaskDeleted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TaskSequence Class](topic11713.md) : TaskDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when a task is deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event TaskDeleted As [TaskEventHandler](topic11826.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TaskSequence](topic11713.md)
    Dim handler As [TaskEventHandler](topic11826.md)
     
    AddHandler instance.TaskDeleted, handler  
  
C#|   
---|---  
      
    
    public event [TaskEventHandler](topic11826.md) TaskDeleted  
  
# Event Data

The event handler receives an argument of type [TaskEventArgs](topic11672.md) containing data related to this event. The following **TaskEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Task](topic11682.md)| Gets the task which is the target of the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskSequence Class](topic11713.md)   
[TaskSequence Members](topic11714.md)


