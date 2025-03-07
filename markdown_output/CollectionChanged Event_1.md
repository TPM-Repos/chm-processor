Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CollectionChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTableColumns Class](topic3968.md) : CollectionChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raise whenever a column is created, deleted or moved (this collection changes). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event CollectionChanged As NotifyCollectionChangedEventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTableColumns](topic3968.md)
    Dim handler As NotifyCollectionChangedEventHandler
     
    AddHandler instance.CollectionChanged, handler  
  
C#|   
---|---  
      
    
    public event NotifyCollectionChangedEventHandler CollectionChanged  
  
# Event Data

The event handler receives an argument of type NotifyCollectionChangedEventArgs containing data related to this event. The following **NotifyCollectionChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
Action|   
NewItems|   
NewStartingIndex|   
OldItems|   
OldStartingIndex|   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTableColumns Class](topic3968.md)   
[ProjectCalculationTableColumns Members](topic3969.md)


