Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EntryAdded Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationTaskList Class](topic11525.md) : EntryAdded Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an entry is added to the list. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event EntryAdded As [SpecificationTaskListEntryEventHandler](topic11823.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationTaskList](topic11525.md)
    Dim handler As [SpecificationTaskListEntryEventHandler](topic11823.md)
     
    AddHandler instance.EntryAdded, handler  
  
C#|   
---|---  
      
    
    public event [SpecificationTaskListEntryEventHandler](topic11823.md) EntryAdded  
  
# Event Data

The event handler receives an argument of type [SpecificationTaskListEntryEventArgs](topic11548.md) containing data related to this event. The following **SpecificationTaskListEntryEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Entry](topic11558.md)| Gets the entry that is the target of the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationTaskList Class](topic11525.md)   
[SpecificationTaskList Members](topic11526.md)


