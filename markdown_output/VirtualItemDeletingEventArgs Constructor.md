       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VirtualItemDeletingEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1181.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [VirtualItemDeletingEventArgs Class](topic1175.md) : VirtualItemDeletingEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_item_
    The data for the virtual item that was selected.

Glossary Item Box

Initializes a new instance of the [VirtualItemDeletingEventArgs](topic1175.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _item_ As [VirtualItemData](topic1154.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim item As [VirtualItemData](topic1154.md)
     
    Dim instance As New [VirtualItemDeletingEventArgs](topic1175.md)(item)  
  
C#|   
---|---  
      
    
    public VirtualItemDeletingEventArgs( 
       [VirtualItemData](topic1154.md) _item_
    )  
  
#### Parameters

 _item_
    The data for the virtual item that was selected.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[VirtualItemDeletingEventArgs Class](topic1175.md)   
[VirtualItemDeletingEventArgs Members](topic1176.md)

©2024 DriveWorks Ltd. All Rights Reserved.
