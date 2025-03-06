       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TaskListEntryUpdated Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : TaskListEntryUpdated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an entry in the specification task list is updated. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event TaskListEntryUpdated As [SpecificationTaskListEntryEventHandler](topic11823.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As [SpecificationTaskListEntryEventHandler](topic11823.md)
     
    AddHandler instance.TaskListEntryUpdated, handler  
  
C#|   
---|---  
      
    
    public event [SpecificationTaskListEntryEventHandler](topic11823.md) TaskListEntryUpdated  
  
# Event Data

The event handler receives an argument of type [SpecificationTaskListEntryEventArgs](topic11548.md) containing data related to this event. The following **SpecificationTaskListEntryEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Entry](topic11558.md)| Gets the entry that is the target of the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


