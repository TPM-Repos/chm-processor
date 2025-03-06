       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SelectedItemsChanged Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ViewControl Class](topic1119.md) : SelectedItemsChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event SelectedItemsChanged As [SelectionChangedEventHandler](topic1270.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ViewControl](topic1119.md)
    Dim handler As [SelectionChangedEventHandler](topic1270.md)
     
    AddHandler instance.SelectedItemsChanged, handler  
  
C#|   
---|---  
      
    
    public event [SelectionChangedEventHandler](topic1270.md) SelectedItemsChanged  
  
# Event Data

The event handler receives an argument of type [SelectionChangeEventArgs](topic926.md) containing data related to this event. The following **SelectionChangeEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[NewSelectedItems](topic933.md)| Gets the new selection.   
[OldSelectedItems](topic934.md)| Gets the selection before the change took place.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)


