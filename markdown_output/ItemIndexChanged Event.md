Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ItemIndexChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationDef Class](topic4019.md) : ItemIndexChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when any item is moved up or down. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ItemIndexChanged As EventHandler(Of IndexesChangedEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationDef](topic4019.md)
    Dim handler As EventHandler(Of IndexesChangedEventArgs)
     
    AddHandler instance.ItemIndexChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<IndexesChangedEventArgs> ItemIndexChanged  
  
# Event Data

The event handler receives an argument of type [IndexesChangedEventArgs](topic3496.md) containing data related to this event. The following **IndexesChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[ChangedIndexes](topic3503.md)| The original index, before the change.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[ProjectChildSpecificationDef Members](topic4020.md)


