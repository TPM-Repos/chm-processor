       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VirtualItemDeleting Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IVirtualSplitCommandButton Interface](topic598.md) : VirtualItemDeleting Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the user presses the delete key on a virtual item on the drop down list. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event VirtualItemDeleting As [VirtualItemDeletingEventHandler](topic1274.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IVirtualSplitCommandButton](topic598.md)
    Dim handler As [VirtualItemDeletingEventHandler](topic1274.md)
     
    AddHandler instance.VirtualItemDeleting, handler  
  
C#|   
---|---  
      
    
    event [VirtualItemDeletingEventHandler](topic1274.md) VirtualItemDeleting  
  
# Event Data

The event handler receives an argument of type [VirtualItemDeletingEventArgs](topic1175.md) containing data related to this event. The following **VirtualItemDeletingEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Cancel](topic1182.md)| Gets/sets whether the delete should be cancelled.   
[Item](topic1183.md)| Gets the data for the virtual item that was selected.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IVirtualSplitCommandButton Interface](topic598.md)   
[IVirtualSplitCommandButton Members](topic599.md)


