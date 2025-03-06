       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VirtualItemDeleted Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IVirtualSplitCommandButton Interface](topic598.md) : VirtualItemDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised after the user presses the delete key on a virtual item on the drop down list. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event VirtualItemDeleted As [VirtualItemDeletedEventHandler](topic1273.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IVirtualSplitCommandButton](topic598.md)
    Dim handler As [VirtualItemDeletedEventHandler](topic1273.md)
     
    AddHandler instance.VirtualItemDeleted, handler  
  
C#|   
---|---  
      
    
    event [VirtualItemDeletedEventHandler](topic1273.md) VirtualItemDeleted  
  
# Event Data

The event handler receives an argument of type [VirtualItemDeletedEventArgs](topic1167.md) containing data related to this event. The following **VirtualItemDeletedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Item](topic1174.md)| Gets the data for the virtual item that was selected.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IVirtualSplitCommandButton Interface](topic598.md)   
[IVirtualSplitCommandButton Members](topic599.md)


