SelectedItemsChanged Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISelectionSite Interface](topic422.md) : SelectedItemsChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the selected items property has been changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event SelectedItemsChanged As [SelectionChangedEventHandler](topic1270.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISelectionSite](topic422.md)
    Dim handler As [SelectionChangedEventHandler](topic1270.md)
     
    AddHandler instance.SelectedItemsChanged, handler  
  
C#|   
---|---  
      
    
    event [SelectionChangedEventHandler](topic1270.md) SelectedItemsChanged  
  
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

[ISelectionSite Interface](topic422.md)   
[ISelectionSite Members](topic423.md)


